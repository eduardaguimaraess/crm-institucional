# services/usuario_cadastro.py

from models.usuario import Usuario


class UsuarioCadastroService:

    @staticmethod
    def cadastrar_usuario(
        id_usuario: int,
        nome: str,
        data_nascimento,
        cpf: str,
        genero: str,
        telefone: str,
        email: str,
        senha: str,
        endereco,
        cargo: str,
        lista_usuarios: list
    ) -> Usuario:

        # 1. Validar CPF (simples, mas suficiente para o escopo)
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")

        # 2. Evitar CPF duplicado
        for usuario in lista_usuarios:
            if usuario.cpf == cpf:
                raise ValueError("Já existe um usuário cadastrado com este CPF.")

        # 3. Validar senha mínima
        if len(senha) < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres.")

        # 4. Criar usuário
        usuario = Usuario(
            id_usuario=id_usuario,
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            genero=genero,
            telefone=telefone,
            email=email,
            senha=senha,
            endereco=endereco,
            cargo=cargo,
            ativo=True
        )

        # 5. Registrar no sistema
        lista_usuarios.append(usuario)

        return usuario