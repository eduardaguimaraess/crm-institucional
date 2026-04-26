from datetime import date
from models.frequencia import Frequencia
from models.aluno import Aluno
from models.disciplina import Disciplina
from models.turma import Turma


class FrequenciaService:

    @staticmethod
    def registrar_presenca(
        aluno: Aluno,
        turma: Turma,
        data: date = None,
        presente: bool = True,
        lista_frequencias: list = None,
        **kwargs  # Captura argumentos extras (como disciplina) para não quebrar
    ) -> Frequencia:
        """
        Cria o objeto de frequência e o registra tanto no Aluno quanto na lista Global.
        """
        data = data or date.today()

        # 1. GarantE que a lista de frequências no aluno exista (Memória Local)
        if not hasattr(aluno, "frequencias"):
            aluno.frequencias = []

        # 2. CriaR a instância da Frequencia
        # Busca a disciplina diretamente da turma para evitar inconsistência
        frequencia = Frequencia(
            aluno=aluno,
            turma=turma,
            disciplina=turma.disciplina if hasattr(turma, 'disciplina') else None,
            data=data
        )
        
        # 3. Definir status e ID
        frequencia.presente = presente
        
        # Gerar ID baseado na lista global, se fornecida
        if lista_frequencias is not None:
            novo_id = max([f.id_frequencia for f in lista_frequencias], default=0) + 1
            frequencia.id_frequencia = novo_id
            # Adiciona na lista global (Session State)
            lista_frequencias.append(frequencia)

        # 4. Adiciona na lista do objeto Aluno
        aluno.frequencias.append(frequencia)
        
        return frequencia

    @staticmethod
    def registrar_falta(
        aluno: Aluno,
        turma: Turma,
        data: date = None,
        lista_frequencias: list = None
    ) -> Frequencia:
        """
        Atalho para registrar falta reutilizando a lógica de presença.
        """
        return FrequenciaService.registrar_presenca(
            aluno=aluno,
            turma=turma,
            data=data,
            presente=False,
            lista_frequencias=lista_frequencias
        )

    @staticmethod
    def calcular_percentual(
        aluno: Aluno,
        turma: Turma = None
    ) -> float:
        """
        Calcula o percentual de presença baseado nas frequências registradas.
        """
        if not hasattr(aluno, "frequencias") or not aluno.frequencias:
            return 0.0

        # Filtrar registros por turma, se especificado
        registros = aluno.frequencias
        if turma:
            registros = [f for f in registros if f.turma.id_turma == turma.id_turma]

        if not registros:
            return 0.0

        presencas = [f for f in registros if f.presente]
        return (len(presencas) / len(registros)) * 100