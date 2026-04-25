from models.database import engine, SessionLocal
from models.usuario import Base, Usuario
from models.endereco import Endereco
from models.aluno import Aluno
from models.professor import Professor
from models.curso import Curso
from models.disciplina import Disciplina
from models.matricula import Matricula
from models.frequencia import Frequencia
from models.turma import Turma
from models.desempenho import Desempenho
from models.responsavel import Responsavel

# 1. Cria TODAS as tabelas no arquivo .db
print("Sincronizando todas as tabelas do sistema...")
Base.metadata.create_all(bind=engine)
print("Sucesso! O arquivo sistema_escolar.db foi criado com todas as tabelas.")

db = SessionLocal()

try:
    # 2. Criar um Endereço primeiro (necessário para o usuário não dar erro)
    print("Criando endereço de teste...")
    novo_endereco = Endereco(
        cep="29470-000",
        logradouro="Rua Principal",
        numero="S/N",
        bairro="Centro"
        # Se der erro de 'unexpected argument', remova os campos acima um por um
    )
    db.add(novo_endereco)
    db.commit()
    db.refresh(novo_endereco)

    # 3. Criar o Usuário Admin vinculado ao endereço
    print("Criando usuário administrador...")
    admin_existe = db.query(Usuario).filter(Usuario.cpf == "11111111111").first()
    
    if not admin_existe:
        admin = Usuario(
            nome="Dyogo Admin",
            cpf="11111111111",
            senha="12345",
            cargo="admin",
            data_nascimento="2000-01-01",
            genero="Masculino",
            telefone="28 9999-9999",
            email="dyogo@email.com",
            # Tentamos id_endereco primeiro (padrão do seu projeto)
            # Se der erro de 'attribute', mude para novo_endereco.id
            endereco_id=novo_endereco.id_endereco 
        )
        db.add(admin)
        db.commit()
        print("✅ TUDO PRONTO! Usuário 'Dyogo Admin' criado com sucesso.")
    else:
        print("O usuário administrador já existe.")

except Exception as e:
    print(f"❌ Erro final: {e}")
    db.rollback()
finally:
    db.close()