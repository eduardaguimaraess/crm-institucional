from services.curso_services import CursoService


class CursoController:

    @staticmethod
    def cadastrar_curso(dados: dict, lista_cursos: list):

        return CursoService.cadastrar_curso(
            **dados,
            lista_cursos=lista_cursos
        )