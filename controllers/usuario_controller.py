from models.usuario import Usuario
from data.csv_repository import salvar_usuarios

class UsuarioController:
    @staticmethod
    def cadastrar_usuario(dados: dict, lista_usuarios: list):
        # Validação simples de e-mail duplicado
        if any(u.email == dados['email'] for u in lista_usuarios):
            raise ValueError("E-mail já cadastrado.")
        
        # Criar instância do modelo
        novo_usuario = Usuario(
            id_usuario=dados['id_usuario'],
            nome=dados['nome'],
            cpf=dados['cpf'],
            email=dados['email'],
            senha=dados['senha'],
            data_nascimento=dados['data_nascimento'],
            genero=dados['genero'],
            telefone=dados['telefone'],
            cargo=dados['cargo'],
            endereco=dados['endereco']
        )
        
        # Atualiza memória e persiste no disco
        lista_usuarios.append(novo_usuario)
        salvar_usuarios(lista_usuarios)
        return novo_usuario