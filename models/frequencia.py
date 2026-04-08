from datetime import date
from disciplina import Disciplina
from turma import Turma
from aluno import Aluno 

class Frequencia:
    """
    Inicialmente, o aluno é marcado como presente; o professor pode alterar para falta.
    """
    def __init__(self, turma: Turma, disciplina: Disciplina, data: date, presente: bool = True):
        self.turma = turma
        self.disciplina = disciplina
        self.data = data
        self.presente = presente  # True = presente, False = falta

    def marcar_falta(self):
        self.presente = False

# Extendendo a classe Aluno existente com métodos de frequência
def adicionar_frequencia(self, turma: Turma, disciplina: Disciplina, data: date = None):
    data = data or date.today()
    freq = Frequencia(turma, disciplina, data)
    if not hasattr(self, "frequencias"):
        self.frequencias = {}  # cria atributo se ainda não existir
    if disciplina not in self.frequencias:
        self.frequencias[disciplina] = []
    self.frequencias[disciplina].append(freq)
    return freq

def total_aulas(self, disciplina: Disciplina):
    if not hasattr(self, "frequencias") or disciplina not in self.frequencias:
        return 0
    return len(self.frequencias[disciplina])

def total_presencas(self, disciplina: Disciplina):
    if not hasattr(self, "frequencias") or disciplina not in self.frequencias:
        return 0
    return len([f for f in self.frequencias[disciplina] if f.presente])

def percentual_presenca(self, disciplina: Disciplina):
    total = self.total_aulas(disciplina)
    if total == 0:
        return 0.0
    return (self.total_presencas(disciplina) / total) * 100

# Adicionando os métodos dinamicamente à classe Aluno existente
Aluno.adicionar_frequencia = adicionar_frequencia
Aluno.total_aulas = total_aulas
Aluno.total_presencas = total_presencas
Aluno.percentual_presenca = percentual_presenca