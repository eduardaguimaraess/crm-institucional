from data.mysql_repository import carregar_usuarios

usuarios = carregar_usuarios()

for usuario in usuarios:
    print(usuario.nome)