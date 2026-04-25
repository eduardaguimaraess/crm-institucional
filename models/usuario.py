from models.endereco import Endereco

class Usuario:

    def __init__(self, id_usuario, nome, data_nascimento, cpf, genero, telefone, email, senha, endereco, cargo, ativo=True): # login se dá por cpf e senha
        self.id_usuario = id_usuario
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.cargo = cargo  # admin_diretor (somente ele cadastra novos usários), professor, secretario_financeiro, captador_comercial
        self.ativo = ativo

    def autenticar(self, cpf, senha):
        if not self.ativo:
            return False

        if self.cpf == cpf and self.senha == senha:
            return True

        return False

    def alterarSenha(self, nova_senha):

        self.senha = nova_senha

    def desativar(self):

        self.ativo = False