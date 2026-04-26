from services.frequencia_services import FrequenciaService
from data import csv_repository

class FrequenciaController:

    @staticmethod
    def registrar_presenca(dados: dict, lista_frequencias: list):
        """
        Registra uma única presença via Service e persiste no CSV.
        dados deve conter: {'aluno', 'turma', 'data', 'presente'}
        """
        try:
            # Integração Segura: Extraímos os dados para garantir que 
            # o Service receba exatamente o que espera.
            nova_freq = FrequenciaService.registrar_presenca(
                aluno=dados.get("aluno"),
                turma=dados.get("turma"),
                data=dados.get("data"),
                presente=dados.get("presente", True),
                lista_frequencias=lista_frequencias
            )
            
            # Persistência Física: Sincroniza a lista atualizada com o CSV
            csv_repository.salvar_frequencias(lista_frequencias)
            
            return nova_freq
        except Exception as e:
            # Repassa a exceção para ser exibida como st.error na View
            raise Exception(f"Erro no Controller ao registrar presença: {str(e)}")

    @staticmethod
    def registrar_frequencia_lote(dados_lote: list, lista_frequencias: list):
        """
        Registra uma lista de presenças (chamada da turma) de uma só vez.
        dados_lote: lista de dicionários [{'aluno', 'turma', 'data', 'presente'}, ...]
        """
        try:
            registros_criados = []
            for dados in dados_lote:
                # Reutiliza a lógica de criação do Service
                nova_freq = FrequenciaService.registrar_presenca(
                    aluno=dados.get("aluno"),
                    turma=dados.get("turma"),
                    data=dados.get("data"),
                    presente=dados.get("presente", True),
                    lista_frequencias=lista_frequencias
                )
                registros_criados.append(nova_freq)
            
            # Persistência: Salva no CSV uma única vez após o loop (Otimização)
            csv_repository.salvar_frequencias(lista_frequencias)
            
            return registros_criados
        except Exception as e:
            raise Exception(f"Erro no Controller ao registrar lote: {str(e)}")

    @staticmethod
    def listar_frequencias_por_turma(id_turma: int, lista_frequencias: list):
        """
        Filtra os registros de frequência de uma turma específica usando IDs.
        """
        return [
            f for f in lista_frequencias 
            if hasattr(f.turma, 'id_turma') and f.turma.id_turma == id_turma
        ]