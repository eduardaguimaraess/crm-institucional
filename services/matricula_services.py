from datetime import date
from models.matricula import Matricula
from models.aluno import Aluno
from models.turma import Turma


class MatriculaService:

    @staticmethod
    def realizar_matricula(aluno: Aluno, turma: Turma) -> Matricula:

        # 1. Aluno precisa estar ativo
        if aluno.status.lower() != "ativo":
            raise ValueError("Aluno não está ativo.")

        # 2. Turma precisa estar ativa
        if turma.status != "ativa":
            raise ValueError("Turma não está ativa.")

        # 3. Precisa haver vaga
        if turma.vagas <= 0:
            raise ValueError("Não há vagas disponíveis.")

        # 4. Verificar duplicidade
        if turma.possui_aluno(aluno):
            raise ValueError("Aluno já matriculado.")

        # 5. Criar matrícula
        matricula = Matricula(aluno=aluno, turma=turma)

        # 6. Atualizar estado
        turma.vagas -= 1
        turma.adicionar_aluno(aluno)

        return matricula
