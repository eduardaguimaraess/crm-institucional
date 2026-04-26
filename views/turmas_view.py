import streamlit as st
from controllers.turma_controller import TurmaController


def mostrar_turmas():
    st.title("🏫 Gestão de Turmas")
    st.markdown("Cadastro e visualização de turmas.")
    st.markdown("---")

    # ==================================================
    # DADOS DO ESTADO
    # ==================================================
    if 'turmas' not in st.session_state:
        st.session_state.turmas = []
    if 'cursos' not in st.session_state:
        st.session_state.cursos = []
    if 'disciplinas' not in st.session_state:
        st.session_state.disciplinas = []
    if 'usuarios' not in st.session_state:
        st.session_state.usuarios = []
    if 'matriculas' not in st.session_state:
        st.session_state.matriculas = []

    turmas = st.session_state.turmas
    cursos = st.session_state.cursos
    disciplinas = st.session_state.disciplinas
    usuarios = st.session_state.usuarios
    matriculas = st.session_state.matriculas

    # Professores são usuários com cargo "Professor"
    professores = [
        u for u in usuarios
        if hasattr(u, "cargo") and u.cargo == "Professor"
    ]

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO DAS TURMAS
    # ==================================================
    if turmas:
        st.subheader("📋 Turmas cadastradas")

        for turma in turmas:
            disciplina_nome = (
                turma.disciplina.nome
                if turma.disciplina is not None
                else "Sem disciplina"
            )

            with st.expander(f"{turma.nome} | {disciplina_nome}"):

                st.write(f"**Curso:** {turma.curso.nome}")
                st.write(f"**Disciplina:** {disciplina_nome}")
                st.write(f"**Professor:** {turma.professor.nome}")
                st.write(f"**Horário:** {turma.horario}")
                st.write(f"**Vagas disponíveis:** {turma.vagas}")
                st.write(f"**Status atual:** {turma.status}")

                # --- ÁREA DE EDIÇÃO ---
                st.markdown("#### ✏️ Editar Turma")
                with st.form(f"form_update_turma_{turma.id_turma}"):
                    nome_up = st.text_input("Nome da turma", value=turma.nome)
                    
                    try:
                        prof_idx = professores.index(turma.professor)
                    except (ValueError, AttributeError):
                        prof_idx = 0

                    professor_up = st.selectbox(
                        "Professor", 
                        professores, 
                        index=prof_idx, 
                        format_func=lambda p: p.nome,
                        key=f"sel_prof_{turma.id_turma}"
                    )
                    
                    horario_up = st.text_input("Horário", value=turma.horario)
                    vagas_up = st.number_input("Vagas", min_value=1, value=turma.vagas)
                    
                    # Lista expandida para evitar erro de index com 'Inativa' ou outros
                    opcoes_status = ["Ativa", "Inativa", "Encerrada", "Cancelada"]
                    try:
                        status_idx = opcoes_status.index(turma.status)
                    except ValueError:
                        status_idx = 0

                    status_up = st.selectbox(
                        "Status",
                        opcoes_status,
                        index=status_idx
                    )

                    btn_atualizar = st.form_submit_button("Salvar Alterações")

                if btn_atualizar:
                    dados_up = {
                        "id_turma": turma.id_turma,
                        "nome": nome_up,
                        "curso": turma.curso,
                        "disciplina": turma.disciplina,
                        "professor": professor_up,
                        "horario": horario_up,
                        "vagas": vagas_up,
                        "status": status_up
                    }
                    try:
                        TurmaController.atualizar_turma(dados_up, st.session_state.turmas)
                        st.success("Turma atualizada com sucesso!")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))

                # ==========================================
                # ALUNOS MATRICULADOS
                # ==========================================
                st.markdown("---")
                st.markdown("**Alunos matriculados:**")

                alunos_matriculados = [
                    m.aluno
                    for m in matriculas
                    if hasattr(m, "turma") and m.turma.id_turma == turma.id_turma and m.status == "Ativa"
                ]

                if alunos_matriculados:
                    for aluno in alunos_matriculados:
                        st.write(f"- {aluno.nome} (CPF: {aluno.cpf})")
                else:
                    st.info("Nenhum aluno matriculado.")
    else:
        st.info("Nenhuma turma cadastrada.")

    st.markdown("---")

    # ==================================================
    # CADASTRO DE NOVA TURMA
    # ==================================================
    st.subheader("➕ Cadastrar nova turma")

    if not cursos:
        st.warning("Cadastre um curso antes de criar turmas.")
        return

    if not disciplinas:
        st.warning("Cadastre uma disciplina antes de criar turmas.")
        return

    if not professores:
        st.warning("Cadastre um professor antes de criar turmas.")
        return

    # Campos fora do form para manter a reatividade da filtragem
    nome_novo = st.text_input("Nome da nova turma")

    curso_novo = st.selectbox(
        "Selecionar Curso",
        cursos,
        format_func=lambda c: c.nome,
        key="new_turma_curso_sel"
    )

    disciplinas_filtradas = [
        d for d in disciplinas
        if d.curso.id_curso == curso_novo.id_curso
    ]

    if not disciplinas_filtradas:
        st.warning("Não há disciplinas para este curso.")
    else:
        disciplina_nova = st.selectbox(
            "Selecionar Disciplina",
            disciplinas_filtradas,
            format_func=lambda d: d.nome,
            key="new_turma_disc_sel"
        )

        professor_novo = st.selectbox(
            "Selecionar Professor",
            professores,
            format_func=lambda p: p.nome,
            key="new_turma_prof_sel"
        )

        horario_novo = st.text_input("Horário", key="new_turma_horario")
        vagas_nova = st.number_input("Número de vagas", min_value=1, step=1, value=20)

        # Form apenas para o botão de submissão
        with st.form("form_cadastro_turma"):
            cadastrar = st.form_submit_button("Confirmar Cadastro")

        if cadastrar:
            if not nome_novo or not horario_novo:
                st.error("Preencha todos os campos obrigatórios.")
            else:
                dados_cadastro = {
                    "id_turma": st.session_state.get('contador_turmas', 0),
                    "nome": nome_novo,
                    "curso": curso_novo,
                    "disciplina": disciplina_nova,
                    "professor": professor_novo,
                    "horario": horario_novo,
                    "vagas": vagas_nova,
                    "status": "Ativa"
                }

                try:
                    TurmaController.cadastrar_turma(
                        dados_cadastro,
                        st.session_state.turmas
                    )
                    st.session_state.contador_turmas += 1
                    st.success("Turma cadastrada!")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))