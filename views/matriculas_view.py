import streamlit as st
from controllers.matricula_controller import MatriculaController
from datetime import date

def mostrar_matriculas():
    st.title("📝 Matrículas")
    st.markdown("Realize e acompanhe matrículas de alunos em turmas.")
    st.markdown("---")

    # ==================================================
    # DADOS DO ESTADO
    # ==================================================
    alunos = st.session_state.get('alunos', [])
    turmas = st.session_state.get('turmas', [])
    matriculas = st.session_state.get('matriculas', [])

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO DE MATRÍCULAS
    # ==================================================
    st.subheader("📋 Matrículas realizadas")

    if matriculas:
        for m in matriculas:
            with st.expander(f"{m.aluno.nome} → {m.turma.nome} ({m.status})"):
                st.write(f"**Aluno:** {m.aluno.nome} (CPF: {m.aluno.cpf})")
                st.write(f"**Turma:** {m.turma.nome}")
                st.write(f"**Curso:** {m.turma.curso.nome if m.turma.curso else 'N/A'}")
                st.write(f"**Data da matrícula:** {m.data_matricula}")
                st.write(f"**Status atual:** {m.status}")

                # --- FORMULÁRIO DE EDIÇÃO DE STATUS ---
                st.markdown("#### ✏️ Alterar Status")
                with st.form(f"form_edit_mat_{m.id_matricula}"):
                    opcoes_status = ["Ativa", "Concluída", "Cancelada", "Trancada"]
                    try:
                        idx_status = opcoes_status.index(m.status)
                    except ValueError:
                        idx_status = 0
                        
                    status_up = st.selectbox("Novo Status", opcoes_status, index=idx_status)
                    btn_atualizar = st.form_submit_button("Salvar Alteração")

                if btn_atualizar:
                    dados_up = {
                        "id_matricula": m.id_matricula,
                        "status": status_up
                    }
                    try:
                        MatriculaController.atualizar_matricula(dados_up, st.session_state.matriculas)
                        st.success("Status atualizado!")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))
    else:
        st.info("Nenhuma matrícula realizada até o momento.")

    st.markdown("---")

    # ==================================================
    # CADASTRO DE NOVA MATRÍCULA
    # ==================================================
    st.subheader("➕ Realizar nova matrícula")

    if not alunos:
        st.warning("Cadastre alunos antes de realizar matrículas.")
        return

    if not turmas:
        st.warning("Cadastre turmas antes de realizar matrículas.")
        return

    with st.form("form_matricula"):
        aluno_sel = st.selectbox(
            "Selecionar Aluno",
            alunos,
            format_func=lambda a: f"{a.nome} ({a.cpf})"
        )

        # Filtra apenas turmas que estão Ativas para novas matrículas
        turmas_ativas = [t for t in turmas if t.status == "Ativa"]
        
        turma_sel = st.selectbox(
            "Selecionar Turma",
            turmas_ativas,
            format_func=lambda t: f"{t.nome} - {t.disciplina.nome if t.disciplina else ''}"
        )

        matricular = st.form_submit_button("Matricular aluno")

    if matricular:
        # Gerar ID único para a matrícula
        novo_id = st.session_state.get('contador_matriculas', 0)
        
        dados_nova_mat = {
            "id_matricula": novo_id,
            "aluno": aluno_sel,
            "turma": turma_sel,
            "data_matricula": date.today(),
            "status": "Ativa"
        }

        try:
            # O Controller agora cuida da criação e da persistência no CSV
            MatriculaController.realizar_matricula(
                dados_nova_mat,
                st.session_state.matriculas
            )

            # Sincronização de referências (Opcional, mas útil para lógica em memória)
            if not hasattr(aluno_sel, "matriculas"):
                aluno_sel.matriculas = []
            
            # O Controller já adicionou à lista global, mas podemos linkar no objeto
            st.session_state.contador_matriculas = novo_id + 1
            
            st.success(f"Matrícula de {aluno_sel.nome} realizada com sucesso!")
            st.rerun()

        except Exception as e:
            st.error(str(e))