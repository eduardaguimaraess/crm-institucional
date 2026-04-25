from datetime import date
from models.aluno import Aluno
from models.turma import Turma
from models.disciplina import Disciplina

class Frequencia:

    def __init__(
        self,
        aluno: Aluno,
        turma: Turma,
        disciplina: Disciplina,
        data: date,
        presente: bool = True
    ):
        self.aluno = aluno
        self.turma = turma
        self.disciplina = disciplina
        self.data = data
        self.presente = presente

    def marcar_falta(self):
        self.presente = False


from datetime import date
