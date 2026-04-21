from services.matricula_services import MatriculaService

class MatriculaController:

    @staticmethod
    def realizar_matricula(aluno, turma):
        return MatriculaService.realizar_matricula(aluno, turma)