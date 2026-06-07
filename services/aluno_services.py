from models.aluno import Aluno

class AlunoService:

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Validação matemática real do CPF."""
        cpf_limpo = ''.join(filter(str.isdigit, str(cpf)))
        
        if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
            return False
            
        # Cálculo do 1º dígito
        soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (soma % 11)
        if digito1 > 9:
            digito1 = 0
            
        # Cálculo do 2º dígito
        soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
        digito2 = 11 - (soma % 11)
        if digito2 > 9:
            digito2 = 0
            
        return cpf_limpo[-2:] == f"{digito1}{digito2}"

    @staticmethod
    def cadastrar_aluno(
        id_aluno: int,
        nome: str,
        data_nascimento,
        cpf: str,
        genero: str,
        telefone: str,
        email: str,
        endereco,
        responsavel,
        lista_alunos: list
    ) -> Aluno:

        # 1. NOVA VALIDAÇÃO INTELIGENTE DE CPF
        if not AlunoService.validar_cpf(cpf):
            raise ValueError("CPF inválido! O número digitado não é um CPF real.")

        for aluno in lista_alunos:
            if aluno.cpf == cpf:
                raise ValueError("Aluno já cadastrado com este CPF.")

        aluno = Aluno(
            id_aluno=id_aluno,
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            genero=genero,
            telefone=telefone,
            email=email,
            endereco=endereco,
            responsavel=responsavel,
            status="Ativo"
        )

        # 4. Registrar no sistema
        lista_alunos.append(aluno)

        return aluno
    
    @staticmethod
    def atualizar_aluno(
        id_aluno: int,
        nome: str,
        data_nascimento,
        cpf: str,
        genero: str,
        telefone: str,
        email: str,
        endereco,
        responsavel,
        status: str,
        lista_alunos: list
    ):

        aluno = next(
            (a for a in lista_alunos if a.id_aluno == id_aluno),
            None
        )

        if not aluno:
            raise ValueError("Aluno não encontrado.")

        # VALIDAÇÃO INTELIGENTE NA HORA DE ATUALIZAR TAMBÉM
        if not AlunoService.validar_cpf(cpf):
            raise ValueError("CPF inválido! O número digitado não é um CPF real.")

        for outro in lista_alunos:
            if outro.cpf == cpf and outro.id_aluno != id_aluno:
                raise ValueError("CPF já vinculado a outro aluno.")

        aluno.nome = nome
        aluno.data_nascimento = data_nascimento
        aluno.cpf = cpf
        aluno.genero = genero
        aluno.telefone = telefone
        aluno.email = email
        aluno.endereco = endereco
        aluno.responsavel = responsavel
        aluno.status = status

        return aluno