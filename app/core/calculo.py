from datetime import datetime, timedelta
from collections import defaultdict
from datetime import datetime, timedelta

def classificar_funcionario(dados):
    score = 100

    total_min = dados["total"][0] * 60 + dados["total"][1]

    dias_trabalhados = len(dados["registros"])
    media_diaria = total_min / dias_trabalhados if dias_trabalhados else 0

    faltas = len(dados["faltas"])
    incompletos = len(dados["incompletos"])
    pouco_produtivos = len(dados["pouco_produtivos"])
    excedentes = len(dados["excedentes"])

    # 📉 Penalizações

    # faltas pesam MUITO
    score -= faltas * 10

    # registros incompletos
    score -= incompletos * 5

    # dias com baixa produtividade
    score -= pouco_produtivos * 3

    # excesso de horas (leve penalização)
    score -= excedentes * 2

    # média baixa (< 6h)
    if media_diaria < 360:
        score -= 10

    # trava score
    score = max(0, min(100, score))

    # 🏷️ classificação
    if score >= 90:
        nivel = "🏆 Excelente"
    elif score >= 75:
        nivel = "👍 Bom"
    elif score >= 60:
        nivel = "⚖️ Regular"
    elif score >= 40:
        nivel = "⚠️ Atenção"
    else:
        nivel = "🚨 Crítico"

    return {
        "score": score,
        "nivel": nivel,
        "media_diaria": int(media_diaria)
    }

def gerar_lista_dias(inicio, fim):
    dias = []
    atual = inicio

    while atual <= fim:
        dias.append(atual.strftime("%d/%m/%y"))
        atual += timedelta(days=1)

    return dias

def calcular_relatorio_completo(registros, incompletos, data_inicio, data_fim):
    total_minutos = 0
    dias_pouco_produtivos = []
    dias_excedentes = []
    semanas = defaultdict(int)

    inicio_periodo = datetime.strptime(data_inicio, "%d/%m/%Y")
    fim_periodo = datetime.strptime(data_fim, "%d/%m/%Y")

    for data_str, duracao in registros:
        horas, minutos = map(int, duracao.split(":"))
        minutos_total = horas * 60 + minutos

        data_obj = datetime.strptime(data_str, "%d/%m/%y")

        # 🔥 ignora fora do período (segurança)
        if not (inicio_periodo <= data_obj <= fim_periodo):
            continue

        total_minutos += minutos_total

        # 📅 semana original
        inicio_semana = data_obj - timedelta(days=data_obj.weekday())
        fim_semana = inicio_semana + timedelta(days=6)

        # ✂️ CORTE PELO PERÍODO
        inicio_ajustado = max(inicio_semana, inicio_periodo)
        fim_ajustado = min(fim_semana, fim_periodo)

        chave_semana = (
            inicio_ajustado.strftime("%d/%m/%Y"),
            fim_ajustado.strftime("%d/%m/%Y")
        )

        semanas[chave_semana] += minutos_total

        # ⚠️ pouco produtivo (< 4h)
        if minutos_total < 240:
            dias_pouco_produtivos.append((data_str, duracao))

        # 🔥 excedeu 8h
        if minutos_total > 480:
            dias_excedentes.append((data_str, duracao))

    inicio_periodo = datetime.strptime(data_inicio, "%d/%m/%Y")
    fim_periodo = datetime.strptime(data_fim, "%d/%m/%Y")

    todos_dias = set(gerar_lista_dias(inicio_periodo, fim_periodo))
    dias_com_registro = set([data for data, _ in registros])

    faltas = sorted(todos_dias - dias_com_registro)

    # 🧮 total
    total_horas = total_minutos // 60
    resto_minutos = total_minutos % 60

    carga_clt = 220 * 60
    diferenca = total_minutos - carga_clt

    carga_mensal_minutos = 220 * 60
    saldo_minutos = total_minutos - carga_mensal_minutos

    saldo_horas = abs(saldo_minutos) // 60
    saldo_restante = abs(saldo_minutos) % 60

    if saldo_minutos > 0:
        tipo_saldo = "positivo"
    elif saldo_minutos < 0:
        tipo_saldo = "negativo"
    else:
        tipo_saldo = "zerado"

    dados = {
        "total": (total_horas, resto_minutos),
        "faltas": faltas,
        "incompletos": incompletos,
        "pouco_produtivos": dias_pouco_produtivos,
        "excedentes": dias_excedentes,
        "registros": registros
    }

    dados_classificacao = classificar_funcionario(dados)

    return {
        "total": (total_horas, resto_minutos),
        "diferenca": diferenca,
        "semanas": semanas,
        "pouco_produtivos": dias_pouco_produtivos,
        "excedentes": dias_excedentes,
        "faltas": faltas,
        "incompletos": incompletos,
        "saldo_minutos": saldo_minutos,
        "avaliacao": dados_classificacao,
        "banco_horas": {
            "tipo": tipo_saldo,
            "horas": saldo_horas,
            "minutos": saldo_restante
        }
    }