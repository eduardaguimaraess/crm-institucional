from services.matricula_services import MatriculaService
from data import csv_repository

class MatriculaController:

    @staticmethod
    def realizar_matricula(dados: dict, lista_matriculas: list):
        """
        Realiza a matrícula de um aluno via Service e persiste no CSV.
        """
        # Chama o Service para criar o objeto e validar as regras de negócio
        resultado = MatriculaService.realizar_matricula(
            **dados,
            lista_matriculas=lista_matriculas
        )
        
        # Persistência Física: Salva a lista atualizada no arquivo matriculas.csv
        csv_repository.salvar_matriculas(lista_matriculas)
        
        return resultado
    
    @staticmethod
    def atualizar_matricula(dados: dict, lista_matriculas: list):
        """
        Atualiza os dados de uma matrícula existente (como status) e sincroniza com o CSV.
        """
        # Chama o Service para localizar e alterar o objeto na memória
        resultado = MatriculaService.atualizar_matricula(
            **dados,
            lista_matriculas=lista_matriculas
        )
        
        # Persistência Física: Sobrescreve o CSV com a lista atualizada
        csv_repository.salvar_matriculas(lista_matriculas)
        
        return resultado

    @staticmethod
    def listar_matriculas(lista_matriculas: list):
        """
        Retorna a listagem de matrículas em memória.
        """
        return lista_matriculas