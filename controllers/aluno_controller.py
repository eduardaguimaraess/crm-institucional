from services.aluno_services import AlunoService


class AlunoController:

    @staticmethod
    def cadastrar_aluno(dados: dict, lista_alunos: list):
        
        return AlunoService.cadastrar_aluno(
            **dados,
            lista_alunos=lista_alunos
        )

    @staticmethod
    def atualizar_aluno(dados: dict, lista_alunos: list):
        return AlunoService.atualizar_aluno(
            **dados,
            lista_alunos=lista_alunos
        )
        
    @staticmethod
    def listar_alunos(lista_alunos: list):
        
        return lista_alunos


