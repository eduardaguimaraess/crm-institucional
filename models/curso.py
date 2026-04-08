class Curso:

    def __init__(self, id_curso, nome, carga_horaria, valor, ativo=True):

        self.id_curso = id_curso
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.valor = valor
        self.ativo = ativo

    # Retorna valor formatado em R$
    def valor_formatado(self):
        return f"R$ {self.valor:.2f}".replace(".", ",")