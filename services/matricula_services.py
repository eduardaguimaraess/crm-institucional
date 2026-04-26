from datetime import date
from models.matricula import Matricula
from models.aluno import Aluno
from models.turma import Turma


class MatriculaService:

    @staticmethod
    def realizar_matricula(
        id_matricula: int,
        aluno: Aluno,
        turma: Turma,
        data_matricula: date,
        lista_matriculas: list,
        status: str = "Ativa",
        **kwargs
    ) -> Matricula:
        """
        Realiza a matrícula validando regras de negócio e vinculando os objetos na memória.
        """
        # 1. Validação: Aluno precisa estar ativo
        if hasattr(aluno, "status") and aluno.status.lower() != "ativo":
            raise ValueError(f"O aluno {aluno.nome} não está ativo no sistema.")

        # 2. Validação: Turma precisa estar ativa
        if hasattr(turma, "status") and turma.status.lower() != "ativa":
            raise ValueError(f"A turma {turma.nome} não está ativa para novas matrículas.")

        # 3. Validação: Precisa haver vaga
        if turma.vagas <= 0:
            raise ValueError(f"Não há vagas disponíveis na turma {turma.nome}.")

        # 4. Validação: Verificar duplicidade (Evita aluno ter duas matrículas 'Ativas' na mesma turma)
        for m in lista_matriculas:
            if m.aluno.id_aluno == aluno.id_aluno and m.turma.id_turma == turma.id_turma:
                if m.status.lower() == "ativa":
                    raise ValueError(f"O aluno {aluno.nome} já possui uma matrícula ativa nesta turma.")

        # 5. Criar o objeto Matricula
        # Usando o construtor padrão da sua Model
        matricula = Matricula(aluno=aluno, turma=turma)
        matricula.id_matricula = id_matricula
        matricula.data_matricula = data_matricula
        matricula.status = status

        # 6. Atualizar estado físico da turma e VINCULAR referências
        turma.vagas -= 1
        
        # GARANTIA DE VÍNCULO: Adiciona a matrícula na lista interna da turma
        # Isso é o que permite que turma.possui_aluno(aluno) funcione na View
        if not hasattr(turma, 'matriculas'):
            turma.matriculas = []
        turma.matriculas.append(matricula)

        # Mantém compatibilidade com outros métodos de adicionar aluno que você possa ter
        if hasattr(turma, "adicionar_aluno"):
            turma.adicionar_aluno(aluno)

        # 7. Registrar na lista global de matrículas (para persistência e listagem)
        lista_matriculas.append(matricula)

        return matricula
    
    @staticmethod
    def atualizar_matricula(
        id_matricula: int,
        status: str,
        lista_matriculas: list,
        **kwargs
    ) -> Matricula:
        """
        Localiza a matrícula por ID e atualiza o status, gerenciando a devolução de vagas.
        """
        # 1. Localizar matrícula na lista global
        matricula = next(
            (m for m in lista_matriculas if m.id_matricula == id_matricula),
            None
        )

        if not matricula:
            raise ValueError(f"Matrícula ID {id_matricula} não encontrada no sistema.")

        # 2. Validar status permitido
        status_validos = ["Ativa", "Cancelada", "Concluída", "Trancada"]
        if status.capitalize() not in status_validos:
            raise ValueError(f"Status '{status}' é inválido. Use: {status_validos}")

        # 3. Lógica de devolução de vaga
        # Se a matrícula estava 'Ativa' e agora é 'Cancelada', a vaga volta para a turma
        status_antigo = matricula.status.lower()
        novo_status = status.lower()

        if status_antigo == "ativa" and novo_status == "cancelada":
            matricula.turma.vagas += 1
        
        # Se estava 'Cancelada' e volta a ser 'Ativa', consome a vaga de novo
        elif status_antigo == "cancelada" and novo_status == "ativa":
            if matricula.turma.vagas > 0:
                matricula.turma.vagas -= 1
            else:
                raise ValueError("Não há vagas disponíveis para reativar esta matrícula.")

        # 4. Atualizar o dado no objeto (refletirá em todas as listas por referência)
        matricula.status = status.capitalize()

        return matricula