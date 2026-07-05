# 📡 Sistema de Faturamento — Provedor de Internet (ISP)

Sistema de linha de comando (CLI) em Python que simula o motor de cobrança de um provedor de internet, aplicando regras de tarifação progressiva, impostos "por dentro" e taxas fixas — o mesmo modelo matemático usado em contas de energia elétrica reguladas pela ANEEL, adaptado para consumo de dados (GB).

Projeto construído como exercício de **arquitetura em camadas**, aplicando o padrão **Repository / Service / Interface**, com cobertura de testes automatizados via **Pytest**.

---

## 🎯 Objetivo

Calcular a fatura de um assinante com base em:

- Consumo de dados (GB)
- Plano contratado (Residencial, Empresarial, Corporativo)
- Nível de congestionamento da rede no período

Além disso, o sistema permite cadastrar assinantes, lançar consumo mensal (histórico de 12 meses) e gerar relatórios analíticos sobre a base de clientes.

---

## 🧮 Regras de negócio

### Tarifas por plano (por GB consumido)

| Plano | TD (Tarifa de Dados) | TI (Tarifa de Infraestrutura) | Taxa de Equipamento |
|---|---|---|---|
| Residencial (R) | R$ 0,15 | R$ 0,10 | R$ 25,00 |
| Empresarial (E) | R$ 0,20 | R$ 0,15 | R$ 60,00 |
| Corporativo (C) | R$ 0,28 | R$ 0,22 | R$ 150,00 |

```
Custo_Base = Consumo_GB * (TD + TI)
```

### Acréscimo por congestionamento de rede

Cobrado a cada 50 GB consumidos (divisão inteira):

| Nível | Valor a cada 50 GB |
|---|---|
| Normal (N) | R$ 0,00 |
| Moderado (M) | R$ 0,90 |
| Alto (A1) | R$ 2,50 |
| Crítico (A2) | R$ 4,80 |

```
Acrescimo_Rede = (Consumo_GB // 50) * Valor_Nivel
```

### Impostos "por dentro"

Alíquota combinada de ICMS + PIS + COFINS = 27,25%:

```
Subtotal = Custo_Base + Acrescimo_Rede
Base_Calculo = Subtotal / (1 - 0.2725)
```

### Total da fatura

```
Fatura_Final = Base_Calculo + Taxa_Equipamento
```

### Teste de mesa (validação)

Residencial · 220 GB · Nível Alto (A1):

```
Custo Base:     220 * (0.15 + 0.10) = R$ 55,00
Congestionamento: (220 // 50) * 2.50 = R$ 10,00
Subtotal:       R$ 65,00
Base de Cálculo: 65,00 / 0,7275   = R$ 89,35
Taxa Equipamento:                 = R$ 25,00
TOTAL:                            = R$ 114,35
```

---

## 🏗️ Arquitetura

O projeto segue separação de responsabilidades em camadas, evitando misturar regra de negócio com entrada/saída de dados:

```
main.py                  → ponto de entrada
interface.py              → camada de apresentação (input/print, menus)
servico_assinante.py       → camada de serviço (validações e regras de negócio)
banco_dados.py             → camada de repositório (classe Assinante + estado em memória)
motor_calculo.py           → funções puras de cálculo de fatura
relatorios_analytics.py    → agregações e relatórios sobre a base de assinantes
```

**Fluxo de dependências:**

```
interface.py → servico_assinante.py → banco_dados.py
interface.py → motor_calculo.py
interface.py → relatorios_analytics.py → motor_calculo.py + banco_dados.py
```

A interface nunca acessa a lista de assinantes ou valida regras diretamente — ela delega tudo ao serviço, que por sua vez delega o armazenamento ao repositório. Isso permite trocar a camada de persistência (ex: memória → MySQL) sem alterar a interface.

---

## ⚙️ Funcionalidades

1. **Calcular fatura avulsa** — informa consumo, plano e nível de rede, recebe o valor calculado na hora.
2. **Cadastrar assinante** — registra um novo cliente com ID, nome e plano.
3. **Lançar consumo mensal** — grava o consumo de um assinante em um mês específico (1 a 12).
4. **Ver relatórios**:
   - Matriz de consumo (assinante × mês)
   - Conta mais alta entre todos os assinantes/meses
   - IDs de assinantes com consumo acima da média (indício de uso atípico)

Todas as entradas são validadas — tentativas de digitar texto onde se espera número, planos/níveis inexistentes, IDs não cadastrados ou meses fora do intervalo 1–12 são tratadas sem derrubar o programa.

---

## 🧪 Testes automatizados

O projeto conta com **21 testes** usando Pytest, cobrindo:

- Cálculo de fatura para os 3 planos e diferentes níveis de rede (casos parametrizados)
- Exceções para plano/nível inválido (`KeyError`)
- Inicialização correta da classe `Assinante` (histórico de 12 meses)
- Cadastro de assinantes no repositório
- Relatórios: identificação da conta mais alta e detecção de consumo acima da média
- Validações da camada de serviço (`ValueError` para plano inválido, assinante inexistente e mês fora do intervalo)

### Rodando os testes

```bash
pip install pytest
pytest
```

Saída esperada:

```
======================== test session starts ========================
collected 21 items

test_banco_dados.py ...                                        [ 14%]
test_motor_calculo.py ........                                 [ 52%]
test_relatorios_analytics.py ...                                [ 66%]
test_servico_assinante.py .......                                [100%]

======================== 21 passed in 0.06s ========================
```

---

## ▶️ Como executar

```bash
python main.py
```

Menu exibido:

```
=== Sistema de Faturamento ISP ===
1. Calcular fatura avulsa
2. Cadastrar assinante
3. Lançar consumo mensal
4. Ver relatórios
5. Sair
```

---

## 🛠️ Tecnologias

- Python 3.14
- Pytest (testes unitários)
- Programação Orientada a Objetos
- Arquitetura em camadas (Repository / Service / Interface)

---

## 📌 Roadmap (evolução planejada)

- [ ] Persistência em MySQL (substituindo o armazenamento em memória)
- [ ] Variáveis de ambiente (`.env`) para credenciais de banco
- [ ] Exposição das funcionalidades como API REST (Flask)
- [ ] Documentação de rotas via Postman/Insomnia

---

## 👤 Autor

**Maickon Santos**
Estudante de Análise e Desenvolvimento de Sistemas — UNIVERSO (Recife/PE)
[LinkedIn](https://linkedin.com/in/maickon-santos-0903163b3) · [GitHub](https://github.com/Maickon0709)
