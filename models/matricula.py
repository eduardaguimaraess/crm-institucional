from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base
from datetime import date

class Matricula(Base):
    __tablename__ = 'matriculas'
    
    id_matricula = Column(Integer, primary_key=True, autoincrement=True)
    
    # Chaves Estrangeiras para ligar Aluno e Turma
    aluno_id = Column(Integer, ForeignKey('alunos.id_aluno'))
    turma_id = Column(Integer, ForeignKey('turmas.id_turma'))
    
    data_matricula = Column(String)
    status = Column(String, default="ativa") # 'ativa', 'cancelada', 'concluída'

    def __init__(self, aluno_id, turma_id, status="ativa"):
        self.aluno_id = aluno_id
        self.turma_id = turma_id
        self.data_matricula = str(date.today())
        self.status = status

    def __str__(self):
        return f"Matricula(aluno_id={self.aluno_id}, turma_id={self.turma_id}, data={self.data_matricula}, status={self.status})"

    # Mantendo suas funções de lógica
    def desativar(self):
        self.status = "cancelada"

    def concluir(self):
        self.status = "concluída"

    def reativar(self):
        self.status = "ativa"