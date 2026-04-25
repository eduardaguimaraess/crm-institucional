import streamlit as st
from controllers.auth_controller import AuthController
from views.styles.style_loader import carregar_css

def mostrar_login():
    carregar_css("views/styles/theme.css")

    margem_esq, centro, margem_dir = st.columns([1, 2, 1])

    with centro:

        st.markdown("""
            <h1 style='text-align: center; font-size: 2.5rem;'>
                <i class="fas fa-book" style="color: #B861C6; margin-right: 10px;"></i>Login
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("Acesse o sistema acadêmico utilizando suas credenciais.")
        
        st.write("---")


        cpf = st.text_input("CPF", placeholder="000.000.000-00", max_chars=11)
        senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        st.write("") 
        c1, c2 = st.columns(2)

        with c1:
            if st.button("Entrar", use_container_width=True, type="primary"):
                try:
                    usuario = AuthController.login(cpf, senha, st.session_state.usuarios)
                    st.session_state.usuario_logado = usuario
                    st.session_state.pagina_atual = "dashboard"
                    st.success("Sucesso!")
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))

        with c2:
            if st.button("Criar conta", use_container_width=True):
                st.session_state.pagina_atual = "cadastro"
                st.rerun()