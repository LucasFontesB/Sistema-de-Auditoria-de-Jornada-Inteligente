import pdfplumber
import re

def extrair_dados_completos(pdf_path):
    registros = []
    incompletos = []
    nome = "Desconhecido"
    data_inicio = None
    data_fim = None

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            linhas = text.split("\n")

            for linha in linhas:

                # nome
                if "NOME:" in linha.upper():
                    match_nome = re.search(r'NOME:\s*(.*?)\s+PIS', linha, re.IGNORECASE)
                    if match_nome:
                        nome = match_nome.group(1).strip()

                # período
                if "DE" in linha and "ATÉ" in linha:
                    match_data = re.search(
                        r'DE\s*(\d{2}/\d{2}/\d{4})\s*ATÉ\s*(\d{2}/\d{2}/\d{4})',
                        linha
                    )
                    if match_data:
                        data_inicio = match_data.group(1)
                        data_fim = match_data.group(2)

                # registros
                if re.match(r'\d{2}/\d{2}/\d{2}', linha):
                    data = linha[:8]
                    horarios = re.findall(r'\d{2}:\d{2}', linha)

                    if horarios:
                        contagem = {}
                        for h in horarios:
                            contagem[h] = contagem.get(h, 0) + 1

                        duracao = None
                        for h, qtd in contagem.items():
                            if qtd == 1:
                                duracao = h
                                break

                        if duracao:
                            registros.append((data, duracao))
                        else:
                            incompletos.append(data)

    return nome, registros, incompletos, data_inicio, data_fim