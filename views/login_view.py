import streamlit as st
from controllers.auth_controller import AuthController


def mostrar_login():
    st.title("🔐 Login")

    st.markdown("Acesse o sistema acadêmico utilizando suas credenciais.")

    # Campos de entrada
    cpf = st.text_input(
        "CPF",
        placeholder="Digite apenas números",
        max_chars=11
    )

    senha = st.text_input(
        "Senha",
        type="password",
        placeholder="Digite sua senha"
    )

    col1, col2 = st.columns(2)

    # Botão de login
    with col1:
        if st.button("Entrar", use_container_width=True):
            try:
                usuario = AuthController.login(
                    cpf,
                    senha,
                    st.session_state.usuarios
                )

                # Login bem-sucedido
                st.session_state.usuario_logado = usuario
                st.session_state.pagina_atual = "dashboard"
                st.success("Login realizado com sucesso!")
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

    # Botão para criar conta
    with col2:
        if st.button("Criar conta", use_container_width=True):
            st.session_state.pagina_atual = "cadastro"
            st.rerun()