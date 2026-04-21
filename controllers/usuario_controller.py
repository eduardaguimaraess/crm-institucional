from services.usuario_cadastro import UsuarioCadastroService

class UsuarioController:

    @staticmethod
    def cadastrar_usuario(dados, lista_usuarios):
        return UsuarioCadastroService.cadastrar_usuario(
            **dados,
            lista_usuarios=lista_usuarios
        )

