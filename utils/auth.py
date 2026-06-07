import streamlit as st
from functools import wraps

def login_required(func):
    """
    Decorador que bloqueia o acesso à página se o usuário não estiver logado.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Verifica se o usuário existe no session_state e não é None
        if not st.session_state.get("usuario_logado"):
            st.error("⚠️ Acesso Negado! Você precisa fazer login para ver esta página.")
            # O st.stop() para a execução do código aqui. Nada abaixo disso vai rodar.
            st.stop()
        
        # Se estiver logado, deixa a função original rodar normalmente
        return func(*args, **kwargs)
    return wrapper