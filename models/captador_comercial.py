from models.usuario import Usuario

# Classe responsável por captar novos alunos e responsáveis
class CaptadorComercial(Usuario):

    def __init__(self, id_usuario, nome, data_nascimento, cpf, genero,
                 telefone, email, senha,
                 id_captador, salario, data_admissao,
                 cargo="captador_comercial", ativo=True):

        super().__init__(
            id_usuario, nome, data_nascimento, cpf,
            genero, telefone, email, senha,
            cargo, ativo
        )

        self.id_captador = id_captador
        self.salario = salario
        self.data_admissao = data_admissao

    def limpar_cpf(self, cpf): # Remove pontos e traços do CPF
        return cpf.replace(".", "").replace("-", "")

    def buscar_aluno_por_cpf(self, lista_alunos, cpf): # Busca aluno pelo CPF
        cpf = self.limpar_cpf(cpf)

        for aluno in lista_alunos:
            if self.limpar_cpf(aluno.cpf) == cpf:
                return aluno

        return None

    def buscar_responsavel_por_cpf(self, lista_responsaveis, cpf): # Busca responsável pelo CPF
        cpf = self.limpar_cpf(cpf)

        for r in lista_responsaveis:
            if self.limpar_cpf(r.cpf) == cpf:
                return r

        return None

    def cadastrar_aluno(self, lista_alunos, aluno): # Cadastra aluno (evita duplicado)
        if self.buscar_aluno_por_cpf(lista_alunos, aluno.cpf):
            print("Aluno já cadastrado.")
        else:
            lista_alunos.append(aluno)
            print(f"Aluno {aluno.nome} cadastrado com sucesso.")

    def cadastrar_responsavel(self, lista_responsaveis, responsavel): # Cadastra responsável (evita duplicado)
        if self.buscar_responsavel_por_cpf(lista_responsaveis, responsavel.cpf):
            print("Responsável já cadastrado.")
        else:
            lista_responsaveis.append(responsavel)
            print(f"Responsável {responsavel.nome} cadastrado com sucesso.")

    def vincular_responsavel_aluno(self, lista_alunos, lista_responsaveis, cpf_aluno, cpf_responsavel): # Vincula responsável ao aluno usando CPF

        aluno = self.buscar_aluno_por_cpf(lista_alunos, cpf_aluno)
        responsavel = self.buscar_responsavel_por_cpf(lista_responsaveis, cpf_responsavel)

        if aluno and responsavel:
            # vincula no aluno
            aluno.responsavel = responsavel

            # garante lista de alunos no responsável
            if not hasattr(responsavel, "alunos"):
                responsavel.alunos = []

            # evita duplicar vínculo
            if aluno not in responsavel.alunos:
                responsavel.alunos.append(aluno)

            print(f"{responsavel.nome} vinculado ao aluno {aluno.nome}.")
        else:
            print("Erro: aluno ou responsável não encontrado.")