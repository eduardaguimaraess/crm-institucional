# python -m main.teste_models

from models.usuario import Usuario

usuario = Usuario(
    id=1,
    nome="Admin",
    data_nascimento="1990-01-01",
    cpf="00000000000",
    genero="M",
    telefone="31999999999",
    email="admin@email.com",
    senha="123",
    perfil="admin"
)

print(usuario.autenticar("00000000000", "123"))
