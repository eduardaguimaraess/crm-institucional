from models.turma import Turma
from models.curso import Curso
from models.disciplina import Disciplina
from models.usuario import Usuario 

class TurmaService:

    @staticmethod
    def cadastrar_turma(
        id_turma: int,
        nome: str,
        curso: Curso,
        disciplina: Disciplina,
        professor: Usuario,
        horario: str,
        vagas: int,
        lista_turmas: list,
        status: str = "Ativa"  # <--- ADICIONAMOS ISSO AQUI
    ) -> Turma:
        
        if vagas <= 0:
            raise ValueError("Número de vagas inválido.")

        if not nome:
            raise ValueError("Nome da turma é obrigatório.")

        for turma in lista_turmas:
            if turma.disciplina == disciplina and turma.professor == professor:
                raise ValueError("Já existe uma turma desta disciplina com este professor.")

        # Agora usamos o status que veio do parâmetro
        turma = Turma(
            id_turma=id_turma,
            nome=nome,
            curso=curso,
            disciplina=disciplina,
            professor=professor,
            horario=horario,
            vagas=vagas,
            status=status 
        )

        lista_turmas.append(turma)
        return turma

    # O atualizar_turma já estava certo, pois usava **kwargs ou recebia o status
    @staticmethod
    def atualizar_turma(
        id_turma: int,
        nome: str,
        professor: Usuario,
        horario: str,
        vagas: int,
        status: str,
        lista_turmas: list,
        **kwargs
    ) -> Turma:
        if vagas <= 0:
            raise ValueError("O número de vagas deve ser maior que zero.")
        
        if not nome or not nome.strip():
            raise ValueError("O nome da turma não pode estar vazio.")

        for turma in lista_turmas:
            if turma.id_turma == id_turma:
                turma.nome = nome
                turma.professor = professor
                turma.horario = horario
                turma.vagas = vagas
                turma.status = status
                return turma
        
        raise ValueError(f"Não foi possível encontrar a turma com ID {id_turma}.")