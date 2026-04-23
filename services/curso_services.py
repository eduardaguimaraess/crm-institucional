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
    
    @staticmethod
    def atualizar_curso(id_curso, nome: str, carga_horaria: int, valor: float, ativo: bool, lista_cursos: list):

        # 1. Localizar o curso
        curso = next(
            (c for c in lista_cursos if c.id_curso == id_curso),
            None
        )

        if not curso:
            raise ValueError("Curso não encontrado.")

        # 2. Evitar duplicidade
        for outro in lista_cursos:
            if outro.nome.lower() == nome.lower() and outro.id_curso != id_curso:
                raise ValueError("Já existe outro curso com este nome.")

        # 3. Atualizar dados
        curso.nome = nome
        curso.carga_horaria = carga_horaria
        curso.valor = valor
        curso.ativo = ativo

        return curso