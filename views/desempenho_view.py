import streamlit as st
from controllers.desempenho_controller import DesempenhoController
from services.desempenho_services import DesempenhoService

def mostrar_desempenho():
    st.title("📊 Desempenho / Notas")
    st.markdown("Lançamento e acompanhamento das notas dos alunos.")
    st.markdown("---")

    # 1. CARREGAMENTO SEGURO DOS DADOS
    # Garantimos que as listas existam no state para evitar erros de AtributeError
    alunos = st.session_state.get('alunos', [])
    matriculas = st.session_state.get('matriculas', [])
    notas = st.session_state.get('notas', [])

    if not alunos:
        st.warning("Cadastre alunos antes de lançar notas.")
        return

    # 2. SELEÇÃO DO ALUNO
    aluno_sel = st.selectbox(
        "Selecionar Aluno",
        alunos,
        format_func=lambda a: f"{a.nome} ({a.cpf})"
    )

    # 3. FILTRAR TURMAS POR CPF (Blindagem contra recarregamento de memória)
    # Buscamos nas matrículas ativas para garantir que o vínculo seja encontrado via dado (CPF)
    cpf_busca = str(aluno_sel.cpf).strip()
    turmas_do_aluno = [
        m.turma for m in matriculas 
        if str(m.aluno.cpf).strip() == cpf_busca and m.status.lower() == "ativa"
    ]

    if not turmas_do_aluno:
        st.info(f"O aluno {aluno_sel.nome} não possui matrículas ativas em nenhuma turma.")
        return

    # 4. SELEÇÃO DA TURMA
    turma_sel = st.selectbox(
        "Turma / Disciplina",
        turmas_do_aluno,
        format_func=lambda t: f"{t.nome} - {t.disciplina.nome if t.disciplina else 'Sem Disciplina'}"
    )

    st.markdown("---")

    # 5. FORMULÁRIO DE LANÇAMENTO
    st.subheader("➕ Lançar Nota")
    
    with st.form("form_lancar_nota", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Nota ajustada para 0-10 conforme a regra de negócio padrão, 
            # mas você pode alterar max_value para 100 se preferir.
            valor_nota = st.number_input(
                "Nota (0 a 10)", 
                min_value=0.0, 
                max_value=10.0, 
                step=0.5
            )
        
        with col2:
            tipo_aval = st.selectbox(
                "Tipo de avaliação",
                ["Prova", "Trabalho", "Recuperação", "Atividade"]
            )

        submit = st.form_submit_button("Confirmar Lançamento", use_container_width=True)

        if submit:
            # Dicionário integrado com o que o Controller espera
            dados_nota = {
                "aluno": aluno_sel,
                "turma": turma_sel,
                "valor": valor_nota,
                "tipo": tipo_aval
            }
            
            try:
                # O Controller salvará no CSV e atualizará a lista 'notas' na memória
                DesempenhoController.lancar_nota(dados_nota, notas)
                st.success(f"Nota registrada para {aluno_sel.nome}!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao salvar nota: {e}")

    # 6. HISTÓRICO E BOLETIM (Visualização)
    st.markdown("---")
    st.subheader(f"📑 Boletim: {aluno_sel.nome}")
    
    # Filtra as notas existentes para este aluno e esta turma
    notas_filtradas = [
        n for n in notas 
        if str(n.aluno.cpf).strip() == cpf_busca and n.turma.id_turma == turma_sel.id_turma
    ]

    if notas_filtradas:
        # Exibe as notas em colunas
        cols = st.columns(len(notas_filtradas) if len(notas_filtradas) < 4 else 4)
        for desempenho in notas_filtradas:
            for nota in desempenho.notas:
                st.metric(label=nota["tipo"].capitalize(), value=f'{nota["valor"]:.1f}')

        # Cálculo da média via Service
        desempenho_atual = notas_filtradas[0]
        media = DesempenhoService.calcular_media(desempenho_atual)
        
        # Estilização da Situação
        cor = "green" if media >= 7.0 else "red"
        status = "APROVADO" if media >= 7.0 else "EM RECUPERAÇÃO"
        
        st.markdown(f"### Média Final: :{cor}[{media:.2f}]")
        st.markdown(f"**Situação:** :{cor}[{status}]")
    else:
        st.info("Nenhuma nota lançada para este aluno nesta disciplina.")