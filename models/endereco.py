from sqlalchemy import Column, Integer, String
from models.database import Base
import requests

class Endereco(Base):
    __tablename__ = 'enderecos'
    
    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    cep = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    complemento = Column(String)
    cidade = Column(String)
    estado = Column(String)

    def __init__(self, cep, logradouro, numero, bairro, complemento=None):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.cidade = ""
        self.estado = ""
        
        # Chama a função para preencher cidade e estado antes de salvar
        self.buscar_cep()

    def buscar_cep(self):
        try:
            url = f"https://viacep.com.br/ws/{self.cep}/json/"
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                self.cidade = dados.get("localidade", "")
                self.estado = dados.get("uf", "")
        except Exception as e:
            print("Erro na conexão ViaCEP:", e)