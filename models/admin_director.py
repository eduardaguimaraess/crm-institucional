from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.database import Base

class Admin(Base):
    __tablename__ = 'admins'
    
    # O id_usuario vem da tabela Usuario (Herança no banco)
    id_admin = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    email = Column(String)
    salario = Column(Float)
    data_admissao = Column(String)
    cargo = Column(String, default="admin_diretor")
    status_ativo = Column(String, default="True")

    def __init__(self, nome, cpf, email, salario, data_admissao, cargo="admin_diretor"):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.salario = salario
        self.data_admissao = data_admissao
        self.cargo = cargo