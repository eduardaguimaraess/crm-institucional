import streamlit as st
from data.csv_repository import (
    carregar_usuarios,
    carregar_alunos,
    carregar_cursos,
    carregar_disciplinas,
    carregar_turmas,
    carregar_matriculas,
    carregar_frequencias,
    carregar_desempenhos
)



def inicializar_estado():

    # ===============================
    # CARGA DOS DADOS (CSV)
    # ===============================
    if "usuarios" not in st.session_state:
        st.session_state.usuarios = carregar_usuarios()

    if "alunos" not in st.session_state:
        st.session_state.alunos = carregar_alunos()

    if "cursos" not in st.session_state:
        st.session_state.cursos = carregar_cursos()

    if "disciplinas" not in st.session_state:
        st.session_state.disciplinas = carregar_disciplinas(
            st.session_state.cursos,
            st.session_state.usuarios
        )

    if "turmas" not in st.session_state:
        st.session_state.turmas = carregar_turmas(
            st.session_state.cursos,
            st.session_state.disciplinas,
            st.session_state.usuarios
        )

    if "matriculas" not in st.session_state:
        st.session_state.matriculas = carregar_matriculas(
            st.session_state.alunos,
            st.session_state.turmas
        )

    # ==================================================
    # 🔗 LIGAR MATRÍCULAS AOS ALUNOS E TURMAS (AJUSTE CHAVE)
    # ==================================================
    for aluno in st.session_state.alunos:
        aluno.matriculas = []

    for turma in st.session_state.turmas:
        turma.matriculas = []

    for matricula in st.session_state.matriculas:
        matricula.aluno.matriculas.append(matricula)
        matricula.turma.matriculas.append(matricula)

    # ===============================
    # FREQUÊNCIAS
    # ===============================
    if "frequencias" not in st.session_state:
        st.session_state.frequencias = carregar_frequencias(
            st.session_state.alunos,
            st.session_state.turmas,
            st.session_state.disciplinas
        )

    # Garantia de lista
    if not isinstance(st.session_state.frequencias, list):
        st.session_state.frequencias = [st.session_state.frequencias]

    # ===============================
    # DESEMPENHOS
    # ===============================
    if "desempenhos" not in st.session_state:
        st.session_state.desempenhos = carregar_desempenhos(
            st.session_state.alunos,
            st.session_state.turmas,
            st.session_state.disciplinas
        )

    # ===============================
    # NAVEGAÇÃO / LOGIN
    # ===============================
    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if "pagina_atual" not in st.session_state:
        st.session_state.pagina_atual = "login"

    # ===============================
    # CONTADORES
    # ===============================
    if "contador_usuarios" not in st.session_state:
        st.session_state.contador_usuarios = (
            max((u.id_usuario for u in st.session_state.usuarios), default=0) + 1
        )

    if "contador_alunos" not in st.session_state:
        st.session_state.contador_alunos = (
            max((a.id_aluno for a in st.session_state.alunos), default=0) + 1
        )

    if "contador_cursos" not in st.session_state:
        st.session_state.contador_cursos = (
            max((c.id_curso for c in st.session_state.cursos), default=0) + 1
        )

    if "contador_disciplinas" not in st.session_state:
        st.session_state.contador_disciplinas = (
            max((d.id_disciplina for d in st.session_state.disciplinas), default=0) + 1
        )

    if "contador_turmas" not in st.session_state:
        st.session_state.contador_turmas = (
            max((t.id_turma for t in st.session_state.turmas), default=0) + 1
        )

    if "contador_matriculas" not in st.session_state:
        st.session_state.contador_matriculas = (
            max((m.id_matricula for m in st.session_state.matriculas), default=0) + 1
        )

    if "contador_frequencias" not in st.session_state:
        st.session_state.contador_frequencias = (
            max((f.id_frequencia for f in st.session_state.frequencias), default=0) + 1
        )

    if "contador_desempenhos" not in st.session_state:
        st.session_state.contador_desempenhos = (
            max((d.id_desempenho for d in st.session_state.desempenhos), default=0) + 1
        )

    if "contador_enderecos" not in st.session_state:
        st.session_state.contador_enderecos = (
            max(
                [u.endereco.id_endereco for u in st.session_state.usuarios] +
                [a.endereco.id_endereco for a in st.session_state.alunos],
                default=0
            ) + 1
        )
