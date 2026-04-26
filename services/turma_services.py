from models.turma import Turma
from models.curso import Curso
from models.disciplina import Disciplina
# Importa Usuario, pois no sistema o Professor costuma ser um Usuario com cargo específico
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
        lista_turmas: list
    ) -> Turma:
        """
        Realiza as validações e cria uma nova instância de Turma na lista.
        """
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
            status="Ativa"
        )

        # 4. Registrar no sistema
        lista_turmas.append(turma)

        return turma

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
        """
        Localiza uma turma existente por ID e atualiza seus dados na memória.
        O uso de **kwargs permite receber curso/disciplina do controller sem erro.
        """
        # 1. Validações básicas de edição
        if vagas <= 0:
            raise ValueError("O número de vagas deve ser maior que zero.")
        
        if not nome or not nome.strip():
            raise ValueError("O nome da turma não pode estar vazio.")

        # 2. Busca e Atualização
        for turma in lista_turmas:
            if turma.id_turma == id_turma:
                turma.nome = nome
                turma.professor = professor
                turma.horario = horario
                turma.vagas = vagas
                turma.status = status
                return turma
        
        raise ValueError(f"Não foi possível encontrar a turma com ID {id_turma}.")