class Assinante:
    def __init__(self, id_assinante, nome, plano):
        self.id_assinante = id_assinante
        self.nome = nome
        self.plano = plano
        self.historico = [0.0] * 12 # consumo em GB um valor por mês


assinantes = []

def cadastrar_assinante(id_assinante, nome, plano):
    novo = Assinante(id_assinante, nome, plano)
    assinantes.append(novo)
    return novo