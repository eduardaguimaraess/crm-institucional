from models.curso import Curso

class CursoService:

    @staticmethod
    def cadastrar_curso(
        id_curso,
        nome,
        carga_horaria,
        valor,
        lista_cursos
    ) -> Curso:

        # regra simples: evitar nome duplicado
        for curso in lista_cursos:
            if curso.nome.lower() == nome.lower():
                raise ValueError("Curso já cadastrado.")

        # validações básicas
        if carga_horaria <= 0:
            raise ValueError("Carga horária inválida.")

        if valor <= 0:
            raise ValueError("Valor inválido.")

        curso = Curso(
            id_curso=id_curso,
            nome=nome,
            carga_horaria=carga_horaria,
            valor=valor
        )

        lista_cursos.append(curso)
        return curso