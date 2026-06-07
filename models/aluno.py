from datetime import date
from models.endereco import Endereco

# Classe Aluno
class Aluno:

    def __init__(self, id_aluno, nome, data_nascimento, cpf,
                 genero, telefone, email, endereco, responsavel=None, status="ativo"): 

        # --- 1. LIMPEZA E VALIDAÇÃO DE DADOS ---

        # CPF apenas números
        cpf_limpo = str(cpf).replace(".", "").replace("-", "").strip()
        if not cpf_limpo.isdigit():
            raise ValueError("Erro: O CPF deve conter apenas números.")

        # Telefone com limite de 15 caracteres
        tel_limpo = str(telefone).replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()
        if len(tel_limpo) > 15:
            raise ValueError("Erro: O telefone não pode ter mais de 15 dígitos.")

        # --- 2. LÓGICA DE MAIORIDADE (RESPONSÁVEL) ---

        # Calcula a idade atual
        hoje = date.today()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

        if idade < 18:
            # Se for menor, o campo responsável NÃO pode ser vazio nem ser "O próprio"
            if not responsavel or str(responsavel).strip() == "" or str(responsavel).lower() == "o próprio":
                raise ValueError(f"Erro: Aluno menor de idade ({idade} anos) exige um responsável cadastrado.")
            self.responsavel = responsavel
        else:
            # Se for maior de idade e o campo vier vazio, definimos como "O próprio"
            if not responsavel or str(responsavel).strip() == "":
                self.responsavel = "O próprio"
            else:
                self.responsavel = responsavel

        # --- 3. ATRIBUIÇÃO DOS ATRIBUTOS ---
        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf_limpo          
        self.genero = genero
        self.telefone = tel_limpo 
        self.email = email
        self.endereco = endereco
        self.status = "Ativo"