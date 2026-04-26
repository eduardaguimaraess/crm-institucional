from services.aluno_services import AlunoService
from data import csv_repository

class AlunoController:

    @staticmethod
    def cadastrar_aluno(dados: dict, lista_alunos: list):
        """
        Cadastra um aluno via Service e persiste a lista atualizada no CSV.
        """
        # Executa a lógica de negócio
        resultado = AlunoService.cadastrar_aluno(
            **dados,
            lista_alunos=lista_alunos
        )
        
        # Persistência Física: Salva a lista completa no arquivo alunos.csv
        csv_repository.salvar_alunos(lista_alunos)
        
        return resultado

    @staticmethod
    def atualizar_aluno(dados: dict, lista_alunos: list):
        """
        Atualiza os dados de um aluno e sincroniza a alteração no arquivo físico.
        """
        # Executa a atualização na memória
        resultado = AlunoService.atualizar_aluno(
            **dados,
            lista_alunos=lista_alunos
        )
        
        # Persistência Física: Sobrescreve o CSV com os dados atualizados
        csv_repository.salvar_alunos(lista_alunos)
        
        return resultado
        
    @staticmethod
    def listar_alunos(lista_alunos: list):
        """
        Retorna a listagem de alunos (conforme estrutura original).
        """
        return lista_alunos