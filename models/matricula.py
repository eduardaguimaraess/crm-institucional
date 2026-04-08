from aluno import Aluno
from turma import Turma
from datetime import date

class Matricula:
    def __init__(self, aluno, turma, status: str = "ativa"):
        self.aluno = aluno          
        self.turma = turma          
        self.data_matricula = date.today()  # sempre pega a data de hoje automaticamente
        self.status = status        # 'ativa', 'desativada', 'concluída'

    def __str__(self):
        return f"Matricula(aluno={self.aluno.nome}, turma={self.turma.nome}, data={self.data_matricula}, status={self.status})"

    def desativar(self):
        self.status = "cancelada"

    def concluir(self):
        self.status = "concluída"

    def reativar(self):
        self.status = "ativa"