from services.disciplina_services import DisciplinaService
from data import csv_repository

class DisciplinaController:
    
    @staticmethod
    def cadastrar_disciplina(dados: dict, lista_disciplinas: list):
        """
        Cadastra uma disciplina via Service e persiste a lista no CSV.
        """
        resultado = DisciplinaService.cadastrar_disciplina(
            **dados,
            lista_disciplinas=lista_disciplinas
        )
        
        # Persistência Física: Atualiza o arquivo disciplinas.csv
        csv_repository.salvar_disciplinas(lista_disciplinas)
        
        return resultado

    @staticmethod
    def atualizar_disciplina(dados: dict, lista_disciplinas: list):
        """
        Atualiza uma disciplina existente e sincroniza com o arquivo CSV.
        """
        resultado = DisciplinaService.atualizar_disciplina(
            **dados,
            lista_disciplinas=lista_disciplinas
        )
        
        # Persistência Física: Atualiza o arquivo disciplinas.csv
        csv_repository.salvar_disciplinas(lista_disciplinas)
        
        return resultado