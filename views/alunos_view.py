import streamlit as st
from datetime import date
from controllers.aluno_controller import AlunoController
from models.endereco import Endereco


def mostrar_alunos():
    st.title("👩‍🎓 Gestão de Alunos")
    st.markdown("Cadastro, visualização e atualização de alunos.")
    st.markdown("---")

    # ===============================
    # CONFIGURAÇÃO DE DATAS
    # ===============================
    hoje = date.today()
    data_minima = date(hoje.year - 100, hoje.month, hoje.day)

    # Garantir que a lista de alunos exista no session_state
    if 'alunos' not in st.session_state:
        st.session_state.alunos = []
    
    alunos = st.session_state.alunos

    # ==================================================
    # LISTAGEM E ATUALIZAÇÃO
    # ==================================================
    if alunos:
        st.subheader("📋 Alunos cadastrados")

        for aluno in alunos:
            with st.expander(f"{aluno.nome} | CPF: {aluno.cpf}"):

                st.write(f"**ID:** {aluno.id_aluno}")
                st.write(f"**Nome:** {aluno.nome}")
                st.write(f"**CPF:** {aluno.cpf}")
                st.write(f"**E-mail:** {aluno.email}")
                st.write(f"**Telefone:** {aluno.telefone}")
                st.write(f"**Gênero:** {aluno.genero}")
                st.write(f"**Data de nascimento:** {aluno.data_nascimento.strftime('%d/%m/%Y')}")
                st.write(f"**Responsável:** {aluno.responsavel}")
                st.write(f"**Status:** {aluno.status}")

                st.markdown("#### ✏️ Atualizar aluno")

                with st.form(f"form_update_{aluno.id_aluno}"):

                    nome_up = st.text_input("Nome", value=aluno.nome)
                    telefone_up = st.text_input("Telefone", value=aluno.telefone)
                    email_up = st.text_input("E-mail", value=aluno.email)

                    genero_up = st.selectbox(
                        "Gênero",
                        ["Masculino", "Feminino", "Outro"],
                        index=["Masculino", "Feminino", "Outro"].index(aluno.genero)
                        if aluno.genero in ["Masculino", "Feminino", "Outro"] else 0
                    )

                    data_nascimento_up = st.date_input(
                        "Data de nascimento",
                        value=aluno.data_nascimento,
                        min_value=data_minima,
                        max_value=hoje,
                        format="DD/MM/YYYY"
                    )

                    responsavel_up = st.text_input(
                        "Responsável",
                        value=aluno.responsavel
                    )

                    status_up = st.selectbox(
                        "Status",
                        ["Ativo", "Inativo"],
                        index=0 if aluno.status == "Ativo" else 1
                    )

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    # Ajuste 3: Validação Completa (Campos obrigatórios)
                    campos_update = [nome_up, telefone_up, email_up, responsavel_up]
                    if not all(campos_update):
                        st.error("Erro: Preencha todos os campos obrigatórios para atualização.")
                    else:
                        dados_update = {
                            "id_aluno": aluno.id_aluno,
                            "nome": nome_up,
                            "data_nascimento": data_nascimento_up,
                            "cpf": aluno.cpf,
                            "genero": genero_up,
                            "telefone": telefone_up,
                            "email": email_up,
                            "endereco": aluno.endereco,
                            "responsavel": responsavel_up,
                            "status": status_up
                        }

                        try:
                            AlunoController.atualizar_aluno(
                                dados_update,
                                st.session_state.alunos
                            )
                            st.success("Aluno atualizado com sucesso!")
                            # Ajuste 2: Limpeza e reset da View
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
        # Sanitização imediata para validação
        cpf = "".join(filter(str.isdigit, cpf_input))

        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")

        genero = st.selectbox(
            "Gênero",
            ["Masculino", "Feminino", "Outro"]
        )

        data_nascimento = st.date_input(
            "Data de nascimento",
            min_value=data_minima,
            max_value=hoje,
            format="DD/MM/YYYY"
        )

        responsavel = st.text_input("Responsável")

        cadastrar = st.form_submit_button("Cadastrar aluno")

    if cadastrar:
        # Ajuste 3: Validação Completa
        campos_cadastro = [nome, cpf, email, telefone, responsavel]
        
        if not all(campos_cadastro):
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif len(cpf) != 11:
            st.error("O CPF deve conter exatamente 11 dígitos numéricos.")
        else:
            # ===============================
            # GERAÇÃO DE IDS
            # ===============================
            novo_id = st.session_state.contador_alunos
            id_endereco = st.session_state.contador_enderecos

            endereco = Endereco(
                id_endereco=id_endereco,
                cep="00000000",
                logradouro="Não informado",
                numero="S/N",
                bairro="Não informado"
            )

            dados = {
                "id_aluno": novo_id,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cpf": cpf,
                "genero": genero,
                "telefone": telefone,
                "email": email,
                "endereco": endereco,
                "responsavel": responsavel
            }

            try:
                AlunoController.cadastrar_aluno(
                    dados,
                    st.session_state.alunos
                )
                st.session_state.contador_alunos += 1
                st.session_state.contador_enderecos += 1
                st.success("Aluno cadastrado com sucesso!")
                
                # Ajuste 2: Limpeza automática do formulário para o próximo uso
                st.rerun()
            except ValueError as e:
                st.error(str(e))