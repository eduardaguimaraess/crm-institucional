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