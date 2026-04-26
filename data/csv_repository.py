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

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

# ==================================================
# FUNÇÕES DE PERSISTÊNCIA (GRAVAÇÃO)
# ==================================================

def salvar_csv(nome_arquivo, lista_objetos):
    if not lista_objetos: return
    caminho = BASE_PATH + nome_arquivo
    dados_para_salvar = []
    for obj in lista_objetos:
        item = obj.__dict__.copy()
        if 'endereco' in item and isinstance(item['endereco'], Endereco):
            end = item['endereco']
            item['id_endereco'] = end.id_endereco
            item['cep'] = end.cep
            item['logradouro'] = end.logradouro
            item['numero'] = end.numero
            item['bairro'] = end.bairro
            del item['endereco']
        for chave in list(item.keys()):
            valor = item[chave]
            if hasattr(valor, 'id_curso'): item[chave] = valor.id_curso
            elif hasattr(valor, 'id_disciplina'): item[chave] = valor.id_disciplina
            elif hasattr(valor, 'id_usuario'): item[chave] = valor.id_usuario
            elif hasattr(valor, 'id_aluno'): item[chave] = valor.id_aluno
            elif hasattr(valor, 'id_turma'): item[chave] = valor.id_turma
            elif hasattr(valor, 'id_matricula'): item[chave] = valor.id_matricula
            elif isinstance(valor, (date, datetime)):
                item[chave] = valor.strftime("%Y-%m-%d")
            elif isinstance(valor, list) and nome_arquivo != "desempenho.csv":
                del item[chave]
        dados_para_salvar.append(item)
    if dados_para_salvar:
        fieldnames = dados_para_salvar[0].keys()
        with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dados_para_salvar)

def salvar_usuarios(usuarios): salvar_csv("usuarios.csv", usuarios)
def salvar_alunos(alunos): salvar_csv("alunos.csv", alunos)
def salvar_cursos(cursos): salvar_csv("cursos.csv", cursos)
def salvar_disciplinas(disciplinas): salvar_csv("disciplinas.csv", disciplinas)
def salvar_turmas(turmas): salvar_csv("turmas.csv", turmas)
def salvar_matriculas(matriculas): salvar_csv("matriculas.csv", matriculas)
def salvar_frequencias(frequencias): salvar_csv("frequencia.csv", frequencias)

def salvar_desempenhos(lista_desempenhos):
    caminho = BASE_PATH + "desempenho.csv"
    dados_para_salvar = []
    for des in lista_desempenhos:
        notas_obj = getattr(des, 'notas', [])
        for n in notas_obj:
            dados_para_salvar.append({
                'id_aluno': des.aluno.id_aluno,
                'id_disciplina': des.disciplina.id_disciplina,
                'id_turma': des.turma.id_turma if hasattr(des, 'turma') else 0,
                'valor': n.get('valor') if isinstance(n, dict) else n,
                'tipo': n.get('tipo', 'prova') if isinstance(n, dict) else 'prova'
            })
    if dados_para_salvar:
        fieldnames = ['id_aluno', 'id_disciplina', 'id_turma', 'valor', 'tipo']
        with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dados_para_salvar)

def salvar_notas(notas): salvar_desempenhos(notas)

# ==================================================
# FUNÇÕES DE LEITURA (COM BLINDAGEM CONTRA ERROS)
# ==================================================

def ler_csv(nome_arquivo):
    caminho = BASE_PATH + nome_arquivo
    if not os.path.exists(caminho): return []
    try:
        with open(caminho, newline="", encoding="utf-8") as arquivo:
            return list(csv.DictReader(arquivo))
    except: return []

def carregar_usuarios():
    linhas = ler_csv("usuarios.csv")
    usuarios = []
    for linha in linhas:
        try:
            end = Endereco(
                id_endereco=int(linha.get("id_endereco", 0)),
                cep=linha.get("cep", ""), logradouro=linha.get("logradouro", ""),
                numero=linha.get("numero", ""), bairro=linha.get("bairro", "")
            )
            usuarios.append(Usuario(
                id_usuario=int(linha["id_usuario"]), nome=linha["nome"], cpf=linha["cpf"],
                email=linha["email"], senha=linha["senha"],
                data_nascimento=datetime.strptime(linha["data_nascimento"], "%Y-%m-%d").date(),
                genero=linha["genero"], telefone=linha["telefone"], cargo=linha["cargo"], endereco=end
            ))
        except: continue
    return usuarios

def carregar_alunos():
    linhas = ler_csv("alunos.csv")
    alunos = []
    for linha in linhas:
        try:
            end = Endereco(
                id_endereco=int(linha.get("id_endereco", 0)),
                cep=linha.get("cep", ""), logradouro=linha.get("logradouro", ""),
                numero=linha.get("numero", ""), bairro=linha.get("bairro", "")
            )
            alunos.append(Aluno(
                id_aluno=int(linha["id_aluno"]), nome=linha["nome"],
                data_nascimento=datetime.strptime(linha["data_nascimento"], "%Y-%m-%d").date(),
                cpf=linha["cpf"], genero=linha["genero"], telefone=linha["telefone"],
                email=linha["email"], endereco=end, responsavel=linha.get("responsavel", "O próprio")
            ))
        except: continue
    return alunos

def carregar_cursos():
    linhas = ler_csv("cursos.csv")
    cursos = []
    for l in linhas:
        try:
            cursos.append(Curso(int(l["id_curso"]), l["nome"], int(l["carga_horaria"]), float(l["valor"]), l["ativo"] == "True"))
        except: continue
    return cursos

def carregar_disciplinas(cursos, usuarios):
    linhas = ler_csv("disciplinas.csv")
    disciplinas = []
    for l in linhas:
        try:
            id_c = l.get("curso") or l.get("id_curso")
            id_p = l.get("professor") or l.get("id_professor")
            c = next((c for c in cursos if c.id_curso == int(id_c)), None)
            p = next((u for u in usuarios if u.id_usuario == int(id_p)), None)
            if c and p:
                disciplinas.append(Disciplina(int(l["id_disciplina"]), l["nome"], c, p, int(l["carga_horaria"]), l["dia_semana"], l["hora_inicio"], l["hora_fim"], l.get("ativa") == "True"))
        except: continue
    return disciplinas

def carregar_turmas(cursos, disciplinas, usuarios):
    linhas = ler_csv("turmas.csv")
    turmas = []
    for l in linhas:
        try:
            id_c = l.get("curso") or l.get("id_curso")
            id_d = l.get("disciplina") or l.get("id_disciplina")
            id_p = l.get("professor") or l.get("id_professor")
            c = next((c for c in cursos if c.id_curso == int(id_c)), None)
            d = next((d for d in disciplinas if d.id_disciplina == int(id_d)), None)
            p = next((u for u in usuarios if u.id_usuario == int(id_p)), None)
            if c and d and p:
                turmas.append(Turma(int(l["id_turma"]), l["nome"], c, d, p, l["horario"], int(l["vagas"]), l.get("status", "Ativa")))
        except: continue
    return turmas

def carregar_matriculas(alunos, turmas):
    linhas = ler_csv("matriculas.csv")
    matriculas = []
    for l in linhas:
        try:
            id_al = l.get("aluno") or l.get("id_aluno")
            id_tu = l.get("turma") or l.get("id_turma")
            al = next((a for a in alunos if a.id_aluno == int(id_al)), None)
            tu = next((t for t in turmas if t.id_turma == int(id_tu)), None)
            if al and tu:
                m = Matricula(al, tu)
                m.id_matricula = int(l["id_matricula"])
                m.data_matricula = datetime.strptime(l["data_matricula"], "%Y-%m-%d").date()
                m.status = l.get("status", "Ativa")
                matriculas.append(m)
        except: continue
    return matriculas

def carregar_frequencias(alunos, turmas, disciplinas):
    linhas = ler_csv("frequencia.csv")
    frequencias = []
    for l in linhas:
        try:
            id_al = l.get("aluno") or l.get("id_aluno")
            id_tu = l.get("turma") or l.get("id_turma")
            id_di = l.get("disciplina") or l.get("id_disciplina")
            
            # Checagem extra de segurança para evitar erro de int() vazio
            if not all([id_al, id_tu, id_di]): continue

            al = next((a for a in alunos if a.id_aluno == int(id_al)), None)
            tu = next((t for t in turmas if t.id_turma == int(id_tu)), None)
            di = next((d for d in disciplinas if d.id_disciplina == int(id_di)), None)
            
            if al and tu and di:
                f = Frequencia(al, tu, di, datetime.strptime(l["data"], "%Y-%m-%d").date())
                f.id_frequencia = int(l.get("id_frequencia", 0))
                f.presente = l["presente"] == "True"
                frequencias.append(f)
        except: continue
    return frequencias

def carregar_desempenhos(alunos, turmas, disciplinas):
    linhas = ler_csv("desempenho.csv")
    desempenhos = []
    for l in linhas:
        try:
            id_al = l.get("aluno") or l.get("id_aluno")
            id_di = l.get("disciplina") or l.get("id_disciplina")
            if not id_al or not id_di: continue

            al = next((a for a in alunos if a.id_aluno == int(id_al)), None)
            di = next((d for d in disciplinas if d.id_disciplina == int(id_di)), None)
            
            if al and di:
                des = next((d for d in desempenhos if d.aluno.id_aluno == al.id_aluno and d.disciplina.id_disciplina == di.id_disciplina), None)
                
                if not des:
                    des = Desempenho(al, di)
                    # ESSA LINHA ABAIXO É A QUE RESOLVE O ERRO:
                    des.id_desempenho = len(desempenhos) + 1 
                    desempenhos.append(des)
                
                valor_n = l.get("valor", "0")
                des.adicionar_nota(float(valor_n) if valor_n else 0.0, l.get("tipo", "prova"))
        except: continue
    return desempenhos