from services.curso_services import CursoService
from data import csv_repository

class CursoController:

    @staticmethod
    def cadastrar_curso(dados: dict, lista_cursos: list):
        """
        Cadastra um curso via Service e persiste a lista atualizada no arquivo físico.
        """
        resultado = CursoService.cadastrar_curso(
            **dados,
            lista_cursos=lista_cursos
        )
        
        # Persistência Física: Salva a lista de cursos no arquivo cursos.csv
        csv_repository.salvar_cursos(lista_cursos)
        
        return resultado
        
    @staticmethod
    def atualizar_curso(dados: dict, lista_cursos: list):
        """
        Atualiza um curso via Service e sincroniza a alteração no arquivo físico.
        """
        resultado = CursoService.atualizar_curso(
            **dados,
            lista_cursos=lista_cursos
        )
        
        # Persistência Física: Sobrescreve o CSV com os dados atualizados
        csv_repository.salvar_cursos(lista_cursos)
        
        return resultado

    @staticmethod
    def listar_cursos(lista_cursos: list):
        """
        Retorna a listagem de cursos em memória.
        """
        return lista_cursos