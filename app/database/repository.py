from app.database.db import conectar

def salvar_saldo(funcionario, mes, ano, saldo_minutos):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO banco_horas (funcionario, mes, ano, saldo_minutos)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(funcionario, mes, ano)
        DO UPDATE SET saldo_minutos = excluded.saldo_minutos
    """, (funcionario, mes, ano, saldo_minutos))

    conn.commit()
    conn.close()


def buscar_saldo_total(funcionario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(saldo_minutos)
        FROM banco_horas
        WHERE funcionario = ?
    """, (funcionario,))

    resultado = cursor.fetchone()[0]
    conn.close()

    return resultado if resultado else 0

def buscar_historico(funcionario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT mes, ano, saldo_minutos
        FROM banco_horas
        WHERE funcionario = ?
        ORDER BY ano, mes
    """, (funcionario,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

def formatar_historico(registros):
    linhas = []

    for mes, ano, saldo in registros:
        h = abs(saldo) // 60
        m = abs(saldo) % 60

        if saldo > 0:
            texto = f"{mes:02d}/{ano} → +{h:02d}:{m:02d}"
        elif saldo < 0:
            texto = f"{mes:02d}/{ano} → -{h:02d}:{m:02d}"
        else:
            texto = f"{mes:02d}/{ano} → 00:00"

        linhas.append(texto)

    return "\n".join(linhas)