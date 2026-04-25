from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_nascimento = Column(String)
    cpf = Column(String, unique=True)
    genero = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String)
    cargo = Column(String) # admin_diretor, professor, captador_comercial, etc.
    ativo = Column(Boolean, default=True)
    
    # Chave estrangeira para o endereço
    endereco_id = Column(Integer, ForeignKey('enderecos.id_endereco'))

    def __init__(self, nome, data_nascimento, cpf, genero, telefone, email, senha, endereco_id, cargo, ativo=True):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.endereco_id = endereco_id
        self.cargo = cargo
        self.ativo = ativo

    def autenticar(self, cpf, senha):
        if not self.ativo:
            return False
        return self.cpf == cpf and self.senha == senha

    def alterarSenha(self, nova_senha):
        self.senha = nova_senha

    def desativar(self):
        self.ativo = False