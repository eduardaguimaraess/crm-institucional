from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models.database import Base

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    
    id_disciplina = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    
    # Chaves Estrangeiras para ligar com Curso e Professor
    curso_id = Column(Integer, ForeignKey('cursos.id_curso'))
    professor_id = Column(Integer, ForeignKey('professores.id_professor'))
    
    carga_horaria = Column(Integer)
    dia_semana = Column(String)
    hora_inicio = Column(String)
    hora_fim = Column(String)
    ativa = Column(Boolean, default=True)

    def __init__(self, nome, curso_id, professor_id, carga_horaria, dia_semana, hora_inicio, hora_fim, ativa=True):
        self.nome = nome
        self.curso_id = curso_id
        self.professor_id = professor_id
        self.carga_horaria = carga_horaria
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.ativa = ativa

    # Mantendo sua função de horário
    def horario_formatado(self):
        return f"{self.dia_semana} {self.hora_inicio} - {self.hora_fim}"