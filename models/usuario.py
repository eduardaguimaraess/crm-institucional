class Usuario:
    """
    Classe Usuario
    Responsável por autenticação e controle de acesso ao sistema.
    """

    def __init__(self, id, nome, data_nascimento, cpf, genero, telefone, email, senha, perfil, ativo=True):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.ativo = ativo

    def autenticar(self, cpf, senha):
        """
        Verifica se o usuário pode se autenticar no sistema.
        Retorna True se as credenciais estiverem corretas e o usuário ativo.
        """
        if not self.ativo:
            return False

        if self.cpf == cpf and self.senha == senha:
            return True

        return False

    def alterarSenha(self, nova_senha):
        """
        Altera a senha do usuário.
        """
        self.senha = nova_senha

    def desativar(self):
        """
        Desativa o usuário no sistema.
        """
        self.ativo = False