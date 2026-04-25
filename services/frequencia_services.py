from datetime import date
from models.frequencia import Frequencia
from models.aluno import Aluno
from models.disciplina import Disciplina
from models.turma import Turma


class FrequenciaService:

    @staticmethod
    def registrar_presenca(
        aluno: Aluno,
        turma: Turma,
        disciplina: Disciplina,
        data: date = None
    ) -> Frequencia:

        data = data or date.today()

        # garante lista de frequências no aluno
        if not hasattr(aluno, "frequencias"):
            aluno.frequencias = []

        frequencia = Frequencia(
            aluno=aluno,
            turma=turma,
            disciplina=disciplina,
            data=data,
            presente=True
        )

        aluno.frequencias.append(frequencia)
        return frequencia

    @staticmethod
    def registrar_falta(
        aluno: Aluno,
        turma: Turma,
        disciplina: Disciplina,
        data: date = None
    ) -> Frequencia:

        frequencia = FrequenciaService.registrar_presenca(
            aluno, turma, disciplina, data
        )
        frequencia.marcar_falta()
        return frequencia

    @staticmethod
    def calcular_percentual(
        aluno: Aluno,
        disciplina: Disciplina
    ) -> float:

        if not hasattr(aluno, "frequencias"):
            return 0.0

        registros = [
            f for f in aluno.frequencias
            if f.disciplina == disciplina
        ]

        if not registros:
            return 0.0

        presencas = [f for f in registros if f.presente]
        return (len(presencas) / len(registros)) * 100