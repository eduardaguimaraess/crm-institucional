from models.disciplina import Disciplina
from models.curso import Curso
from models.professor import Professor


class DisciplinaService:


    @staticmethod
    def cadastrar_disciplina(
        id_disciplina: int,
        nome: str,
        curso: Curso,
        professor: Professor,
        carga_horaria: int,
        dia_semana: str,
        hora_inicio: str,
        hora_fim: str,
        lista_disciplinas: list
    ) -> Disciplina:

        if not nome:
            raise ValueError("Nome da disciplina é obrigatório.")

        if carga_horaria <= 0:
            raise ValueError("Carga horária inválida.")

        for d in lista_disciplinas:
            if d.nome.lower() == nome.lower() and d.curso == curso:
                raise ValueError("Disciplina já cadastrada para este curso.")

        disciplina = Disciplina(
            id_disciplina=id_disciplina,
            nome=nome,
            curso=curso,
            professor=professor,
            carga_horaria=carga_horaria,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim,
            ativa=True
        )
        
        lista_disciplinas.append(disciplina)

        return disciplina
    
    @staticmethod
    def atualizar_disciplina(
        id_disciplina: int,
        nome: str,
        curso,
        professor,
        carga_horaria: int,
        dia_semana: str,
        hora_inicio: str,
        hora_fim: str,
        ativa: bool,
        lista_disciplinas: list
    ):

        # 1. Localizar disciplina
        disciplina = next(
            (d for d in lista_disciplinas if d.id_disciplina == id_disciplina),
            None
        )

        if not disciplina:
            raise ValueError("Disciplina não encontrada.")

        # 2. Evitar duplicidade no mesmo curso (se mudou)
        for outra in lista_disciplinas:
            if (
                outra.nome.lower() == nome.lower()
                and outra.curso == curso
                and outra.id_disciplina != id_disciplina
            ):
                raise ValueError("Já existe outra disciplina com este nome neste curso.")

        # 3. Atualizar dados
        disciplina.nome = nome
        disciplina.curso = curso
        disciplina.professor = professor
        disciplina.carga_horaria = carga_horaria
        disciplina.dia_semana = dia_semana
        disciplina.hora_inicio = hora_inicio
        disciplina.hora_fim = hora_fim
        disciplina.ativa = ativa

        return disciplina