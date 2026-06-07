# models/desempenho.py

from datetime import date
from models.aluno import Aluno
from models.disciplina import Disciplina


class Desempenho:

    def __init__(self, aluno: Aluno, disciplina: Disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.notas = []  # lista de dicionários

    def adicionar_nota(self, valor: float, tipo: str, data: date = None):
        
        self.notas.append({
            "valor": valor,
            "tipo": tipo.lower(),
            "data": data or date.today()
        })