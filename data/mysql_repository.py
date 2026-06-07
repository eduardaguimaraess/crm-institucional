from data.database import conectar
from models.usuario import Usuario
from models.aluno import Aluno
from models.endereco import Endereco
from models.curso import Curso
from models.disciplina import Disciplina
from models.turma import Turma
from models.matricula import Matricula
from models.frequencia import Frequencia
from models.desempenho import Desempenho
from datetime import datetime

def carregar_usuarios():

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")

    dados = cursor.fetchall()

    usuarios = []

    for linha in dados:

        endereco = Endereco(
            id_endereco=linha["id_endereco"],
            cep="",
            logradouro="",
            numero="",
            bairro=""
        )

        usuario = Usuario(
            id_usuario=linha["id_usuario"],
            nome=linha["nome"],
            cpf=linha["cpf"],
            email=linha["email"],
            senha=linha["senha"],
            data_nascimento=linha["data_nascimento"],
            genero=linha["genero"],
            telefone=linha["telefone"],
            cargo=linha["cargo"],
            endereco=endereco
        )

        usuarios.append(usuario)

    conn.close()

    return usuarios

def carregar_alunos():

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()

    alunos = []

    for linha in dados:

        endereco = Endereco(
            id_endereco=linha["id_endereco"],
            cep="",
            logradouro="",
            numero="",
            bairro=""
        )

        aluno = Aluno(
            id_aluno=linha["id_aluno"],
            nome=linha["nome"],
            data_nascimento=linha["data_nascimento"],
            cpf=linha["cpf"],
            genero=linha["genero"],
            telefone=linha["telefone"],
            email=linha["email"],
            endereco=endereco,
            responsavel=linha["responsavel"]
        )

        alunos.append(aluno)

    conn.close()

    return alunos

def salvar_usuarios(lista_usuarios):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios")

    for usuario in lista_usuarios:

        cursor.execute("""
            INSERT INTO usuarios
            (
                id_usuario,
                nome,
                data_nascimento,
                cpf,
                genero,
                telefone,
                email,
                senha,
                cargo,
                ativo,
                id_endereco
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            usuario.id_usuario,
            usuario.nome,
            usuario.data_nascimento,
            usuario.cpf,
            usuario.genero,
            usuario.telefone,
            usuario.email,
            usuario.senha,
            usuario.cargo,
            usuario.ativo,
            usuario.endereco.id_endereco
        ))

    conn.commit()
    conn.close()

def salvar_alunos(lista_alunos):

    print("ENTROU NO SALVAR_ALUNOS")
    print("Quantidade:", len(lista_alunos))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos")

    for aluno in lista_alunos:

        cursor.execute("""
            INSERT INTO alunos
            (
                id_aluno,
                nome,
                data_nascimento,
                cpf,
                genero,
                telefone,
                email,
                responsavel,
                status,
                id_endereco
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            aluno.id_aluno,
            aluno.nome,
            aluno.data_nascimento,
            aluno.cpf,
            aluno.genero,
            aluno.telefone,
            aluno.email,
            aluno.responsavel,
            aluno.status,
            aluno.endereco.id_endereco
        ))

    conn.commit()
    conn.close()

def carregar_cursos():

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cursos")

    dados = cursor.fetchall()

    cursos = []

    for linha in dados:

        curso = Curso(
            id_curso=linha["id_curso"],
            nome=linha["nome"],
            carga_horaria=linha["carga_horaria"],
            valor=float(linha["valor"]),
            ativo=linha["ativo"]
        )

        cursos.append(curso)

    conn.close()

    return cursos


def salvar_cursos(lista_cursos):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cursos")

    for curso in lista_cursos:

        cursor.execute("""
            INSERT INTO cursos
            (
                id_curso,
                nome,
                carga_horaria,
                valor,
                ativo
            )
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            curso.id_curso,
            curso.nome,
            curso.carga_horaria,
            curso.valor,
            curso.ativo
        ))

    conn.commit()
    conn.close()

def salvar_disciplinas(lista_disciplinas):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM disciplinas")

    for disciplina in lista_disciplinas:

        cursor.execute("""
            INSERT INTO disciplinas
            (
                id_disciplina,
                nome,
                id_curso,
                id_professor,
                carga_horaria,
                dia_semana,
                hora_inicio,
                hora_fim,
                ativa
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            disciplina.id_disciplina,
            disciplina.nome,
            disciplina.curso.id_curso,
            disciplina.professor.id_usuario,
            disciplina.carga_horaria,
            disciplina.dia_semana,
            disciplina.hora_inicio,
            disciplina.hora_fim,
            disciplina.ativa
        ))

    conn.commit()
    conn.close()

def carregar_disciplinas(cursos, usuarios):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM disciplinas")

    dados = cursor.fetchall()

    disciplinas = []

    for linha in dados:

        curso = next(
            (c for c in cursos if c.id_curso == linha["id_curso"]),
            None
        )

        professor = next(
            (u for u in usuarios if u.id_usuario == linha["id_professor"]),
            None
        )

        if curso and professor:

            disciplina = Disciplina(
                id_disciplina=linha["id_disciplina"],
                nome=linha["nome"],
                curso=curso,
                professor=professor,
                carga_horaria=linha["carga_horaria"],
                dia_semana=linha["dia_semana"],
                hora_inicio=linha["hora_inicio"],
                hora_fim=linha["hora_fim"],
                ativa=linha["ativa"]
            )

            disciplinas.append(disciplina)

    conn.close()

    return disciplinas

def salvar_turmas(lista_turmas):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM turmas")

    for turma in lista_turmas:

        cursor.execute("""
            INSERT INTO turmas
            (
                id_turma,
                nome,
                id_curso,
                id_disciplina,
                id_professor,
                horario,
                vagas,
                status
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            turma.id_turma,
            turma.nome,
            turma.curso.id_curso,
            turma.disciplina.id_disciplina,
            turma.professor.id_usuario,
            turma.horario,
            turma.vagas,
            turma.status
        ))

    conn.commit()
    conn.close()

def carregar_turmas(cursos, disciplinas, usuarios):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM turmas")

    dados = cursor.fetchall()

    turmas = []

    for linha in dados:

        curso = next(
            (c for c in cursos if c.id_curso == linha["id_curso"]),
            None
        )

        disciplina = next(
            (d for d in disciplinas if d.id_disciplina == linha["id_disciplina"]),
            None
        )

        professor = next(
            (u for u in usuarios if u.id_usuario == linha["id_professor"]),
            None
        )

        if curso and disciplina and professor:

            turma = Turma(
                id_turma=linha["id_turma"],
                nome=linha["nome"],
                curso=curso,
                disciplina=disciplina,
                professor=professor,
                horario=linha["horario"],
                vagas=linha["vagas"],
                status=linha["status"]
            )

            turmas.append(turma)

    conn.close()

    return turmas

def salvar_matriculas(lista_matriculas):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM matriculas")

    for matricula in lista_matriculas:

        cursor.execute("""
            INSERT INTO matriculas
            (
                id_matricula,
                id_aluno,
                id_turma,
                data_matricula,
                status
            )
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            matricula.id_matricula,
            matricula.aluno.id_aluno,
            matricula.turma.id_turma,
            matricula.data_matricula,
            matricula.status
        ))

    conn.commit()
    conn.close()

def carregar_matriculas(alunos, turmas):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM matriculas")

    dados = cursor.fetchall()

    matriculas = []

    for linha in dados:

        aluno = next(
            (a for a in alunos if a.id_aluno == linha["id_aluno"]),
            None
        )

        turma = next(
            (t for t in turmas if t.id_turma == linha["id_turma"]),
            None
        )

        if aluno and turma:

            matricula = Matricula(
                aluno=aluno,
                turma=turma
            )

            matricula.id_matricula = linha["id_matricula"]
            matricula.data_matricula = linha["data_matricula"]
            matricula.status = linha["status"]

            matriculas.append(matricula)

    conn.close()

    return matriculas

def salvar_frequencias(lista_frequencias):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM frequencias")

    for freq in lista_frequencias:

        cursor.execute("""
            INSERT INTO frequencias
            (
                id_frequencia,
                id_aluno,
                id_turma,
                data,
                presente
            )
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            freq.id_frequencia,
            freq.aluno.id_aluno,
            freq.turma.id_turma,
            freq.data,
            freq.presente
        ))

    conn.commit()
    conn.close()

def carregar_frequencias(alunos, turmas):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM frequencias")

    dados = cursor.fetchall()

    frequencias = []

    for linha in dados:

        aluno = next(
            (a for a in alunos if a.id_aluno == linha["id_aluno"]),
            None
        )

        turma = next(
            (t for t in turmas if t.id_turma == linha["id_turma"]),
            None
        )

        if aluno and turma:

            freq = Frequencia(
                aluno=aluno,
                turma=turma,
                disciplina=None,
                data=linha["data"]
            )

            freq.id_frequencia = linha["id_frequencia"]
            freq.presente = linha["presente"]

            frequencias.append(freq)

    conn.close()

    return frequencias

def salvar_desempenhos(lista_desempenhos):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM desempenho")

    for des in lista_desempenhos:

        for nota in des.notas:

            cursor.execute("""
                INSERT INTO desempenho
                (
                    id_aluno,
                    id_disciplina,
                    valor,
                    tipo
                )
                VALUES (%s,%s,%s,%s)
            """,
            (
                des.aluno.id_aluno,
                des.disciplina.id_disciplina,
                nota["valor"],
                nota["tipo"]
            ))

    conn.commit()
    conn.close()

def carregar_desempenhos(alunos, turmas, disciplinas):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM desempenho")

    dados = cursor.fetchall()

    for aluno in alunos:
        aluno.desempenhos = []

    desempenhos=[]

    for linha in dados:

        aluno = next(
            (a for a in alunos if a.id_aluno == linha["id_aluno"]),
            None
        )

        disciplina = next(
            (d for d in disciplinas if d.id_disciplina == linha["id_disciplina"]),
            None
        )

        if aluno and disciplina:

            des = next(
                (
                    x for x in desempenhos
                    if x.aluno.id_aluno==aluno.id_aluno
                    and x.disciplina.id_disciplina==disciplina.id_disciplina
                ),
                None
            )

            if not des:

                des = Desempenho(aluno, disciplina)

                des.turma = next(
                    (
                        t for t in turmas
                        if hasattr(t, "disciplina")
                        and t.disciplina.id_disciplina == disciplina.id_disciplina
                    ),
                    None
                )

                des.id_desempenho = len(desempenhos)+1

                desempenhos.append(des)

            des.adicionar_nota(
                linha["valor"],
                linha["tipo"]
            )

            if not hasattr(aluno, "desempenhos"):
                aluno.desempenhos = []

            aluno.desempenhos.append(des)
         
    conn.close()

    return desempenhos