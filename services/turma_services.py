from models.turma import Turma
from models.curso import Curso
from models.disciplina import Disciplina
from models.professor import Professor


class TurmaService:

    @staticmethod
    def cadastrar_turma(
        id_turma: int,
        nome: str,
        curso: Curso,
        disciplina: Disciplina,
        professor: Professor,
        horario: str,
        vagas: int,
        lista_turmas: list
    ) -> Turma:

        # 1. Validações básicas
        if vagas <= 0:
            raise ValueError("Número de vagas inválido.")

        if not nome:
            raise ValueError("Nome da turma é obrigatório.")

        # 2. Evitar duplicidade (mesma disciplina com mesmo professor)
        for turma in lista_turmas:
            if turma.disciplina == disciplina and turma.professor == professor:
                raise ValueError(
                    "Já existe uma turma desta disciplina com este professor."
                )

        # 3. Criar turma
        turma = Turma(
            id_turma=id_turma,
            nome=nome,
            curso=curso,
            disciplina=disciplina,
            professor=professor,
            horario=horario,
            vagas=vagas,
            status="ativa"
        )

        # 4. Registrar no sistema
        lista_turmas.append(turma)

        return turma
