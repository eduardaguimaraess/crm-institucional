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

                    nome = st.text_input("Nome", value=aluno.nome)
                    telefone = st.text_input("Telefone", value=aluno.telefone)
                    email = st.text_input("E-mail", value=aluno.email)

                    genero = st.selectbox(
                        "Gênero",
                        ["Masculino", "Feminino", "Outro"],
                        index=["Masculino", "Feminino", "Outro"].index(aluno.genero)
                        if aluno.genero in ["Masculino", "Feminino", "Outro"] else 0
                    )

                    data_nascimento = st.date_input(
                        "Data de nascimento",
                        value=aluno.data_nascimento,
                        min_value=data_minima,
                        max_value=hoje,
                        format="DD/MM/YYYY"
                    )

                    responsavel = st.text_input(
                        "Responsável",
                        value=aluno.responsavel
                    )

                    status = st.selectbox(
                        "Status",
                        ["Ativo", "Inativo"],
                        index=0 if aluno.status == "Ativo" else 1
                    )

                    atualizar = st.form_submit_button("Atualizar")

                if atualizar:
                    dados_update = {
                        "id_aluno": aluno.id_aluno,
                        "nome": nome,
                        "data_nascimento": data_nascimento,
                        "cpf": aluno.cpf,
                        "genero": genero,
                        "telefone": telefone,
                        "email": email,
                        "endereco": aluno.endereco,
                        "responsavel": responsavel,
                        "status": status
                    }

                    try:
                        AlunoController.atualizar_aluno(
                            dados_update,
                            st.session_state.alunos
                        )
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

        cpf = st.text_input("CPF", max_chars=11)
        cpf = "".join(filter(str.isdigit, cpf))

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
        # ===============================
        # VALIDAÇÕES
        # ===============================
        if not all([nome, cpf, email, telefone, responsavel]):
            st.error("Preencha todos os campos obrigatórios.")
            return

        if not cpf.isdigit():
            st.error("O CPF deve conter apenas números.")
            return

        if len(cpf) != 11:
            st.error("O CPF deve ter exatamente 11 números.")
            return

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
            st.rerun()
        except ValueError as e:
            st.error(str(e))