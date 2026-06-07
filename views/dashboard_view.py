import streamlit as st


def mostrar_dashboard():
    usuario = st.session_state.get("usuario_logado")

    st.title("🏠 Dashboard")

    if usuario:
        st.markdown(
            f"### Bem-vindo(a), **{usuario.nome}**!"
        )

    st.markdown("Acompanhe abaixo um resumo geral do sistema.")

    st.markdown("---")

    # Métricas do sistema (dados reais do backend)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👤 Usuários", len(st.session_state.usuarios))
        st.metric("👩‍🎓 Alunos", len(st.session_state.alunos))

    with col2:
        st.metric("📘 Cursos", len(st.session_state.cursos))
        st.metric("📖 Disciplinas", len(st.session_state.disciplinas))

    with col3:
        st.metric("🏫 Turmas", len(st.session_state.turmas))
        st.metric("📝 Matrículas", len(st.session_state.matriculas))

    st.markdown("---")

    st.info(
        "Utilize o menu lateral para navegar entre as funcionalidades do sistema."
    )