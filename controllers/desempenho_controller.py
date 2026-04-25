from services.desempenho_services import DesempenhoService

class DesempenhoController:

    @staticmethod
    def lancar_nota(aluno, disciplina, valor, tipo):
        return DesempenhoService.registrar_nota(
            aluno, disciplina, valor, tipo
        )