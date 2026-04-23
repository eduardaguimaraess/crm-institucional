# controllers/disciplina_controller.py

from services.disciplina_services import DisciplinaService

class DisciplinaController:
    
    @staticmethod
    def cadastrar_disciplina(dados: dict, lista_disciplinas: list):

        return DisciplinaService.cadastrar_disciplina(
            **dados,
            lista_disciplinas=lista_disciplinas
        )
