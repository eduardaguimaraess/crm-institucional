from services.auth_services import AuthService

class AuthController:
    
    @staticmethod
    def login(cpf, senha, lista_usuarios):
        return AuthService.login(cpf, senha, lista_usuarios)