from services.matricula_services import MatriculaService

class MatriculaController:

    @staticmethod
    def realizar_matricula(aluno, turma):
        return MatriculaService.realizar_matricula(aluno, turma)
    
    @staticmethod
    def atualizar_matricula(dados: dict, lista_matriculas: list):
        
        return MatriculaService.atualizar_matricula(
            **dados,
            lista_matriculas=lista_matriculas
        )