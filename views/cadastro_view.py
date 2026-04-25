import streamlit as st
from datetime import date
from controllers.usuario_controller import UsuarioController
from models.endereco import Endereco


def mostrar_cadastro():
    st.title("📝 Cadastro de Usuário")
    st.markdown("Crie uma nova conta para acessar o sistema.")
    st.markdown("---")

    hoje = date.today()
    data_minima = date(hoje.year - 100, hoje.month, hoje.day)

    with st.form("form_cadastro_usuario"):

        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF", max_chars=11)
        cpf = ''.join(filter(str.isdigit, cpf))
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        confirmar_senha = st.text_input("Confirmar senha", type="password")

        data_nascimento = st.date_input(
            "Data de nascimento",
            min_value=data_minima,
            max_value=hoje,
            format="DD/MM/YYYY"

        )

        genero = st.selectbox(
            "Gênero",
            ["Masculino", "Feminino", "Outro"]
        )

        telefone = st.text_input("Telefone")

        cargo = st.selectbox(
            "Cargo",
            ["Aluno", "Professor", "Administrador"]
        )

        st.markdown("### Endereço")

        cep = st.text_input("CEP", max_chars=8)
        cep = ''.join(filter(str.isdigit, cep))
        logradouro = st.text_input("Logradouro (Rua/Avenida)")
        numero = st.text_input("Número")
        bairro = st.text_input("Bairro")

        cadastrar = st.form_submit_button("Cadastrar")

    if cadastrar:

        if not all([
            nome, cpf, email, senha, telefone, genero, cargo, data_nascimento,
            cep, logradouro, numero, bairro
        ]):
            st.error("Preencha todos os campos obrigatórios.")
            return

        if senha != confirmar_senha:
            st.error("As senhas não coincidem.")
            return
    
        if not cpf.isdigit():
            st.error("O CPF deve conter apenas números.")
            return

        if not cep.isdigit():
            st.error("O CEP deve conter apenas números.")
            return

        if len(cpf) != 11:
            st.error("O CPF deve ter exatamente 11 números.")
            return
        
        if len(cep) != 8:
            st.error("O CEP deve ter exatamente 8 números.")
            return

        id_usuario = st.session_state.contador_usuarios
        id_endereco = st.session_state.contador_enderecos

        endereco = Endereco(
            id_endereco=id_endereco,
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            bairro=bairro
        )

        dados = {
            "id_usuario": id_usuario,
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "senha": senha,
            "data_nascimento": data_nascimento,
            "genero": genero,
            "telefone": telefone,
            "cargo": cargo,
            "endereco": endereco
        }

        try:
            UsuarioController.cadastrar_usuario(
                dados,
                st.session_state.usuarios
            )

            st.session_state.contador_usuarios += 1
            st.session_state.contador_enderecos += 1

            st.success("Usuário cadastrado com sucesso!")
            st.session_state.pagina_atual = "login"
            st.rerun()

        except ValueError as erro:
            st.error(str(erro))

    if st.button("Voltar para login"):
        st.session_state.pagina_atual = "login"
        st.rerun()