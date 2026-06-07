import streamlit as st
from controllers.frequencia_controller import FrequenciaController
from datetime import date

def mostrar_frequencia():
    st.title("📅 Gestão de Frequência")
    st.markdown("Registro e acompanhamento de presença dos alunos.")
    st.markdown("---")

    # ==================================================
    # 1. CARREGAMENTO DE DADOS DO ESTADO
    # ==================================================
    alunos = st.session_state.get('alunos', [])
    matriculas = st.session_state.get('matriculas', [])
    frequencias = st.session_state.get('frequencias', [])

    if not alunos:
        st.warning("Cadastre alunos antes de acessar a frequência.")
        return

    # 2. SELEÇÃO DO ALUNO
    aluno_sel = st.selectbox(
        "Selecionar Aluno",
        alunos,
        format_func=lambda a: f"{a.nome} ({a.cpf})"
    )

    # ==================================================
    # 3. FILTRAR TURMAS ATIVAS (CORREÇÃO DE INTEGRAÇÃO POR CPF)
    # ==================================================
    turmas_do_aluno = []
    
    # Normalizamos o CPF para garantir que a busca seja idêntica ao CSV
    cpf_aluno_selecionado = str(aluno_sel.cpf).strip()

    for m in matriculas:
        # Comparamos por CPF e ID, ignorando se o objeto na memória é o mesmo
        mesmo_aluno = str(m.aluno.cpf).strip() == cpf_aluno_selecionado
        status_ativo = str(m.status).strip().lower() == "ativa"

        if mesmo_aluno and status_ativo:
            turmas_do_aluno.append(m.turma)

    if not turmas_do_aluno:
        st.error(f"O aluno **{aluno_sel.nome}** não possui matrículas com status 'Ativa'.")
        
        # Painel de diagnóstico para identificar o erro no CSV
        with st.expander("🔍 Diagnóstico: Por que o aluno não aparece?"):
            st.write(f"CPF selecionado na tela: `{cpf_aluno_selecionado}`")
            m_encontradas = [m for m in matriculas if str(m.aluno.cpf).strip() == cpf_aluno_selecionado]
            if m_encontradas:
                for m in m_encontradas:
                    st.write(f"📌 Turma: **{m.turma.nome}** | Status no CSV: `{m.status}`")
                    if m.status.lower() != "ativa":
                        st.info("Dica: O status precisa ser exatamente 'Ativa' para aparecer na frequência.")
            else:
                st.write("❌ Nenhuma matrícula encontrada para este CPF no sistema.")
        return

    # 4. SELEÇÃO DA TURMA E DATA
    col_t, col_d = st.columns(2)
    
    with col_t:
        turma_sel = st.selectbox(
            "Turma / Disciplina",
            turmas_do_aluno,
            format_func=lambda t: f"{t.nome} - {t.disciplina.nome if t.disciplina else 'Sem Disciplina'}"
        )
    
    with col_d:
        data_aula = st.date_input("Data da Aula", value=date.today())

    st.markdown("---")

    # ==================================================
    # 5. REGISTRO DE PRESENÇA / FALTA
    # ==================================================
    col1, col2 = st.columns(2)

    dados_freq = {
        "aluno": aluno_sel,
        "turma": turma_sel,
        "data": data_aula
    }

    with col1:
        if st.button("✅ Registrar Presença", use_container_width=True):
            try:
                dados_freq["presente"] = True
                FrequenciaController.registrar_presenca(dados_freq, frequencias)
                st.success(f"Presença de {aluno_sel.nome} registrada!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao registrar: {e}")

    with col2:
        if st.button("❌ Registrar Falta", use_container_width=True):
            try:
                dados_freq["presente"] = False
                FrequenciaController.registrar_presenca(dados_freq, frequencias)
                st.warning(f"Falta de {aluno_sel.nome} registrada.")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao registrar: {e}")

    st.markdown("---")

    # ==================================================
    # 6. HISTÓRICO VISUAL (COMPARAÇÃO POR CPF E ID)
    # ==================================================
    st.subheader(f"📊 Histórico: {aluno_sel.nome}")
    
    registros_aluno = [
        f for f in frequencias 
        if str(f.aluno.cpf).strip() == cpf_aluno_selecionado 
        and f.turma.id_turma == turma_sel.id_turma
    ]

    if registros_aluno:
        registros_aluno.sort(key=lambda x: x.data, reverse=True)
        
        for r in registros_aluno:
            cor = "#d4edda" if r.presente else "#f8d7da"
            texto_cor = "#155724" if r.presente else "#721c24"
            status = "PRESENTE" if r.presente else "FALTA"
            
            st.markdown(f"""
                <div style="background-color: {cor}; color: {texto_cor}; padding: 10px; 
                            border-radius: 5px; margin-bottom: 5px; border: 1px solid {texto_cor};">
                    <strong>{r.data.strftime('%d/%m/%Y')}</strong> - {status}
                </div>
            """, unsafe_allow_html=True)
            
        total = len(registros_aluno)
        presencas = sum(1 for r in registros_aluno if r.presente)
        perc = (presencas / total * 100) if total > 0 else 0
        st.sidebar.metric("Frequência Atual", f"{perc:.1f}%", f"{presencas}/{total}")
    else:
        st.info("Nenhum registro de frequência encontrado para esta disciplina.")