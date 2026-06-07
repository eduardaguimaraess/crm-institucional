import streamlit as st
from services.auth_services import AuthService

class AuthController:
    
    @staticmethod
    def login(cpf, senha):
        """
        Coordena o login. 
        Usa a lista de usuários que já deve estar no st.session_state.
        """
        try:
            # Pega a lista carregada do CSV que está na memória
            lista_usuarios = st.session_state.get('usuarios', [])
            
            # Chama o serviço para validar
            usuario_autenticado = AuthService.login(cpf, senha, lista_usuarios)
            
            # Se chegou aqui, deu certo: salva na sessão
            st.session_state.usuario_logado = usuario_autenticado
            return True, "Login realizado com sucesso!"
            
        except ValueError as e:
            # Captura o erro "CPF ou senha inválidos" do Service
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"