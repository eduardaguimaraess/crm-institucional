from services.turma_services import TurmaService

class TurmaController:

    @staticmethod
    def cadastrar_turma(dados: dict, lista_turmas: list):

        return TurmaService.cadastrar_turma(
            **dados,
            lista_turmas=lista_turmas
        )
    
    @staticmethod
    def listar_turmas(lista_turmas: list):
        
        return lista_turmas
