# services/matricula.py

from datetime import date

from models.matricula import Matricula
from models.aluno import Aluno
from models.turma import Turma


class MatriculaService:
    """
    Serviço responsável por realizar operações relacionadas à matrícula.
    Atua como a 'secretaria' do sistema.
    """

    @staticmethod
    def realizar_matricula(aluno: Aluno, turma: Turma) -> Matricula:
        """
        Realiza a matrícula de um aluno em uma turma, aplicando
        todas as regras de negócio necessárias.
        """

        # 1. Verificar se o aluno está ativo
        if aluno.status != "ativo":
            raise ValueError("Aluno não está ativo e não pode ser matriculado.")

        # 2. Verificar se a turma está ativa
        if turma.status != "ativa":
            raise ValueError("Turma não está ativa.")

        # 3. Verificar se há vagas disponíveis
        if turma.vagas <= 0:
            raise ValueError("Não há vagas disponíveis nesta turma.")

        # 4. (Opcional) Verificar se o aluno já está matriculado
        if turma.possui_aluno(aluno):
            raise ValueError("Aluno já está matriculado nesta turma.")

        # 5. Criar a matrícula
        matricula = Matricula(
            aluno=aluno,
            turma=turma,
            data_matricula=date.today(),
            status="ativa"
        )

        # 6. Atualizar a turma
        turma.vagas -= 1
        turma.adicionar_aluno(aluno)

        return matricula