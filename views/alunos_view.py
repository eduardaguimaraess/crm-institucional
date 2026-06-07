import streamlit as st
from datetime import date
from controllers.aluno_controller import AlunoController
from models.endereco import Endereco

def mostrar_alunos():
    st.title("Gestão de Alunos")
    st.markdown("Cadastro, visualização e atualização de alunos.")
    st.markdown("---")

    hoje = date.today()
    data_minima = date(hoje.year - 100, hoje.month, hoje.day)

    if 'alunos' not in st.session_state:
        st.session_state.alunos = []
    
    alunos = st.session_state.alunos

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO
    # ==================================================
    if alunos:
        st.subheader("Alunos cadastrados")

        for aluno in alunos:
            with st.expander(f"{aluno.nome} | CPF: {aluno.cpf}"):
                # Exibição dos dados
                st.write(f"**ID:** {aluno.id_aluno}")
                st.write(f"**Data de nascimento:** {aluno.data_nascimento.strftime('%d/%m/%Y')}")
                st.write(f"**Responsável:** {aluno.responsavel}")
                st.write(f"**Telefone:** {aluno.telefone}")

                st.markdown("#### Atualizar aluno")

                with st.form(f"form_update_{aluno.id_aluno}"):
                    nome_up = st.text_input("Nome", value=aluno.nome)
                    # AJUSTE 1: Limite de 11 caracteres na atualização
                    telefone_up = st.text_input("Telefone", value=aluno.telefone, max_chars=11)
                    email_up = st.text_input("E-mail", value=aluno.email)

                    genero_up = st.selectbox(
                        "Gênero", ["Masculino", "Feminino", "Outro"],
                        index=["Masculino", "Feminino", "Outro"].index(aluno.genero)
                        if aluno.genero in ["Masculino", "Feminino", "Outro"] else 0
                    )

                    data_nasc_up = st.date_input("Data de nascimento", value=aluno.data_nascimento,
                                                 min_value=data_minima, max_value=hoje, format="DD/MM/YYYY")

                    # AJUSTE 2: Lógica de maioridade na ATUALIZAÇÃO
                    idade_up = hoje.year - data_nasc_up.year - ((hoje.month, hoje.day) < (data_nasc_up.month, data_nasc_up.day))
                    
                    if idade_up >= 18:
                        st.info(f"Aluno maior de idade ({idade_up} anos). Responsável: O próprio.")
                        responsavel_up = "O próprio"
                    else:
                        responsavel_up = st.text_input("Responsável", value=aluno.responsavel if aluno.responsavel != "O próprio" else "")

                    status_up = st.selectbox("Status", ["Ativo", "Inativo"], index=0 if aluno.status == "Ativo" else 1)
                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    if not nome_up or not telefone_up or (idade_up < 18 and not responsavel_up):
                        st.error("Erro: Preencha todos os campos obrigatórios.")
                    else:
                        dados_update = {
                            "id_aluno": aluno.id_aluno, "nome": nome_up, "data_nascimento": data_nasc_up,
                            "cpf": aluno.cpf, "genero": genero_up, "telefone": telefone_up,
                            "email": email_up, "endereco": aluno.endereco, "responsavel": responsavel_up, "status": status_up
                        }
                        try:
                            AlunoController.atualizar_aluno(dados_update, st.session_state.alunos)
                            st.success("Aluno atualizado com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(str(e))
    else:
        st.info("Nenhum aluno cadastrado até o momento.")

    st.markdown("---")

    # ==================================================
    # CADASTRO DE NOVO ALUNO
    # ==================================================
    st.subheader("➕ Cadastrar novo aluno")

    with st.form("form_cadastro_aluno"):
        nome = st.text_input("Nome completo")
        cpf_input = st.text_input("CPF (apenas números)", max_chars=11)
        email = st.text_input("E-mail")
        
        # AJUSTE 3: Limite de 11 caracteres no cadastro
        telefone = st.text_input("Telefone (DDD + Número)", max_chars=11, help="Ex: 22999887766")

        genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])

        data_nascimento = st.date_input("Data de nascimento", min_value=data_minima, max_value=hoje, format="DD/MM/YYYY")

        # AJUSTE 4: Lógica de maioridade no CADASTRO
        idade_cad = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        
        if idade_cad >= 18:
            st.info(f"Aluno maior de idade ({idade_cad} anos). O responsável será definido como 'O próprio'.")
            responsavel = "O próprio"
            exibir_campo_resp = False
        else:
            responsavel = st.text_input("Nome do Responsável")
            exibir_campo_resp = True

        cadastrar = st.form_submit_button("Cadastrar aluno")

    if cadastrar:
        cpf = "".join(filter(str.isdigit, cpf_input))
        
        if not nome or not cpf or not telefone or (idade_cad < 18 and not responsavel):
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif len(cpf) != 11:
            st.error("O CPF deve conter exatamente 11 dígitos.")
        else:
            # Geração de IDs (usando session_state como você definiu)
            novo_id = st.session_state.get('contador_alunos', 1)
            id_endereco = st.session_state.get('contador_enderecos', 1)

            endereco = Endereco(id_endereco, "00000000", "Não informado", "S/N", "Não informado")

            dados = {
                "id_aluno": novo_id, "nome": nome, "data_nascimento": data_nascimento,
                "cpf": cpf, "genero": genero, "telefone": telefone,
                "email": email, "endereco": endereco, "responsavel": responsavel
            }

            try:
                AlunoController.cadastrar_aluno(dados, st.session_state.alunos)
                st.session_state.contador_alunos = novo_id + 1
                st.session_state.contador_enderecos = id_endereco + 1
                st.success("Aluno cadastrado com sucesso!")
                st.rerun()
            except ValueError as e:
                st.error(str(e))