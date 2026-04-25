from sqlalchemy import Column, Integer, String, Float
from models.database import Base

class Professor(Base):
    __tablename__ = 'professores'
    
    # Colunas vindas da "base" de Usuário
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_nascimento = Column(String)
    cpf = Column(String, unique=True)
    genero = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String)
    
    # Colunas específicas do Professor
    id_professor = Column(String) # Matrícula funcional
    salario = Column(Float)
    data_admissao = Column(String)
    cargo = Column(String, default="professor")
    ativo = Column(String, default="True")

    def __init__(self, nome, data_nascimento, cpf, genero, telefone, email, senha,
                 id_professor, salario, data_admissao, cargo="professor", ativo="True"):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.id_professor = id_professor
        self.salario = salario
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.ativo = ativo
