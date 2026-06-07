from models.frequencia import Frequencia

class FrequenciaService:
    @staticmethod
    def registrar_presenca(aluno, turma, data, presente, lista_frequencias):
        """Cria a instância de frequência e adiciona na lista da memória."""
        # Lógica simples de ID
        novo_id = len(lista_frequencias) + 1
        
        # Cria o objeto (Passamos a disciplina como None se a turma já tiver essa info)
        nova_freq = Frequencia(aluno=aluno, turma=turma, disciplina=None, data=data)
        nova_freq.id_frequencia = novo_id
        nova_freq.presente = presente
        
        lista_frequencias.append(nova_freq)
        return nova_freq