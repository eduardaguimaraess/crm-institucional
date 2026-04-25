import streamlit as st


def mostrar_sidebar():

    with st.sidebar:
        st.title("📚 Sistema Acadêmico")

        usuario = st.session_state.get("usuario_logado")

        if usuario:
            st.markdown(f"**Usuário logado:** {usuario.nome}")
            st.markdown("---")

        # Navegação principal
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.pagina_atual = "dashboard"

        if st.button("👩‍🎓 Alunos", use_container_width=True):
            st.session_state.pagina_atual = "alunos"

        if st.button("📘 Cursos", use_container_width=True):
            st.session_state.pagina_atual = "cursos"

        if st.button("📖 Disciplinas", use_container_width=True):
            st.session_state.pagina_atual = "disciplinas"

        if st.button("🏫 Turmas", use_container_width=True):
            st.session_state.pagina_atual = "turmas"

        if st.button("📝 Matrículas", use_container_width=True):
            st.session_state.pagina_atual = "matriculas"
            
        if st.button("📅 Frequência", use_container_width=True):
            st.session_state.pagina_atual = "frequencia"
            
        if st.button("📊 Desempenho", use_container_width=True):
            st.session_state.pagina_atual = "desempenho"

        st.markdown("---")

        # Logout
        if st.button("🚪 Sair", use_container_width=True):
            st.session_state.usuario_logado = None
            st.session_state.pagina_atual = "login"
            st.rerun()