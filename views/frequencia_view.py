import streamlit as st
from controllers.frequencia_controller import FrequenciaController
from services.frequencia_services import FrequenciaService


def mostrar_frequencia():
    st.title("📅 Frequência")
    st.markdown("Registro e acompanhamento de presença dos alunos.")
    st.markdown("---")

    alunos = st.session_state.alunos
    turmas = st.session_state.turmas


    if not alunos:
        st.warning("Cadastre alunos antes de registrar frequência.")
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
        st.info("Este aluno ainda não está matriculado em nenhuma turma.")
        return

    turma, disciplina = st.selectbox(
        "Turma / Disciplina",
        disciplinas_aluno,
        format_func=lambda x: f"{x[0].nome} - {x[1].nome}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Registrar presença", use_container_width=True):
            FrequenciaController.registrar_presenca(
                aluno,
                turma,
                disciplina
            )
            st.success("Presença registrada com sucesso!")
            st.rerun()

    with col2:
        if st.button("❌ Registrar falta", use_container_width=True):
            FrequenciaService.registrar_falta(
                aluno,
                turma,
                disciplina
            )
            st.success("Falta registrada com sucesso!")
            st.rerun()

    st.markdown("---")

    st.subheader("📊 Histórico de Frequência")

    if hasattr(aluno, "frequencias"):
        registros = [
            f for f in aluno.frequencias
            if f.disciplina == disciplina
        ]

        if registros:
            for r in registros:
                status = "Presente" if r.presente else "Falta"
