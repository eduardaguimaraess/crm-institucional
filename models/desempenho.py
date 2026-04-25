from sqlalchemy import Column, Integer, Float, String, ForeignKey
from models.database import Base
from datetime import date

class Desempenho(Base):
    __tablename__ = 'desempenhos'
    
    id_desempenho = Column(Integer, primary_key=True, autoincrement=True)
    
    # Chaves Estrangeiras: ligam o desempenho ao Aluno e à Disciplina
    aluno_id = Column(Integer, ForeignKey('alunos.id_aluno'))
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id_disciplina'))
    
    # No banco, é melhor salvar a nota e o tipo direto na linha
    valor_nota = Column(Float)
    tipo_nota = Column(String) # Ex: "Prova 1", "Trabalho"
    data_registro = Column(String)

    def __init__(self, aluno_id, disciplina_id, valor_nota, tipo_nota, data_registro=None):
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id
        self.valor_nota = valor_nota
        self.tipo_nota = tipo_nota.lower()
        self.data_registro = data_registro or str(date.today())

    # Mantendo a lógica de adicionar, mas adaptada para o banco futuramente
    def adicionar_nota(self, valor: float, tipo: str, data: date = None):
        self.valor_nota = valor
        self.tipo_nota = tipo.lower()
        self.data_registro = str(data or date.today())