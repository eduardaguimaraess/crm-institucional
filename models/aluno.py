from endereco import Endereco

# Classe Aluno
class Aluno:

    def __init__(self, id_aluno, nome, data_nascimento, cpf,
                 genero, telefone, email, endereco, responsavel=None, status="ativo"): #ainda não responsável

        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.responsavel = responsavel
        self.status = "Ativo" # ativo, trancado, cancelado, concluido