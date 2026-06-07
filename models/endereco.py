import requests

# Classe Endereco
class Endereco:

    def __init__(self, id_endereco, cep, logradouro, numero, bairro, complemento=None):
        self.id_endereco = id_endereco
        self.cep = cep
        self.logradouro = logradouro  # digitado pela pessoa
        self.numero = numero          # digitado pela pessoa
        self.bairro = bairro          # digitado pela pessoa
        self.complemento = complemento

        # Preenchidos automaticamente
        self.cidade = ""
        self.estado = ""

        # Busca dados do CEP
        self.buscar_cep()

    # Busca cidade e estado pelo CEP
    def buscar_cep(self):
        try:
            url = f"https://viacep.com.br/ws/{self.cep}/json/"
            resposta = requests.get(url)

            if resposta.status_code == 200:
                dados = resposta.json()

                self.cidade = dados.get("localidade", "")
                self.estado = dados.get("uf", "")

            else:
                print("Erro ao buscar CEP.")

        except Exception as e:
            print("Erro na conexão:", e)