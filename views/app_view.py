#python -m streamlit run views/app_view.py

import streamlit as st

from views.state_view import inicializar_estado
from views.login_view import mostrar_login
from views.cadastro_view import mostrar_cadastro
from views.dashboard_view import mostrar_dashboard

from views.components.sidebar import mostrar_sidebar

from views.alunos_view import mostrar_alunos
from views.cursos_view import mostrar_cursos
from views.disciplinas_view import mostrar_disciplinas
from views.turmas_view import mostrar_turmas
from views.matriculas_view import mostrar_matriculas
from views.frequencia_view import mostrar_frequencia
from views.desempenho_view import mostrar_desempenho


def main():
    st.set_page_config(
        page_title="Sistema Acadêmico",
        layout="wide"
    )

    inicializar_estado()

    if not st.session_state.usuario_logado:
        pagina = st.session_state.pagina_atual

        if pagina == "cadastro":
            mostrar_cadastro()
        else:
            mostrar_login()

        return 

    mostrar_sidebar()

    pagina = st.session_state.get("pagina_atual", "dashboard")

    if pagina == "dashboard":
        mostrar_dashboard()
    elif pagina == "alunos":
        mostrar_alunos()
    elif pagina == "cursos":
        mostrar_cursos()
    elif pagina == "disciplinas":
        mostrar_disciplinas()
    elif pagina == "turmas":
        mostrar_turmas()
    elif pagina == "matriculas":
        mostrar_matriculas()
    elif pagina == "frequencia":
        mostrar_frequencia()
    elif pagina == "desempenho":
        mostrar_desempenho()
    else:
        mostrar_dashboard()


if __name__ == "__main__":
    main()