from services.turma_services import TurmaService
from data import csv_repository

class TurmaController:

    @staticmethod
    def cadastrar_turma(dados: dict, lista_turmas: list):
        """
        Cadastra uma turma via Service e persiste a lista no CSV.
        """
        resultado = TurmaService.cadastrar_turma(
            **dados,
            lista_turmas=lista_turmas
        )
        
        # Persistência Física: Atualiza o arquivo turmas.csv
        csv_repository.salvar_turmas(lista_turmas)
        
        return resultado

    @staticmethod
    def atualizar_turma(dados: dict, lista_turmas: list):
        """
        Atualiza os dados de uma turma via Service e sincroniza com o CSV.
        """
        # Chama o Service para realizar a alteração lógica no objeto dentro da lista
        resultado = TurmaService.atualizar_turma(
            **dados,
            lista_turmas=lista_turmas
        )
        
        # Persistência Física: Sobrescreve o CSV com a lista atualizada
        csv_repository.salvar_turmas(lista_turmas)
        
        return resultado
    
    @staticmethod
    def listar_turmas(lista_turmas: list):
        """
        Retorna a listagem de turmas em memória.
        """
        return lista_turmas