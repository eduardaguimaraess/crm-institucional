from models.usuario import Usuario

class AuthService:

    @staticmethod
    def login(cpf: str, senha: str, usuarios: list[Usuario]) -> Usuario:
        """
        Realiza a lógica de busca e autenticação garantindo CPF de 11 dígitos.
        """
        # 1. Extrai apenas os números do que o usuário digitou
        cpf_digitado = ''.join(filter(str.isdigit, cpf))

        # 2. Validação rigorosa de tamanho
        if len(cpf_digitado) != 11:
            raise ValueError("O CPF deve conter exatamente 11 números.")

        for usuario in usuarios:
            # 3. Limpa o CPF que veio do banco/CSV para garantir a comparação "número com número"
            # Isso evita erros se o CSV tiver guardado pontos ou traços por acidente
            u_cpf_banco = ''.join(filter(str.isdigit, usuario.cpf))
            
            if u_cpf_banco == cpf_digitado:
                # 4. Chama o método de autenticação da Model
                # Passamos o cpf_digitado (limpo) e a senha
                if usuario.autenticar(cpf_digitado, senha):
                    return usuario

        # Se percorreu toda a lista e não encontrou ou a senha errou
        raise ValueError("CPF ou senha inválidos.")