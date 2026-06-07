import streamlit as st
from datetime import date
from controllers.usuario_controller import UsuarioController
from models.endereco import Endereco
from views.styles.style_loader import carregar_css

def mostrar_cadastro():
    carregar_css("views/styles/theme.css")

    margem_esq, centro, margem_dir = st.columns([0.5, 2, 0.5])

    with centro:
        st.markdown("""
            <h1 style='text-align: center;'>
                <i class="fas fa-pen-to-square" style="color: #B861C6; margin-right: 10px;"></i>Cadastro
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='text-align: center;'>Crie uma nova conta para acessar o sistema.</p>", unsafe_allow_html=True)

        hoje = date.today()
        data_minima = date(hoje.year - 100, hoje.month, hoje.day)

        with st.form("form_cadastro_usuario"):
            st.markdown("### <i class='fas fa-user' style='font-size: 1.2rem;'></i> Dados Pessoais", unsafe_allow_html=True)
            
            nome = st.text_input("Nome completo")
            
            col_doc1, col_doc2 = st.columns(2)
            with col_doc1:
                cpf = st.text_input("CPF", max_chars=11, placeholder="Apenas números")
            with col_doc2:
                data_nascimento = st.date_input("Nascimento", min_value=data_minima, max_value=hoje, format="DD/MM/YYYY")

            email = st.text_input("E-mail")
            
            col_pass1, col_pass2 = st.columns(2)
            with col_pass1:
                senha = st.text_input("Senha", type="password")
            with col_pass2:
                confirmar_senha = st.text_input("Confirmar senha", type="password")

            col_info1, col_info2 = st.columns(2)
            with col_info1:
                genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
            with col_info2:
                cargo = st.selectbox("Cargo", ["Professor", "Administrador", "Captador Comercial"])

            telefone = st.text_input("Telefone", placeholder="(DDD) 00000-0000", max_chars=15)

            st.markdown("### <i class='fas fa-location-dot' style='font-size: 1.2rem;'></i> Endereço", unsafe_allow_html=True)
            
            col_end1, col_end2 = st.columns([1, 2])
            with col_end1:
                cep = st.text_input("CEP", max_chars=8)
            with col_end2:
                logradouro = st.text_input("Logradouro (Rua/Avenida)")

            col_end3, col_end4 = st.columns([1, 2])
            with col_end3:
                numero = st.text_input("Número")
            with col_end4:
                bairro = st.text_input("Bairro")

            st.write("") 
            cadastrar = st.form_submit_button("Finalizar Cadastro", use_container_width=True)

        if cadastrar:
            cpf_limpo = ''.join(filter(str.isdigit, cpf))
            cep_limpo = ''.join(filter(str.isdigit, cep))

            if not all([nome, cpf_limpo, email, senha, telefone, genero, cargo, data_nascimento, cep_limpo, logradouro, numero, bairro]):
                st.error("Preencha todos os campos obrigatórios.")
            elif senha != confirmar_senha:
                st.error("As senhas não coincidem.")
            elif len(cpf_limpo) != 11:
                st.error("O CPF deve ter 11 números.")
            elif len(cep_limpo) != 8:
                st.error("O CEP deve ter 8 números.")
            else:
                try:
                    # Gerar IDs baseados no tamanho da lista atual para evitar duplicatas
                    id_novo = len(st.session_state.usuarios) + 1
                    
                    endereco_obj = Endereco(
                        id_endereco=id_novo,
                        cep=cep_limpo,
                        logradouro=logradouro,
                        numero=numero,
                        bairro=bairro
                    )

                    dados = {
                        "id_usuario": id_novo,
                        "nome": nome,
                        "cpf": cpf_limpo,
                        "email": email,
                        "senha": senha,
                        "data_nascimento": data_nascimento,
                        "genero": genero,
                        "telefone": telefone,
                        "cargo": cargo,
                        "endereco": endereco_obj
                    }

                    # O Controller agora salva no CSV e atualiza a memória
                    UsuarioController.cadastrar_usuario(dados, st.session_state.usuarios)
                    
                    st.success("Usuário cadastrado com sucesso!")
                    st.session_state.pagina_atual = "login"
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))

        if st.button("Voltar para login", use_container_width=True):
            st.session_state.pagina_atual = "login"
            st.rerun()