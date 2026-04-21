from services.frequencia_services import FrequenciaService


class FrequenciaController:

    @staticmethod
    def registrar_presenca(aluno, turma, disciplina):
        return FrequenciaService.registrar_presenca(
            aluno, turma, disciplina
        )