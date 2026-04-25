from models.curso import Curso
from models.professor import Professor

class Disciplina:

    def __init__(self, id_disciplina, nome, curso, professor,
                 carga_horaria, dia_semana, hora_inicio, hora_fim, ativa=True):

        self.id_disciplina = id_disciplina
        self.nome = nome
        self.curso = curso
        self.professor = professor
        self.carga_horaria = carga_horaria
        self.dia_semana = dia_semana      # Ex: "Segunda"
        self.hora_inicio = hora_inicio    # Ex: "19:00"
        self.hora_fim = hora_fim          # Ex: "21:00"
        self.ativa = ativa

    # Retorna horário formatado
    def horario_formatado(self):
        return f"{self.dia_semana} {self.hora_inicio} - {self.hora_fim}"