# services/desempenho.py

from datetime import date
from statistics import mean

from models.desempenho import Desempenho
from models.aluno import Aluno
from models.disciplina import Disciplina
from models.turma import Turma


class DesempenhoService:
    """
    Serviço responsável pelo controle de notas e desempenho acadêmico.
    Atua como o 'setor pedagógico' do sistema.
    """

    @staticmethod
    def registrar_nota(
        aluno: Aluno,
        disciplina: Disciplina,
        turma: Turma,
        nota: float,
        tipo: str
    ) -> Desempenho:
        """
        Registra uma nota para um aluno em uma disciplina.
        """

        # 1. Verificar se o aluno está matriculado na turma
        if not turma.possui_aluno(aluno):
            raise ValueError("Aluno não está matriculado nesta turma.")

        # 2. Validar a nota
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")

        # 3. Criar o registro de desempenho
        desempenho = Desempenho(
            aluno=aluno,
            disciplina=disciplina,
            nota=nota,
            tipo=tipo,
            data=date.today()
        )

        # 4. Associar o desempenho ao aluno (histórico)
        aluno.adicionar_desempenho(desempenho)

        return desempenho

    @staticmethod
    def calcular_media(aluno: Aluno, disciplina: Disciplina) -> float:
        """
        Calcula a média de um aluno em uma disciplina específica.
        """

        notas = [
            d.nota for d in aluno.desempenhos
            if d.disciplina == disciplina
        ]

        if not notas:
            raise ValueError("Não há notas registradas para esta disciplina.")

        return mean(notas)

    @staticmethod
    def listar_notas(aluno: Aluno, disciplina: Disciplina):
        """
        Retorna todas as notas de um aluno em uma disciplina.
        """

        return [
            d for d in aluno.desempenhos
            if d.disciplina == disciplina
        ]