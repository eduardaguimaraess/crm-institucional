from services.desempenho_services import DesempenhoService
from data import csv_repository

class DesempenhoController:

    @staticmethod
    def lancar_nota(dados: dict, lista_notas: list):
        """
        Registra a nota no aluno, na lista global e persiste no arquivo CSV.
        dados deve conter: {'aluno', 'turma', 'valor', 'tipo'}
        """
        try:
            # 1. Chama o Service para validação e criação do objeto
            # Passamos os dados explicitamente para evitar erros de desempacotamento
            nova_nota = DesempenhoService.registrar_nota(
                aluno=dados.get("aluno"),
                turma=dados.get("turma"),
                valor=dados.get("valor"),
                tipo=dados.get("tipo"),
                lista_notas=lista_notas
            )
            
            # 2. Persistência Física: Sincroniza a lista com o CSV
            # Certifique-se de que esta função existe no seu csv_repository
            csv_repository.salvar_notas(lista_notas)
            
            return nova_nota
            
        except Exception as e:
            # Repassa o erro (ex: nota > 10) para ser exibido na View
            raise Exception(f"Erro ao lançar nota: {str(e)}")

    @staticmethod
    def calcular_media_aluno(aluno, turma):
        """
        Retorna a média formatada do aluno em uma turma específica.
        """
        return DesempenhoService.calcular_media(aluno, turma)