# 📊 Sistema de Auditoria de Jornada Inteligente

---

## 🚀 Sobre o Projeto

O **Sistema de Auditoria de Jornada Inteligente** é uma aplicação desktop desenvolvida para automatizar a análise de espelhos de ponto eletrônico, eliminando processos manuais e trazendo **precisão, velocidade e inteligência** para o controle de jornada.

A solução transforma dados brutos em **insights acionáveis para o RH**, permitindo identificar inconsistências, controlar banco de horas e avaliar o desempenho dos colaboradores.

---

## 🎯 Principais Benefícios

- ⏱️ Redução drástica do tempo de auditoria  
- 📉 Diminuição de erros humanos  
- 📊 Visão estratégica da jornada de trabalho  
- 🧠 Análise inteligente de desempenho  
- 💰 Controle preciso de banco de horas  

---

## 🔍 O que o sistema faz

- 📄 Leitura automática de arquivos PDF de ponto  
- 🧮 Cálculo de horas trabalhadas  
- 📊 Análise semanal da jornada  
- ⚠️ Identificação de inconsistências  
- 💰 Controle de banco de horas (mensal e acumulado)  
- 🏆 Classificação de desempenho do colaborador  
- 📑 Geração de relatórios profissionais em PDF  
- 💾 Armazenamento de histórico com SQLite  

---

## 🧠 Classificação Inteligente

O sistema gera um **score de 0 a 100** com base em:

- Presença  
- Consistência  
- Carga horária  
- Produtividade  

### Classificações

| Score | Classificação |
|------|-------------|
| 90 - 100 | 🏆 Excelente |
| 75 - 89  | 👍 Bom |
| 60 - 74  | ⚖️ Regular |
| 40 - 59  | ⚠️ Atenção |
| 0 - 39   | 🚨 Crítico |

---

## 📊 Auditoria Automatizada

O sistema identifica automaticamente:

- 📅 Horas trabalhadas por semana  
- ⚠️ Dias com baixa produtividade (< 4h)  
- 🔥 Dias com excesso de jornada (> 8h)  
- 🚨 Faltas  
- ❗ Registros incompletos  
- 💰 Banco de horas  

---

## 📑 Relatórios Gerados

Os relatórios são salvos automaticamente em:
data/output/


### Formato


relatorio_{nome}_{mes_ano}.pdf


### Exemplo


relatorio_HOZANO_PEREIRA_07_2025.pdf


---

## ⚙️ Como Executar

### 🔹 1. Clonar o projeto

```bash
git clone https://github.com/seu-repo/sistema-auditoria-jornada.git
cd sistema-auditoria-jornada
```

### 🔹 2. Criar ambiente virtual (recomendado)
```bash
python -m venv .venv
```

# Linux/macOS
```bash
source .venv/bin/activate  
```

# Windows
```bash
.venv\Scripts\activate
```
### 🔹 3. Instalar dependências
```bash
pip install -r requirements.txt
```
### 🔹 4. Executar aplicação
```bash
python main.py
```

# 🖥️ Interface

Interface desktop moderna construída com CustomTkinter, permitindo:

Seleção de arquivos PDF
Visualização dos resultados
Consulta de histórico
Geração de relatórios

# 🏗️ Estrutura do Projeto

```
app/
 ├── core/         # Regras de negócio
 ├── services/     # Processamento e lógica
 ├── database/     # Persistência SQLite
 ├── ui/           # Interface gráfica

data/
 ├── output/       # Relatórios gerados
```

# 🔄 Fluxo de Processamento
PDF → Parser → Cálculo → Banco de Dados → Classificação → Relatório PDF

# 📚 Documentação

Documentação técnica detalhada disponível em:

- 📐 Arquitetura
- 🔄 Fluxo do Sistema
- 📏 Regras de Negócio
- 🎯 Objetivos do Sistema
- Automatizar auditoria de jornada
- Reduzir erros manuais
- Gerar insights para RH
- Controlar banco de horas
- Melhorar tomada de decisão
- 🔮 Roadmap (Futuras melhorias)
- 📊 Dashboard com gráficos
- 👥 Multiusuário
- 🌐 Versão Web (SaaS)
- 📈 Ranking de colaboradores
- 🔗 Integração com folha de pagamento

  
## 👨‍💻 Autor

Lucas Fontes

## 📌 Versão

1.0

## © Licença

Uso interno / projeto em desenvolvimento
