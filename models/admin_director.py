from usuario import Usuario

class Admin(Usuario):
    """
    Classe Admin
    Responsável por gerenciar usuários no sistema.
    """

    def __init__(self, id_usuario, nome, data_nascimento, cpf, genero,
                 telefone, email, senha,
                 id_admin, salario, data_admissao,
                 cargo="admin_diretor", ativo=True):

        super().__init__(
            id_usuario, nome, data_nascimento, cpf,
            genero, telefone, email, senha,
            cargo, ativo
        )

        self.id_admin = id_admin
        self.salario = salario
        self.data_admissao = data_admissao

    def desativar_usuario(self, usuario):
        if not self.ativo:
            print("Admin inativo não pode realizar ações.")
            return

        if usuario.ativo:
            usuario.desativar()
            print(f"Usuário {usuario.nome} desativado com sucesso.")
        else:
            print("Usuário já está desativado.")