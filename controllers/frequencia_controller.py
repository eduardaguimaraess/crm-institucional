from data import csv_repository

class FrequenciaController:

    @staticmethod
    def registrar_presenca(dados: dict, lista_frequencias: list):
        # O IMPORT FICA AQUI DENTRO!
        from services.frequencia_services import FrequenciaService
        
        try:
            aluno = dados.get("aluno")
            turma = dados.get("turma")
            data = dados.get("data")

            # Trava de duplicidade
            for freq in lista_frequencias:
                if (freq.aluno.id_aluno == aluno.id_aluno and 
                    freq.turma.id_turma == turma.id_turma and 
                    freq.data == data):
                    raise ValueError(f"O aluno {aluno.nome} já possui chamada registrada nesta data.")

            nova_freq = FrequenciaService.registrar_presenca(
                aluno=aluno, turma=turma, data=data,
                presente=dados.get("presente", True),
                lista_frequencias=lista_frequencias
            )
            csv_repository.salvar_frequencias(lista_frequencias)
            return nova_freq
        except Exception as e:
            raise Exception(f"Erro ao registrar presença: {str(e)}")

    @staticmethod
    def registrar_frequencia_lote(dados_lote: list, lista_frequencias: list):
        from services.frequencia_services import FrequenciaService
        try:
            registros_criados = []
            for dados in dados_lote:
                aluno = dados.get("aluno")
                data = dados.get("data")

                ja_existe = any(f.aluno.id_aluno == aluno.id_aluno and f.data == data for f in lista_frequencias)
                if ja_existe: continue

                nova_freq = FrequenciaService.registrar_presenca(
                    aluno=aluno, turma=dados.get("turma"), data=data,
                    presente=dados.get("presente", True),
                    lista_frequencias=lista_frequencias
                )
                registros_criados.append(nova_freq)
            
            csv_repository.salvar_frequencias(lista_frequencias)
            return registros_criados
        except Exception as e:
            raise Exception(f"Erro ao registrar lote: {str(e)}")