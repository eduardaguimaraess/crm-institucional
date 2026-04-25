from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

# Não precisamos de Base aqui porque essa classe não vira tabela no banco
class GradePDF:
    def __init__(self, disciplinas, nome_curso):
        self.disciplinas = disciplinas
        self.nome_curso = nome_curso

    def gerar_pdf(self, arquivo="grade.pdf"):
        c = canvas.Canvas(arquivo, pagesize=A4)
        largura, altura = A4

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(largura / 2, altura - 50, f"Grade Semanal - {self.nome_curso}")

        # Tabela
        dias = ["HORÁRIO", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        horarios = ["18:00-19:50", "20:10-22:00"]
        data = []

        for h in horarios:
            linha = [h]
            for dia in dias[1:]:
                # Filtra as disciplinas que batem com o dia e horário
                disc = [
                    d.nome for d in self.disciplinas 
                    if d.dia_semana == dia and f"{d.hora_inicio}-{d.hora_fim}" == h
                ]
                linha.append(disc[0] if disc else "")
            data.append(linha)

        tabela = Table([dias] + data, colWidths=[70] + [80]*5, rowHeights=30)
        tabela.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#4B89DC")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#D9E6F5")),
        ]))

        tabela.wrapOn(c, largura, altura)
        tabela.drawOn(c, 50, altura - 300)

        c.save()
        print(f"PDF gerado: {arquivo}")