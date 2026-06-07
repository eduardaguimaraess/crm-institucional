from models.aluno import Aluno
from models.curso import Curso
from models.disciplina import Disciplina
from models.professor import Professor


class Turma:
    def __init__(
        self,
        id_turma,
        nome,
        curso: Curso,
        disciplina: Disciplina,
        professor: Professor,
        horario,
        vagas: int,
        status="ativa"
    ):
        self.id_turma = id_turma
        self.nome = nome
        self.curso = curso
        self.disciplina = disciplina
        self.professor = professor
        self.horario = horario

        self.vagas = vagas              # vagas disponíveis
        self.status = status            # ativa, encerrada, cancelada
        self.alunos = []                # alunos matriculados

    def possui_aluno(self, aluno: Aluno) -> bool:
        return aluno in self.alunos

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno: Aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
