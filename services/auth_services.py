from models.usuario import Usuario

class AuthService:

    @staticmethod
    def login(cpf: str, senha: str, usuarios: list[Usuario]) -> Usuario:
        """
        Realiza o login no sistema.
        Retorna o usuário autenticado ou lança erro.
        """

        for usuario in usuarios:
            if usuario.autenticar(cpf, senha):
                return usuario

        raise ValueError("CPF ou senha inválidos, ou usuário inativo.")