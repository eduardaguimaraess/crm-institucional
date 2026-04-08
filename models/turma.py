from curso import Curso
from professor import Professor
from aluno import Aluno
from disciplina import Disciplina 

class Turma:
    def __init__(self, id_turma, nome, curso, disciplina, professor, horario, limite_alunos):
        self.id = id_turma
        self.nome = nome
        self.curso = curso                 
        self.disciplina = disciplina        
        self.professor = professor          
        self.horario = horario              
        self.limite_alunos = limite_alunos  # limite máximo de alunos
        self.alunos = []                    # lista de objetos Aluno

    # Adicionar aluno na turma
    def adicionar_aluno(self, aluno):
        if len(self.alunos) < self.limite_alunos:
            if aluno not in self.alunos:
                self.alunos.append(aluno)  # adiciona o objeto aluno
                print(f"Aluno {aluno.nome} matriculado com sucesso!")
            else:
                print(f"Aluno {aluno.nome} já está matriculado.")
        else:
            print("Turma cheia!")

    # Remover aluno da turma
    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno.nome} removido da turma.")
        else:
            print(f"Aluno {aluno.nome} não encontrado na turma.")

    # Exibir dados da turma
    def exibir_dados(self):
        print(f"Turma: {self.nome}")
        print(f"Curso: {self.curso.nome}")
        print(f"Disciplina: {self.disciplina.nome}")
        print(f"Professor: {self.professor.nome}")
        print(f"Horário: {self.horario}")
        print("Alunos matriculados:")
        if not self.alunos:
            print("Nenhum aluno matriculado ainda.")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")