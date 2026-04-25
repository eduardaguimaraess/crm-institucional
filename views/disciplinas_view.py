import streamlit as st
from controllers.disciplina_controller import DisciplinaController


def mostrar_disciplinas():
    st.title("📖 Gestão de Disciplinas")
    st.markdown("Cadastro e manutenção de disciplinas.")
    st.markdown("---")

    disciplinas = st.session_state.disciplinas
    cursos = st.session_state.cursos
    usuarios = st.session_state.usuarios
    professores = [
        u for u in usuarios
        if hasattr(u, "cargo") and u.cargo == "Professor"
    ]

    if disciplinas:
        st.subheader("📋 Disciplinas cadastradas")

        for d in disciplinas:
            with st.expander(f"{d.nome} — {d.curso.nome}"):

                st.write(f"**Curso:** {d.curso.nome}")
                st.write(f"**Professor:** {d.professor.nome}")
                st.write(f"**Carga horária:** {d.carga_horaria}h")
                st.write(f"**Horário:** {d.horario_formatado()}")
                st.write(f"**Status:** {'Ativa' if d.ativa else 'Inativa'}")

                st.markdown("#### ✏️ Atualizar disciplina")

                with st.form(f"form_update_disciplina_{d.id_disciplina}"):

                    nome = st.text_input("Nome", value=d.nome)

                    curso = st.selectbox(
                        "Curso",
                        cursos,
                        icurso_index = next(
                            (i for i, c in enumerate(cursos) if c.id_curso == d.curso.id_curso),
                            0
                        ),

                        format_func=lambda c: c.nome
                    )

                    professor = st.selectbox(
                        "Professor",
                        professores,
                        index=professores.index(d.professor),
                        format_func=lambda p: p.nome
                    )

                    carga_horaria = st.number_input(
                        "Carga horária",
                        min_value=1,
                        step=1,
                        value=d.carga_horaria
                    )

                    dia_semana = st.selectbox(
                        "Dia da semana",
                        ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"],
                        index=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"].index(d.dia_semana)
                    )

                    hora_inicio = st.text_input("Hora início", value=d.hora_inicio)
                    hora_fim = st.text_input("Hora fim", value=d.hora_fim)
                    ativa = st.checkbox("Disciplina ativa", value=d.ativa)

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    dados = {
                        "id_disciplina": d.id_disciplina,
                        "nome": nome,
                        "curso": curso,
                        "professor": professor,
                        "carga_horaria": carga_horaria,
                        "dia_semana": dia_semana,
                        "hora_inicio": hora_inicio,
                        "hora_fim": hora_fim,
                        "ativa": ativa
                    }

                    try:
                        DisciplinaController.atualizar_disciplina(
                            dados,
                            st.session_state.disciplinas
                        )
                        st.success("Disciplina atualizada com sucesso!")
                        st.rerun()
                    except ValueError as e:
                        st.error(str(e))
    else:
        st.info("Nenhuma disciplina cadastrada até o momento.")

    st.markdown("---")

    st.subheader("➕ Cadastrar nova disciplina")

    if not cursos:
        st.warning("Cadastre um curso antes de criar disciplinas.")
        return

    if not professores:
        st.warning("Cadastre um professor antes de criar disciplinas.")
        return

    with st.form("form_cadastro_disciplina"):

        nome = st.text_input("Nome da disciplina")

        curso = st.selectbox(
            "Curso",
            cursos,
            format_func=lambda c: c.nome
        )

        professor = st.selectbox(
            "Professor",
            professores,
            format_func=lambda p: p.nome
        )

        carga_horaria = st.number_input(
            "Carga horária",
            min_value=1,
            step=1
        )

        dia_semana = st.selectbox(
            "Dia da semana",
            ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        )

        hora_inicio = st.text_input("Hora início (ex: 19:00)")
        hora_fim = st.text_input("Hora fim (ex: 21:00)")

        cadastrar = st.form_submit_button("Cadastrar disciplina")

    if cadastrar:
        novo_id = st.session_state.contador_disciplinas

        dados = {
            "id_disciplina": novo_id,
            "nome": nome,
            "curso": curso,
            "professor": professor,
            "carga_horaria": carga_horaria,
            "dia_semana": dia_semana,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim
        }

        try:
            DisciplinaController.cadastrar_disciplina(
                dados,
                st.session_state.disciplinas
            )
            st.session_state.contador_disciplinas += 1
            st.success("Disciplina cadastrada com sucesso!")
            st.rerun()
        except ValueError as e:
            st.error(str(e))