import streamlit as st
from controllers.curso_controller import CursoController


def mostrar_cursos():
    st.title("📘 Gestão de Cursos")
    st.markdown("Cadastro, visualização e atualização de cursos.")
    st.markdown("---")

    # Garante que a lista de cursos exista no estado da sessão
    if 'cursos' not in st.session_state:
        st.session_state.cursos = []

    cursos = st.session_state.cursos

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO
    # ==================================================
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

                    nome_up = st.text_input("Nome", value=curso.nome)
                    carga_horaria_up = st.number_input(
                        "Carga horária (horas)",
                        min_value=1,
                        step=1,
                        value=int(curso.carga_horaria)
                    )
                    valor_up = st.number_input(
                        "Valor (R$)",
                        min_value=0.01,
                        step=0.01,
                        value=float(curso.valor)
                    )
                    ativo_up = st.checkbox("Curso ativo", value=curso.ativo)

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    if not nome_up:
                        st.error("O nome do curso é obrigatório para atualização.")
                    else:
                        # No UPDATE, o campo ativo é necessário
                        dados_update = {
                            "id_curso": curso.id_curso,
                            "nome": nome_up,
                            "carga_horaria": carga_horaria_up,
                            "valor": valor_up,
                            "ativo": ativo_up
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

    # ==================================================
    # CADASTRO DE NOVO CURSO
    # ==================================================
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
        else:
            novo_id = st.session_state.contador_cursos

            # CORREÇÃO: Removido 'ativo' para não dar erro no CursoService.cadastrar_curso
            dados_cadastro = {
                "id_curso": novo_id,
                "nome": nome,
                "carga_horaria": carga_horaria,
                "valor": valor
            }

            try:
                CursoController.cadastrar_curso(
                    dados_cadastro,
                    st.session_state.cursos
                )
                st.session_state.contador_cursos += 1
                st.success("Curso cadastrado com sucesso!")
                st.rerun()
            except ValueError as e:
                st.error(str(e))