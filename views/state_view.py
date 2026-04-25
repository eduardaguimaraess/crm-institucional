import streamlit as st


def inicializar_estado():

    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if "pagina_atual" not in st.session_state:
        st.session_state.pagina_atual = "login"

    if "usuarios" not in st.session_state:
        st.session_state.usuarios = []

    if "alunos" not in st.session_state:
        st.session_state.alunos = []

    if "cursos" not in st.session_state:
        st.session_state.cursos = []

    if "disciplinas" not in st.session_state:
        st.session_state.disciplinas = []

    if "turmas" not in st.session_state:
        st.session_state.turmas = []

    if "matriculas" not in st.session_state:
        st.session_state.matriculas = []

    if "frequencias" not in st.session_state:
        st.session_state.frequencias = []

    if "desempenhos" not in st.session_state:
        st.session_state.desempenhos = []
        
    if "contador_alunos" not in st.session_state:
        st.session_state.contador_alunos = 1
    
    if "contador_cursos" not in st.session_state:
        st.session_state.contador_cursos = 1
        
    if "contador_disciplinas" not in st.session_state:
        st.session_state.contador_disciplinas = 1

    if "professores" not in st.session_state:
        st.session_state.professores = []

    if "contador_turmas" not in st.session_state:
        st.session_state.contador_turmas = 1
