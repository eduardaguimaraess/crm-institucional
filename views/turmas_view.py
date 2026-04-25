import streamlit as st
from controllers.turma_controller import TurmaController


def mostrar_turmas():
    st.title("🏫 Gestão de Turmas")
    st.markdown("Cadastro e visualização de turmas.")
    st.markdown("---")

    # ===============================
    # DADOS DO ESTADO
    # ===============================
    turmas = st.session_state.turmas
    cursos = st.session_state.cursos
    disciplinas = st.session_state.disciplinas
    usuarios = st.session_state.usuarios

    professores = [
        u for u in usuarios
        if hasattr(u, "cargo") and u.cargo == "Professor"
    ]

    # ===============================
    # LISTAGEM DE TURMAS
    # ===============================
    if turmas:
        st.subheader("📋 Turmas cadastradas")

        for turma in turmas:
            disciplina_nome = (
                turma.disciplina.nome
                if turma.disciplina is not None
                else "Sem disciplina"
            )

            with st.expander(f"{turma.nome} | {disciplina_nome}"):

                st.write(f"**Curso:** {turma.curso.nome}")
                st.write(f"**Disciplina:** {disciplina_nome}")
                st.write(f"**Professor:** {turma.professor.nome}")
                st.write(f"**Horário:** {turma.horario}")
                st.write(f"**Vagas disponíveis:** {turma.vagas}")
                st.write(f"**Status:** {turma.status}")

                st.markdown("**Alunos matriculados:**")
                if turma.alunos:
                    for aluno in turma.alunos:
                        st.write(f"- {aluno.nome} (CPF: {aluno.cpf})")
                else:
                    st.info("Nenhum aluno matriculado.")
    else:
        st.info("Nenhuma turma cadastrada.")

    st.markdown("---")

    # ===============================
    # CADASTRO DE NOVA TURMA
    # ===============================
    st.subheader("➕ Cadastrar nova turma")

    if not cursos:
        st.warning("Cadastre um curso antes de criar turmas.")
        return

    if not disciplinas:
        st.warning("Cadastre uma disciplina antes de criar turmas.")
        return

    if not professores:
        st.warning("Cadastre um professor antes de criar turmas.")
        return

    with st.form("form_cadastro_turma"):

        nome = st.text_input("Nome da turma")

        # Seleção de curso
        curso = st.selectbox(
            "Curso",
            cursos,
            format_func=lambda c: c.nome
        )

        # Filtra disciplinas PELO ID DO CURSO
        disciplinas_filtradas = [
            d for d in disciplinas
            if d.curso.id_curso == curso.id_curso
        ]

        if not disciplinas_filtradas:
            st.warning("Não há disciplinas cadastradas para este curso.")
            st.stop()

        # Selectbox de disciplina com KEY dependente do curso
        disciplina = st.selectbox(
            "Disciplina",
            disciplinas_filtradas,
            key=f"disciplina_{curso.id_curso}",
            format_func=lambda d: d.nome
        )

        professor = st.selectbox(
            "Professor",
            professores,
            format_func=lambda p: p.nome
        )

        horario = st.text_input(
            "Horário (ex: Segunda 19:00 - 21:00)"
        )

        vagas = st.number_input(
            "Número de vagas",
            min_value=1,
            step=1
        )

        cadastrar = st.form_submit_button("Cadastrar turma")

    # ===============================
    # SALVAR TURMA
    # ===============================
    if cadastrar:
        novo_id = st.session_state.contador_turmas

        dados = {
            "id_turma": novo_id,
            "nome": nome,
            "curso": curso,
            "disciplina": disciplina,
            "professor": professor,
            "horario": horario,
            "vagas": vagas
        }

        try:
            TurmaController.cadastrar_turma(
                dados,
                st.session_state.turmas
            )
            st.session_state.contador_turmas += 1
            st.success("Turma cadastrada com sucesso!")
            st.rerun()
        except ValueError as e:
            st.error(str(e))