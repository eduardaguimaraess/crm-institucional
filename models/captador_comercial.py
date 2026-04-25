from sqlalchemy import Column, Integer, String, Float
from models.database import Base

class CaptadorComercial(Base):
    __tablename__ = 'captadores_comerciais'
    
    # Colunas que o banco de dados vai criar
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_nascimento = Column(String)
    cpf = Column(String, unique=True)
    genero = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String)
    
    id_captador = Column(String) # Identificador funcional
    salario = Column(Float)
    data_admissao = Column(String)
    cargo = Column(String, default="captador_comercial")
    ativo = Column(String, default="True")

    def __init__(self, nome, data_nascimento, cpf, genero, telefone, email, senha, 
                 id_captador, salario, data_admissao, cargo="captador_comercial", ativo="True"):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.id_captador = id_captador
        self.salario = salario
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.ativo = ativo
    
    def limpar_cpf(self, cpf):
        return cpf.replace(".", "").replace("-", "")