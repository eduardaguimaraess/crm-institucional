from statistics import mean
from models.desempenho import Desempenho
from models.aluno import Aluno
from models.disciplina import Disciplina

class DesempenhoService:

    @staticmethod
    def registrar_nota(
        aluno: Aluno,
        turma, # Adicionado para alinhar com o Controller
        valor: float,
        tipo: str,
        lista_notas: list = None, # Para persistência global se necessário
        **kwargs # Blindagem contra argumentos extras
    ) -> Desempenho:
        
        # 1. Validação de escala (0 a 100 conforme sua View)
        if valor < 0 or valor > 100:
            raise ValueError("Nota deve estar entre 0 e 100.")

        # 2. Garantir que o aluno tenha lista de desempenhos
        if not hasattr(aluno, "desempenhos"):
            aluno.desempenhos = []

        # 3. Buscar desempenho existente por Disciplina (vinda da Turma)
        disciplina = turma.disciplina if hasattr(turma, 'disciplina') else kwargs.get('disciplina')
        
        desempenho = next(
            (d for d in aluno.desempenhos if d.disciplina == disciplina),
            None
        )

        # 4. Criar objeto de desempenho se não existir para essa disciplina
        if not desempenho:
            desempenho = Desempenho(aluno, disciplina)
            aluno.desempenhos.append(desempenho)

        # 5. Adicionar a nota (Ajuste o método na sua Model Desempenho se necessário)
        desempenho.adicionar_nota(valor, tipo)
        
        # 6. Sincronização opcional com lista global de notas (Session State)
        if lista_notas is not None:
            # Se sua lista global espera objetos Nota, você os adicionaria aqui.
            # Se ela espera os objetos Desempenho, adicionamos o desempenho.
            if desempenho not in lista_notas:
                lista_notas.append(desempenho)

        return desempenho

    @staticmethod
    def calcular_media(desempenho: Desempenho) -> float:
        if not desempenho or not hasattr(desempenho, 'notas') or not desempenho.notas:
            return 0.0

        # Filtra notas que não são de recuperação para a média normal
        notas_normais = [
            n["valor"] for n in desempenho.notas
            if n.get("tipo") != "recuperacao"
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