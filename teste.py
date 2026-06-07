from data.database import conectar

conexao = conectar()

print("Conectou!")

conexao.close()