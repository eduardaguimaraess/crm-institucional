from models.endereco import Endereco

class Responsavel:

    def __init__(self, id_responsavel, nome, cpf, telefone, email, genero, endereco):

        self.id_responsavel = id_responsavel
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.genero = genero
        self.endereco = endereco

        # Lista de alunos vinculados
        self.aluno = []