import streamlit as st
from controllers.desempenho_controller import DesempenhoController
from services.desempenho_services import DesempenhoService


def mostrar_desempenho():
    st.title("📊 Desempenho / Notas")
    st.markdown("Lançamento e acompanhamento das notas dos alunos.")
    st.markdown("---")

    alunos = st.session_state.alunos
    turmas = st.session_state.turmas

    if not alunos:
        st.warning("Cadastre alunos antes de lançar notas.")
        return

    aluno = st.selectbox(
        "Aluno",
        alunos,
        format_func=lambda a: f"{a.nome} ({a.cpf})"
    )

    disciplinas_aluno = []

    for turma in turmas:
        if turma.possui_aluno(aluno):
            disciplinas_aluno.append((turma, turma.disciplina))

    if not disciplinas_aluno:
        st.info("Este aluno não está matriculado em nenhuma disciplina.")
        return

    turma, disciplina = st.selectbox(
        "Turma / Disciplina",
        disciplinas_aluno,
        format_func=lambda x: f"{x[0].nome} - {x[1].nome}"
    )

    st.markdown("---")

    st.subheader("➕ Lançar nota")

    with st.form("form_lancar_nota"):

        valor = st.number_input(
            "Nota (0 a 100)",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        tipo = st.selectbox(
            "Tipo de avaliação",
            ["prova", "trabalho", "recuperacao"]
        )

