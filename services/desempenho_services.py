from statistics import mean
from models.desempenho import Desempenho
from models.aluno import Aluno
from models.disciplina import Disciplina

class DesempenhoService:

    @staticmethod
    def registrar_nota(aluno: Aluno, turma, valor: float, tipo: str, lista_notas: list = None, **kwargs) -> Desempenho:
        # 1. Validação de escala
        if valor < 0 or valor > 100:
            raise ValueError("Nota deve estar entre 0 e 100.")

        if not hasattr(aluno, "desempenhos"):
            aluno.desempenhos = []

        # 3. Buscar desempenho existente
        desempenho = next(
            (d for d in lista_notas if d.aluno.id_aluno == aluno.id_aluno and d.turma.id_turma == turma.id_turma),
            None
        )

        # 4. Criar se não existir
        if not desempenho:
            disciplina = turma.disciplina if hasattr(turma, 'disciplina') else kwargs.get('disciplina')
            desempenho = Desempenho(aluno, disciplina)
            desempenho.turma = turma
            # GARANTE O ID PARA NÃO DAR ERRO NA TELA (image_47807c)
            desempenho.id_desempenho = len(lista_notas) + 1 if lista_notas is not None else 0
            
            if lista_notas is not None:
                lista_notas.append(desempenho)
            aluno.desempenhos.append(desempenho)

        desempenho.adicionar_nota(valor, tipo)
        return desempenho

    @staticmethod
    def calcular_media(desempenho: Desempenho) -> float:
        if not desempenho or not hasattr(desempenho, 'notas') or not desempenho.notas:
            return 0.0
        notas_normais = [n["valor"] for n in desempenho.notas if n.get("tipo") != "recuperacao"]
        return mean(notas_normais) if notas_normais else 0.0

    @staticmethod
    def definir_status(desempenho: Desempenho) -> str:
        media = DesempenhoService.calcular_media(desempenho)
        if media >= 70: return "Aprovado"
        elif 40 <= media < 70: return "Recuperação"
        return "Reprovado"