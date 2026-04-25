import csv
from datetime import datetime
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

def ler_csv(nome_arquivo):
    with open(BASE_PATH + nome_arquivo, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def carregar_usuarios():
    linhas = ler_csv("usuarios.csv")
    usuarios = []

    for linha in linhas:
        endereco = Endereco(
            id_endereco=int(linha["id_usuario"]),
            cep=linha["cep"],
            logradouro=linha["logradouro"],
            numero=linha["numero"],
            bairro=linha["bairro"]
        )

        usuario = Usuario(
            id_usuario=int(linha["id_usuario"]),
            nome=linha["nome"],
            cpf=linha["cpf"],
            email=linha["email"],
            senha=linha["senha"],
            data_nascimento=datetime.strptime(
                linha["data_nascimento"], "%Y-%m-%d"
            ).date(),
            genero=linha["genero"],
            telefone=linha["telefone"],
            cargo=linha["cargo"],
            endereco=endereco
        )

        usuarios.append(usuario)

    return usuarios


def carregar_alunos():
    linhas = ler_csv("alunos.csv")
    alunos = []

    for linha in linhas:
        endereco = Endereco(
            id_endereco=int(linha["id_aluno"]),
            cep=linha["cep"],
            logradouro=linha["logradouro"],
            numero=linha["numero"],
            bairro=linha["bairro"]
        )

        aluno = Aluno(
            id_aluno=int(linha["id_aluno"]),
            nome=linha["nome"],
            data_nascimento=datetime.strptime(
                linha["data_nascimento"], "%Y-%m-%d"
            ).date(),
            cpf=linha["cpf"],
            genero=linha["genero"],
            telefone=linha["telefone"],
            email=linha["email"],
            endereco=endereco,
            responsavel=linha["responsavel"]
        )

        alunos.append(aluno)

    return alunos


def carregar_cursos():
    linhas = ler_csv("cursos.csv")
    cursos = []

    for linha in linhas:
        curso = Curso(
            id_curso=int(linha["id_curso"]),
            nome=linha["nome"],
            carga_horaria=int(linha["carga_horaria"]),
            valor=float(linha["valor"]),
            ativo=linha["ativo"] == "True"
        )

        cursos.append(curso)

    return cursos


def carregar_disciplinas(cursos, usuarios):
    linhas = ler_csv("disciplinas.csv")
    disciplinas = []

    for linha in linhas:
        curso = next(
            (c for c in cursos if c.id_curso == int(linha["id_curso"])),
            None
        )

        professor = next(
            (u for u in usuarios if u.id_usuario == int(linha["id_professor"])),
            None
        )

        if curso is None or professor is None:
            continue

        disciplina = Disciplina(
            id_disciplina=int(linha["id_disciplina"]),
            nome=linha["nome"],
            curso=curso,
            professor=professor,
            carga_horaria=int(linha["carga_horaria"]),
            dia_semana=linha["dia_semana"],
            hora_inicio=linha["hora_inicio"],
            hora_fim=linha["hora_fim"],
            ativa=linha["ativa"] == "True"
        )

        disciplinas.append(disciplina)

    return disciplinas


def carregar_turmas(cursos, disciplinas, usuarios):
    linhas = ler_csv("turmas.csv")
    turmas = []

    for linha in linhas:
        curso = next(
            (c for c in cursos if c.id_curso == int(linha["id_curso"])),
            None
        )

        disciplina = next(
            (d for d in disciplinas if d.id_disciplina == int(linha["id_disciplina"])),
            None
        )

        professor = next(
            (u for u in usuarios if u.id_usuario == int(linha["id_professor"])),
            None
        )

        if curso is None or disciplina is None or professor is None:
            continue

        turma = Turma(
            id_turma=int(linha["id_turma"]),
            nome=linha["nome"],
            curso=curso,
            disciplina=disciplina,
            professor=professor,
            horario=linha["horario"],
            vagas=int(linha["vagas"]),
            status=linha["status"]
        )

        turmas.append(turma)

    return turmas



def carregar_matriculas(alunos, turmas):
    linhas = ler_csv("matriculas.csv")
    matriculas = []

    for linha in linhas:
        aluno = next(
            (a for a in alunos if a.id_aluno == int(linha["id_aluno"])),
            None
        )
        turma = next(
            (t for t in turmas if t.id_turma == int(linha["id_turma"])),
            None
        )

        if aluno is None or turma is None:
            continue

        # ✅ cria APENAS com o que o __init__ aceita
        matricula = Matricula(aluno, turma)

        # ✅ atribuições pós-criação (compatível com seu model)
        matricula.id_matricula = int(linha["id_matricula"])
        matricula.data_matricula = datetime.strptime(
            linha["data_matricula"], "%Y-%m-%d"
        ).date()
        matricula.status = linha["status"]

        matriculas.append(matricula)

    return matriculas


def carregar_frequencias(alunos, turmas, disciplinas):
    linhas = ler_csv("frequencia.csv")
    frequencias = []

    for linha in linhas:
        aluno = next(
            (a for a in alunos if a.id_aluno == int(linha["id_aluno"])),
            None
        )
        turma = next(
            (t for t in turmas if t.id_turma == int(linha["id_turma"])),
            None
        )
        disciplina = next(
            (d for d in disciplinas if d.id_disciplina == int(linha["id_disciplina"])),
            None
        )

        if aluno is None or turma is None or disciplina is None:
            continue

        data = datetime.strptime(linha["data"], "%Y-%m-%d").date()

        # ✅ AGORA o __init__ bate exatamente
        frequencia = Frequencia(aluno, turma, disciplina, data)

        # ✅ atributos extras (NÃO vão no construtor)
        frequencia.id_frequencia = int(linha["id_frequencia"])
        frequencia.presente = linha["presente"] == "True"

        frequencias.append(frequencia)

    return frequencia


def carregar_desempenhos(alunos, turmas, disciplinas):
    linhas = ler_csv("desempenho.csv")
    desempenhos = []

    for linha in linhas:
        aluno = next(
            (a for a in alunos if a.id_aluno == int(linha["id_aluno"])),
            None
        )
        disciplina = next(
            (d for d in disciplinas if d.id_disciplina == int(linha["id_disciplina"])),
            None
        )
        turma = next(
            (t for t in turmas if t.id_turma == int(linha["id_turma"])),
            None
        )

        if aluno is None or disciplina is None or turma is None:
            continue

        # ✅ __init__ aceita SOMENTE (aluno, disciplina)
        desempenho = Desempenho(aluno, disciplina)

        # ✅ Demais dados são atribuídos após a criação
        desempenho.id_desempenho = int(linha["id_desempenho"])
        desempenho.turma = turma
        desempenho.tipo = linha["tipo"]
        desempenho.valor = float(linha["valor"])
        desempenho.data = datetime.strptime(
            linha["data"], "%Y-%m-%d"
        ).date()

        desempenhos.append(desempenho)

    return desempenhos
