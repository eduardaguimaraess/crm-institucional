from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base

class Turma(Base):
    __tablename__ = 'turmas'
    
    id_turma = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    
    # Chaves Estrangeiras para as conexões
    curso_id = Column(Integer, ForeignKey('cursos.id_curso'))
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id_disciplina'))
    professor_id = Column(Integer, ForeignKey('professores.id_professor'))
    
    horario = Column(String)
    vagas = Column(Integer)
    status = Column(String, default="ativa") # ativa, encerrada, cancelada

    def __init__(self, nome, curso_id, disciplina_id, professor_id, horario, vagas, status="ativa"):
        self.nome = nome
        self.curso_id = curso_id
        self.disciplina_id = disciplina_id
        self.professor_id = professor_id
        self.horario = horario
        self.vagas = vagas
        self.status = status

    # Mantendo suas funções de lógica (mesmo que agora o banco controle as matrículas)
    def adicionar_aluno(self, aluno_id):
        pass
