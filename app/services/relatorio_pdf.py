from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os

def gerar_pdf(nome, dados, data_inicio):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    caminho_pasta = os.path.join(BASE_DIR, "data", "output")

    # 🧠 Nome do arquivo inteligente
    data_ref = datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%m_%Y")
    nome_limpo = nome.replace(" ", "_")
    nome_arquivo = f"relatorio_{nome_limpo}_{data_ref}.pdf"

    caminho_saida = os.path.join(caminho_pasta, nome_arquivo)

    doc = SimpleDocTemplate(caminho_saida, pagesize=A4)
    styles = getSampleStyleSheet()

    elementos = []

    # ================= HEADER =================
    logo = Image("assets/Logo_sem_fundo.png", width=80, height=80)

    elementos.append(logo)
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(
        "<b>Relatório Detalhado de Ponto Eletrônico</b>",
        styles['Title']
    ))

    elementos.append(Paragraph(
        f"Colaborador: <b>{nome}</b>",
        styles['Normal']
    ))

    elementos.append(Spacer(1, 15))

    # ================= RESUMO =================
    h, m = dados["total"]

    diff = dados["diferenca"]

    if diff > 0:
        diff_txt = f"+{diff//60:02d}:{diff%60:02d}"
    else:
        diff_txt = f"-{abs(diff)//60:02d}:{abs(diff)%60:02d}"

    banco = dados["banco_horas"]
    banco_txt = f"{banco['tipo']} ({banco['horas']:02d}:{banco['minutos']:02d})"

    tabela = Table([
        ["Total Trabalhado", "Diferença CLT", "Banco de Horas"],
        [f"{h:02d}:{m:02d}", diff_txt, banco_txt]
    ])

    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elementos.append(tabela)
    elementos.append(Spacer(1, 20))

    # ================= SEMANAS =================
    elementos.append(Paragraph("<b>Horas por Semana</b>", styles['Heading2']))

    for (inicio, fim), minutos in dados["semanas"].items():
        elementos.append(Paragraph(
            f"{inicio} à {fim}: <b>{minutos//60:02d}:{minutos%60:02d}</b>",
            styles['Normal']
        ))

    elementos.append(Spacer(1, 15))

    # ================= ALERTAS =================
    elementos.append(Paragraph("<b>Alertas de Jornada</b>", styles['Heading2']))

    elementos.append(Paragraph(
        f"Faltas: {len(dados['faltas'])} | "
        f"Incompletos: {len(dados['incompletos'])} | "
        f"Baixa Produtividade: {len(dados['pouco_produtivos'])}",
        styles['Normal']
    ))

    elementos.append(Spacer(1, 15))

    # ================= CLASSIFICAÇÃO =================
    avaliacao = dados["avaliacao"]

    elementos.append(Paragraph("<b>Classificação do Colaborador</b>", styles['Heading2']))
    elementos.append(Paragraph(f"Nível: {avaliacao['nivel']}", styles['Normal']))
    elementos.append(Paragraph(f"Score: {avaliacao['score']}/100", styles['Normal']))

    h = avaliacao["media_diaria"] // 60
    m = avaliacao["media_diaria"] % 60

    elementos.append(Paragraph(f"Média diária: {h:02d}:{m:02d}", styles['Normal']))

    elementos.append(Spacer(1, 20))

    # ================= SALDO ACUMULADO =================
    saldo_total = dados["saldo_acumulado"]

    h = abs(saldo_total) // 60
    m = abs(saldo_total) % 60

    if saldo_total > 0:
        saldo_txt = f"+{h:02d}:{m:02d}"
    elif saldo_total < 0:
        saldo_txt = f"-{h:02d}:{m:02d}"
    else:
        saldo_txt = "00:00"

    elementos.append(Paragraph(
        f"<b>Saldo acumulado:</b> {saldo_txt}",
        styles['Normal']
    ))

    elementos.append(Spacer(1, 30))

    # ================= RODAPÉ =================
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    elementos.append(Paragraph(
        f"Sistema-de-Auditoria-de-Jornada-Inteligente | v1.0 | Gerado em {agora}",
        styles['Normal']
    ))

    doc.build(elementos)

    return caminho_saida