from statistics import mean
from models.desempenho import Desempenho
from models.aluno import Aluno
from models.disciplina import Disciplina


class DesempenhoService:

    @staticmethod
    def registrar_nota(
        aluno: Aluno,
        disciplina: Disciplina,
        valor: float,
        tipo: str
    ) -> Desempenho:

        if valor < 0 or valor > 100:
            raise ValueError("Nota deve estar entre 0 e 100.")

        # Garantir que o aluno tenha lista de desempenhos
        if not hasattr(aluno, "desempenhos"):
            aluno.desempenhos = []

        # Buscar desempenho existente
        desempenho = next(
            (d for d in aluno.desempenhos if d.disciplina == disciplina),
            None
        )

        # Criar se não existir
        if not desempenho:
            desempenho = Desempenho(aluno, disciplina)
            aluno.desempenhos.append(desempenho)

        desempenho.adicionar_nota(valor, tipo)

        return desempenho

    @staticmethod
    def calcular_media(desempenho: Desempenho) -> float:
        if not desempenho.notas:
            return 0.0

        notas_normais = [
            n["valor"] for n in desempenho.notas
            if n["tipo"] != "recuperacao"
        ]

        if not notas_normais:
            return 0.0

        return mean(notas_normais)

    @staticmethod
    def definir_status(desempenho: Desempenho) -> str:
        media = DesempenhoService.calcular_media(desempenho)

        if media >= 70:
            return "Aprovado"
        elif 40 <= media < 70:
            return "Recuperação"
        else:
            return "Reprovado"