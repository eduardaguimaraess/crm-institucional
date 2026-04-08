from usuario import Usuario

# Classe Professor
class Professor(Usuario):

    def __init__(self, id_usuario, nome, data_nascimento, cpf, genero,
                 telefone, email, senha,
                 id_professor, salario, data_admissao,
                 cargo="professor", ativo=True):

        super().__init__(
            id_usuario, nome, data_nascimento, cpf,
            genero, telefone, email, senha,
            cargo, ativo
        )

        self.id_professor = id_professor
        self.salario = salario
        self.data_admissao = data_admissao