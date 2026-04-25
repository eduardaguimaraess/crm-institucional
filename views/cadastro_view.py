import streamlit as st
from controllers.usuario_controller import UsuarioController


def mostrar_cadastro():
    st.title("📝 Cadastro de Usuário")
    st.markdown("Crie uma nova conta para acessar o sistema.")

    # Formulário de cadastro
    with st.form("form_cadastro_usuario"):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF", max_chars=11, placeholder="Somente números")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        confirmar_senha = st.text_input("Confirmar senha", type="password")

        cargo = st.selectbox(
            "Cargo",
            ["Aluno", "Professor", "Administrador"]
        )

        submeter = st.form_submit_button("Cadastrar")

    # Processamento do cadastro
    if submeter:
        if not nome or not cpf or not email or not senha:
            st.error("Preencha todos os campos obrigatórios.")
            return

        if senha != confirmar_senha:
            st.error("As senhas não coincidem.")
            return

        dados = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "senha": senha,
            "cargo": cargo
        }

        try:
            UsuarioController.cadastrar_usuario(
                dados,
                st.session_state.usuarios
            )

            st.success("Usuário cadastrado com sucesso!")
            st.session_state.pagina_atual = "login"
            st.rerun()

        except ValueError as erro:
            st.error(str(erro))

    # Voltar para login
    if st.button("Voltar para Login"):
        st.session_state.pagina_atual = "login"
        st.rerun()