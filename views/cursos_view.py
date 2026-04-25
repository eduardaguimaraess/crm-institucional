import streamlit as st
from controllers.curso_controller import CursoController


def mostrar_cursos():
    st.title("📘 Gestão de Cursos")
    st.markdown("Cadastro, visualização e atualização de cursos.")
    st.markdown("---")

    cursos = st.session_state.cursos

    if cursos:
        st.subheader("📋 Cursos cadastrados")

        for curso in cursos:
            with st.expander(f"{curso.nome} | ID: {curso.id_curso}"):

                st.write(f"**Nome:** {curso.nome}")
                st.write(f"**Carga horária:** {curso.carga_horaria} horas")
                st.write(f"**Valor:** {curso.valor_formatado()}")
                st.write(f"**Status:** {'Ativo' if curso.ativo else 'Inativo'}")

                st.markdown("#### ✏️ Atualizar curso")

                with st.form(f"form_update_curso_{curso.id_curso}"):

                    nome = st.text_input("Nome", value=curso.nome)
                    carga_horaria = st.number_input(
                        "Carga horária (horas)",
                        min_value=1,
                        step=1,
                        value=int(curso.carga_horaria)
                    )
                    valor = st.number_input(
                        "Valor (R$)",
                        min_value=0.01,
                        step=0.01,
                        value=float(curso.valor)
                    )
                    ativo = st.checkbox("Curso ativo", value=curso.ativo)

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    dados_update = {
                        "id_curso": curso.id_curso,
                        "nome": nome,
                        "carga_horaria": carga_horaria,
                        "valor": valor,
                        "ativo": ativo
                    }

                    try:
                        CursoController.atualizar_curso(
                            dados_update,
                            st.session_state.cursos
                        )
                        st.success("Curso atualizado com sucesso!")
                        st.rerun()
                    except ValueError as e:
                        st.error(str(e))

    else:
        st.info("Nenhum curso cadastrado até o momento.")

    st.markdown("---")

    st.subheader("➕ Cadastrar novo curso")

    with st.form("form_cadastro_curso"):

        nome = st.text_input("Nome do curso")
        carga_horaria = st.number_input(
            "Carga horária (horas)",
            min_value=1,
            step=1
        )
        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            step=0.01
        )

        cadastrar = st.form_submit_button("Cadastrar curso")

    if cadastrar:
        if not nome:
            st.error("Preencha o nome do curso.")
            return

        novo_id = st.session_state.contador_cursos

        dados = {
            "id_curso": novo_id,
            "nome": nome,
            "carga_horaria": carga_horaria,
            "valor": valor
        }

        try:
            CursoController.cadastrar_curso(
                dados,
                st.session_state.cursos
            )
            st.session_state.contador_cursos += 1
            st.success("Curso cadastrado com sucesso!")
            st.rerun()
        except ValueError as e:
            st.error(str(e))