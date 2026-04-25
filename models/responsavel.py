from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base

class Responsavel(Base):
    __tablename__ = 'responsaveis'
    
    id_responsavel = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    email = Column(String)
    genero = Column(String)
    
    # Chave estrangeira para o endereço
    endereco_id = Column(Integer, ForeignKey('enderecos.id_endereco'))

    def __init__(self, nome, cpf, telefone, email, genero, endereco_id):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.genero = genero
        self.endereco_id = endereco_id
