import csv
import os
from datetime import datetime, date
from models.usuario import Usuario
from models.aluno import Aluno
from models.endereco import Endereco
from models.curso import Curso
from models.disciplina import Disciplina
from models.turma import Turma
from models.matricula import Matricula
from models.frequencia import Frequencia
from models.desempenho import Desempenho

BASE_PATH = "data/"

# Garante que a pasta data existe
if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

# ==================================================
# FUNÇÕES DE PERSISTÊNCIA (GRAVAÇÃO)
# ==================================================

def salvar_csv(nome_arquivo, lista_objetos):
    """Função genérica para converter objetos em dicionários e sobrescrever o CSV."""
    if not lista_objetos:
        # Se a lista estiver vazia, apenas garante que o arquivo existe (opcional)
        return

    caminho = BASE_PATH + nome_arquivo
    dados_para_salvar = []

    for obj in lista_objetos:
        # Cria uma cópia dos atributos do objeto
        item = obj.__dict__.copy()
        
        # 1. Tratamento especial para Endereço (Flattening para uma única linha no CSV)
        if 'endereco' in item and isinstance(item['endereco'], Endereco):
            end = item['endereco']
            item['id_endereco'] = end.id_endereco
            item['cep'] = end.cep
            item['logradouro'] = end.logradouro
            item['numero'] = end.numero
            item['bairro'] = end.bairro
            del item['endereco']

        # 2. Converte objetos relacionados em IDs e trata Datas
        for chave in list(item.keys()):
            valor = item[chave]
            
            # Se for um objeto de Model, salva apenas o ID
            if hasattr(valor, 'id_curso'): item[chave] = valor.id_curso
            elif hasattr(valor, 'id_disciplina'): item[chave] = valor.id_disciplina
            elif hasattr(valor, 'id_usuario'): item[chave] = valor.id_usuario
            elif hasattr(valor, 'id_aluno'): item[chave] = valor.id_aluno
            elif hasattr(valor, 'id_turma'): item[chave] = valor.id_turma
            elif hasattr(valor, 'id_matricula'): item[chave] = valor.id_matricula
            
            # Formata datas para String
            elif isinstance(valor, (date, datetime)):
                item[chave] = valor.strftime("%Y-%m-%d")
            
            # Remove listas internas (como frequencias=[], matriculas=[]) para não sujar o CSV
            elif isinstance(valor, list):
                del item[chave]

        dados_para_salvar.append(item)

    if dados_para_salvar:
        fieldnames = dados_para_salvar[0].keys()
        with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dados_para_salvar)

# Atalhos de salvamento usados pelos Controllers
def salvar_usuarios(usuarios): salvar_csv("usuarios.csv", usuarios)
def salvar_alunos(alunos): salvar_csv("alunos.csv", alunos)
def salvar_cursos(cursos): salvar_csv("cursos.csv", cursos)
def salvar_disciplinas(disciplinas): salvar_csv("disciplinas.csv", disciplinas)
def salvar_turmas(turmas): salvar_csv("turmas.csv", turmas)
def salvar_matriculas(matriculas): salvar_csv("matriculas.csv", matriculas)
def salvar_frequencias(frequencias): salvar_csv("frequencia.csv", frequencias)
def salvar_desempenhos(desempenhos): salvar_csv("desempenho.csv", desempenhos)
def salvar_notas(notas): salvar_csv("desempenho.csv", notas) # Aliás para compatibilidade

# ==================================================
# FUNÇÕES DE CARREGAMENTO (LEITURA INTEGRADA)
# ==================================================

def ler_csv(nome_arquivo):
    caminho = BASE_PATH + nome_arquivo
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, newline="", encoding="utf-8") as arquivo:
            return list(csv.DictReader(arquivo))
    except Exception:
        return []

def carregar_usuarios():
    linhas = ler_csv("usuarios.csv")
    usuarios = []
    for linha in linhas:
        endereco = Endereco(
            id_endereco=int(linha.get("id_endereco", 0)),
            cep=linha["cep"], logradouro=linha["logradouro"],
            numero=linha["numero"], bairro=linha["bairro"]
        )
        usuarios.append(Usuario(
            id_usuario=int(linha["id_usuario"]), nome=linha["nome"],
            cpf=linha["cpf"], email=linha["email"], senha=linha["senha"],
            data_nascimento=datetime.strptime(linha["data_nascimento"], "%Y-%m-%d").date(),
            genero=linha["genero"], telefone=linha["telefone"], cargo=linha["cargo"], endereco=endereco
        ))
    return usuarios

def carregar_alunos():
    linhas = ler_csv("alunos.csv")
    alunos = []
    for linha in linhas:
        endereco = Endereco(
            id_endereco=int(linha.get("id_endereco", 0)),
            cep=linha["cep"], logradouro=linha["logradouro"],
            numero=linha["numero"], bairro=linha["bairro"]
        )
        alunos.append(Aluno(
            id_aluno=int(linha["id_aluno"]), nome=linha["nome"],
            data_nascimento=datetime.strptime(linha["data_nascimento"], "%Y-%m-%d").date(),
            cpf=linha["cpf"], genero=linha["genero"], telefone=linha["telefone"],
            email=linha["email"], endereco=endereco, responsavel=linha["responsavel"]
        ))
    return alunos

def carregar_cursos():
    linhas = ler_csv("cursos.csv")
    cursos = []
    for linha in linhas:
        cursos.append(Curso(
            id_curso=int(linha["id_curso"]), nome=linha["nome"],
            carga_horaria=int(linha["carga_horaria"]), valor=float(linha["valor"]),
            ativo=linha["ativo"] == "True"
        ))
    return cursos

def carregar_disciplinas(cursos, usuarios):
    linhas = ler_csv("disciplinas.csv")
    disciplinas = []
    for linha in linhas:
        c_id = linha.get("curso") or linha.get("id_curso")
        p_id = linha.get("professor") or linha.get("id_professor")
        if not c_id or not p_id: continue

        curso = next((c for c in cursos if c.id_curso == int(c_id)), None)
        professor = next((u for u in usuarios if u.id_usuario == int(p_id)), None)

        if curso and professor:
            disciplinas.append(Disciplina(
                id_disciplina=int(linha["id_disciplina"]), nome=linha["nome"],
                curso=curso, professor=professor, carga_horaria=int(linha["carga_horaria"]),
                dia_semana=linha["dia_semana"], hora_inicio=linha["hora_inicio"],
                hora_fim=linha["hora_fim"], ativa=linha["ativa"] == "True"
            ))
    return disciplinas

def carregar_turmas(cursos, disciplinas, usuarios):
    linhas = ler_csv("turmas.csv")
    turmas = []
    for linha in linhas:
        c_id = linha.get("curso") or linha.get("id_curso")
        d_id = linha.get("disciplina") or linha.get("id_disciplina")
        p_id = linha.get("professor") or linha.get("id_professor")
        if not all([c_id, d_id, p_id]): continue

        curso = next((c for c in cursos if c.id_curso == int(c_id)), None)
        disciplina = next((d for d in disciplinas if d.id_disciplina == int(d_id)), None)
        professor = next((u for u in usuarios if u.id_usuario == int(p_id)), None)

        if curso and disciplina and professor:
            turmas.append(Turma(
                id_turma=int(linha["id_turma"]), nome=linha["nome"], curso=curso,
                disciplina=disciplina, professor=professor, horario=linha["horario"],
                vagas=int(linha["vagas"]), status=linha["status"]
            ))
    return turmas

def carregar_matriculas(alunos, turmas):
    linhas = ler_csv("matriculas.csv")
    matriculas = []
    for linha in linhas:
        a_id = linha.get("aluno") or linha.get("id_aluno")
        t_id = linha.get("turma") or linha.get("id_turma")
        if not a_id or not t_id: continue

        aluno = next((a for a in alunos if a.id_aluno == int(a_id)), None)
        turma = next((t for t in turmas if t.id_turma == int(t_id)), None)

        if aluno and turma:
            m = Matricula(aluno, turma)
            m.id_matricula = int(linha["id_matricula"])
            m.data_matricula = datetime.strptime(linha["data_matricula"], "%Y-%m-%d").date()
            m.status = linha["status"]
            
            # Sincronização de objetos (Essencial para as Views funcionarem)
            if not hasattr(turma, 'matriculas'): turma.matriculas = []
            turma.matriculas.append(m)
            if not hasattr(aluno, 'matriculas'): aluno.matriculas = []
            aluno.matriculas.append(m)
            
            matriculas.append(m)
    return matriculas

def carregar_frequencias(alunos, turmas, disciplinas):
    linhas = ler_csv("frequencia.csv")
    frequencias = []
    for linha in linhas:
        a_id = linha.get("aluno") or linha.get("id_aluno")
        t_id = linha.get("turma") or linha.get("id_turma")
        d_id = linha.get("disciplina") or linha.get("id_disciplina")
        if not all([a_id, t_id, d_id]): continue

        aluno = next((a for a in alunos if a.id_aluno == int(a_id)), None)
        turma = next((t for t in turmas if t.id_turma == int(t_id)), None)
        disciplina = next((d for d in disciplinas if d.id_disciplina == int(d_id)), None)

        if aluno and turma and disciplina:
            data = datetime.strptime(linha["data"], "%Y-%m-%d").date()
            f = Frequencia(aluno, turma, disciplina, data)
            f.id_frequencia = int(linha["id_frequencia"])
            f.presente = (linha["presente"] == "True")
            
            if not hasattr(aluno, 'frequencias'): aluno.frequencias = []
            aluno.frequencias.append(f)
            frequencias.append(f)
    return frequencias

def carregar_desempenhos(alunos, turmas, disciplinas):
    linhas = ler_csv("desempenho.csv")
    desempenhos = []
    for linha in linhas:
        a_id = linha.get("aluno") or linha.get("id_aluno")
        d_id = linha.get("disciplina") or linha.get("id_disciplina")
        t_id = linha.get("turma") or linha.get("id_turma")
        if not all([a_id, d_id, t_id]): continue

        aluno = next((a for a in alunos if a.id_aluno == int(a_id)), None)
        disciplina = next((d for d in disciplinas if d.id_disciplina == int(d_id)), None)
        turma = next((t for t in turmas if t.id_turma == int(t_id)), None)

        if aluno and disciplina and turma:
            # Tenta encontrar se o objeto Desempenho já foi criado para este aluno nesta disciplina
            des = next((d for d in desempenhos if d.aluno.id_aluno == aluno.id_aluno and d.disciplina.id_disciplina == disciplina.id_disciplina), None)
            
            if not des:
                des = Desempenho(aluno, disciplina)
                des.turma = turma
                if not hasattr(aluno, 'desempenhos'): aluno.desempenhos = []
                aluno.desempenhos.append(des)
                desempenhos.append(des)
            
            # Adiciona a nota específica contida na linha do CSV ao objeto Desempenho
            valor = float(linha.get("valor", 0))
            tipo = linha.get("tipo", "prova")
            des.adicionar_nota(valor, tipo)
            
    return desempenhos