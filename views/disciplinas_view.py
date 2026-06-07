import streamlit as st
from controllers.disciplina_controller import DisciplinaController


def mostrar_disciplinas():
    st.title("📖 Gestão de Disciplinas")
    st.markdown("Cadastro e manutenção de disciplinas.")
    st.markdown("---")

    # Garante que as listas existam no estado da sessão
    if 'disciplinas' not in st.session_state:
        st.session_state.disciplinas = []
    if 'cursos' not in st.session_state:
        st.session_state.cursos = []
    if 'usuarios' not in st.session_state:
        st.session_state.usuarios = []

    disciplinas = st.session_state.disciplinas
    cursos = st.session_state.cursos
    usuarios = st.session_state.usuarios
    
    # Filtra apenas usuários com o cargo de Professor
    professores = [
        u for u in usuarios
        if hasattr(u, "cargo") and u.cargo == "Professor"
    ]

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO
    # ==================================================
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

                    nome_up = st.text_input("Nome", value=d.nome)
                
                    curso_index = next(
                        (i for i, c in enumerate(cursos) if c.id_curso == d.curso.id_curso),
                        0
                    )

                    curso_up = st.selectbox(
                        "Curso",
                        cursos,
                        index=curso_index,
                        format_func=lambda c: c.nome
                    )
                    
                    professor_index = next(
                        (i for i, p in enumerate(professores) if p.id_usuario == d.professor.id_usuario),
                        0
                    )

                    professor_up = st.selectbox(
                        "Professor",
                        professores,
                        index=professor_index,
                        format_func=lambda p: p.nome
                    )

                    carga_horaria_up = st.number_input(
                        "Carga horária",
                        min_value=1,
                        step=1,
                        value=d.carga_horaria
                    )

                    dia_semana_up = st.selectbox(
                        "Dia da semana",
                        ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"],
                        index=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"].index(d.dia_semana)
                    )

                    hora_inicio_up = st.text_input("Hora início", value=d.hora_inicio)
                    hora_fim_up = st.text_input("Hora fim", value=d.hora_fim)
                    ativa_up = st.checkbox("Disciplina ativa", value=d.ativa)

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    if not nome_up:
                        st.error("O nome da disciplina é obrigatório.")
                    else:
                        dados_update = {
                            "id_disciplina": d.id_disciplina,
                            "nome": nome_up,
                            "curso": curso_up,
                            "professor": professor_up,
                            "carga_horaria": carga_horaria_up,
                            "dia_semana": dia_semana_up,
                            "hora_inicio": hora_inicio_up,
                            "hora_fim": hora_fim_up,
                            "ativa": ativa_up
                        }

                        try:
                            DisciplinaController.atualizar_disciplina(
                                dados_update,
                                st.session_state.disciplinas
                            )
                            st.success("Disciplina atualizada com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(str(e))
    else:
        st.info("Nenhuma disciplina cadastrada até o momento.")

    st.markdown("---")

    # ==================================================
    # CADASTRO DE NOVA DISCIPLINA
    # ==================================================
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
        if not nome or not hora_inicio or not hora_fim:
            st.error("Preencha todos os campos obrigatórios.")
        else:
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