from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Cria a conexão com o arquivo do banco de dados
engine = create_engine('sqlite:///sistema_escolar.db', echo=False)

# 2. Cria a "Base" que as suas outras classes (Aluno, Professor) usam
Base = declarative_base()

# 3. CRIA O SESSIONLOCAL (É isso que estava faltando!)
# Ele é a fábrica de "sessões" para salvar e buscar dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)