from datetime import datetime
from app.core.parser import extrair_dados_completos
from app.core.calculo import calcular_relatorio_completo
from app.services.relatorio_pdf import gerar_pdf
from app.database.repository import salvar_saldo, buscar_saldo_total
from app.database.repository import buscar_historico, formatar_historico

def obter_historico_funcionario(nome):
    registros = buscar_historico(nome)
    return formatar_historico(registros)

def processar_pdf_completo(caminho_pdf):
    nome, registros, incompletos, data_inicio, data_fim = extrair_dados_completos(caminho_pdf)

    dados = calcular_relatorio_completo(
        registros,
        incompletos,
        data_inicio,
        data_fim
    )

    # 📅 pegar mês/ano do relatório
    data_inicio_dt = datetime.strptime(data_inicio, "%d/%m/%Y")
    mes = data_inicio_dt.month
    ano = data_inicio_dt.year

    # 💾 salvar saldo do mês
    salvar_saldo(nome, mes, ano, dados["saldo_minutos"])

    # 📊 saldo acumulado
    saldo_total = buscar_saldo_total(nome)

    dados["saldo_acumulado"] = saldo_total

    caminho_saida = gerar_pdf(
        nome,
        dados,
        data_inicio  # 🔥 AGORA CORRETO
    )

    return caminho_saida, nome