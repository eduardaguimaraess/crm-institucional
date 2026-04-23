from models.aluno import Aluno


class AlunoService:

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

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF do aluno inválido.")

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

    
