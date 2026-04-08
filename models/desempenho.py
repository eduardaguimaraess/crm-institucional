from datetime import date
from aluno import Aluno
from disciplina import Disciplina

class Desempenho:
    """Gerencia todas as notas de um aluno em uma disciplina e calcula status."""

    def __init__(self, aluno: Aluno, disciplina: Disciplina):
        self.aluno = aluno               
        self.disciplina = disciplina     
        self.notas = []                  
        self.media = 0.0                 
        self.status = "Sem notas"        

    def adicionar_nota(self, valor: float, tipo: str, data: date = None):
        """Adiciona uma nota normal (prova, trabalho, atividade) e atualiza média e status."""
        nota = {
            "valor": valor,
            "tipo": tipo.lower(),
            "data": data or date.today()
        }
        self.notas.append(nota)
        self._atualizar_media()

    def adicionar_nota_recuperacao(self, valor: float, data: date = None):
        """Adiciona nota de recuperação e atualiza média e status."""
        nota = {
            "valor": valor,
            "tipo": "recuperacao",
            "data": data or date.today()
        }
        self.notas.append(nota)
        self._atualizar_media(recuperacao=True)

    def _atualizar_media(self, recuperacao=False):
        """Calcula média e atualiza status com base nas regras."""
        # calcula média apenas das notas normais
        normais = [n["valor"] for n in self.notas if n["tipo"] != "recuperacao"]
        if normais:
            self.media = sum(normais) / len(normais)
        else:
            self.media = 0.0

        # se houver nota de recuperação, considera ela como média final
        if recuperacao:
            rec_nota = [n["valor"] for n in self.notas if n["tipo"] == "recuperacao"][-1]
            self.media = rec_nota

        # define status de acordo com média
        if self.media >= 70:
            self.status = "Aprovado"
        elif 40 <= self.media < 70:
            self.status = "Recuperação"
        else:
            self.status = "Reprovado"

    def exibir_notas(self):
        """Exibe todas as notas detalhadas, média e status."""
        for n in self.notas:
            print(f"{n['tipo'].capitalize()}({n['valor']}) em {n['data']}")
        print(f"Média: {self.media:.2f}")
        print(f"Status: {self.status}")