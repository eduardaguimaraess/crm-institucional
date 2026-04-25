from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models.database import Base
from datetime import date

class Frequencia(Base):
    __tablename__ = 'frequencias'
    
    id_frequencia = Column(Integer, primary_key=True, autoincrement=True)
    
    # Chaves Estrangeiras para ligar com as outras tabelas
    aluno_id = Column(Integer, ForeignKey('alunos.id_aluno'))
    turma_id = Column(Integer, ForeignKey('turmas.id_turma'))
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id_disciplina'))
    
    data = Column(String) # Guardamos como string para evitar erro de formato
    presente = Column(Boolean, default=True)

    def __init__(self, aluno_id, turma_id, disciplina_id, data=None, presente=True):
        self.aluno_id = aluno_id
        self.turma_id = turma_id
        self.disciplina_id = disciplina_id
        self.data = str(data or date.today())
        self.presente = presente

    # Mantendo sua função original
    def marcar_falta(self):
        self.presente = False
