from sqlalchemy import Column, Integer, String, Float, Boolean
from models.database import Base

class Curso(Base):
    __tablename__ = 'cursos'
    
    # Mapeando seus atributos para colunas do banco
    # Usamos id_curso como chave primária
    id_curso = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    carga_horaria = Column(Integer)
    valor = Column(Float)
    ativo = Column(Boolean, default=True)

    def __init__(self, nome, carga_horaria, valor, ativo=True):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.valor = valor
        self.ativo = ativo

    # Mantendo sua função original de formatação
    def valor_formatado(self):
        return f"R$ {self.valor:.2f}".replace(".", ",")