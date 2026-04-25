import streamlit as st
from controllers.matricula_controller import MatriculaController


def mostrar_matriculas():
    st.title("📝 Matrículas")
    st.markdown("Realize e acompanhe matrículas de alunos em turmas.")
    st.markdown("---")

    alunos = st.session_state.alunos
    turmas = st.session_state.turmas
    matriculas = st.session_state.matriculas

    st.subheader("📋 Matrículas realizadas")

    if matriculas:
        for m in matriculas:
            with st.expander(
                f"{m.aluno.nome} → {m.turma.nome} ({m.status})"
            ):
                st.write(f"**Aluno:** {m.aluno.nome}")
                st.write(f"**Turma:** {m.turma.nome}")
                st.write(f"**Curso:** {m.turma.curso.nome}")
                st.write(f"**Data da matrícula:** {m.data_matricula}")
                st.write(f"**Status:** {m.status}")
    else:
        st.info("Nenhuma matrícula realizada até o momento.")

    st.markdown("---")

    st.subheader("➕ Realizar nova matrícula")

    if not alunos:
        st.warning("Cadastre alunos antes de realizar matrículas.")
        return

    if not turmas:
        st.warning("Cadastre turmas antes de realizar matrículas.")
        return

    with st.form("form_matricula"):

        aluno = st.selectbox(
            "Aluno",
            alunos,
            format_func=lambda a: f"{a.nome} ({a.cpf})"
        )

        turma = st.selectbox(
            "Turma",
            turmas,
            format_func=lambda t: f"{t.nome} - {t.disciplina.nome}"
        )

        matricular = st.form_submit_button("Matricular aluno")

    if matricular:
        try:

            matricula = MatriculaController.realizar_matricula(
                aluno,
                turma
            )

            st.session_state.matriculas.append(matricula)

            if not hasattr(aluno, "matriculas"):
                aluno.matriculas = []
            aluno.matriculas.append(matricula)

            if not hasattr(turma, "matriculas"):
                turma.matriculas = []
            turma.matriculas.append(matricula)

            st.success("Matrícula realizada com sucesso!")
            st.rerun()

        except ValueError as e:
            st.error(str(e))
