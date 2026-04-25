from sqlalchemy import Column, Integer, String
from models.database import Base

# Agora a classe Aluno "herda" do Base, para o banco saber que ela existe
class Aluno(Base):
    __tablename__ = 'alunos' # Nome da tabela no banco
    
    # Aqui definimos as colunas que vão existir na sua "gaveta"
    id_aluno = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_nascimento = Column(String)
    cpf = Column(String, unique=True)
    genero = Column(String)
    telefone = Column(String)
    email = Column(String)
    status = Column(String, default="Ativo")

    # O __init__ continua parecido, mas agora o SQLAlchemy ajuda a gerenciar
    def __init__(self, nome, data_nascimento, cpf, genero, telefone, email, status="Ativo"):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.status = status