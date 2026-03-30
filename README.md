# 📊 Sistema de Auditoria de Jornada Inteligente







## 🚀 Sobre o Projeto

Sistema desktop desenvolvido para análise automatizada de espelhos de ponto eletrônico, com foco em auditoria de jornada, banco de horas e geração de insights para gestão de RH.

O objetivo é substituir análises manuais por um processo inteligente, rápido e confiável.

---
## 🔍 Descrição

Este projeto realiza:

- **📄 Leitura automática de arquivos PDF de ponto**
- **🧮 Cálculo de horas trabalhadas**
- **📊 Análise semanal de jornada**
- **⚠️ Identificação de inconsistências**
- **💰 Controle de banco de horas (mensal e acumulado)**
- **🏆 Classificação de desempenho do colaborador**
- **📑 Geração de relatórios profissionais em PDF**
- **💾 Armazenamento de histórico com SQLite**

**⚡ Ideal para equipes de RH, gestores e empresas que desejam controle total da jornada de trabalho.**

## 🧱 Tecnologias Utilizadas
- Python 3.12
- CustomTkinter (interface)
- SQLite (persistência)
- ReportLab (geração de PDF)
- pdfplumber (leitura de PDF)
### 📦 Pré-requisitos
- Python 3.10+
- pip instalado
- Ambiente virtual recomendado (.venv)

## ⚙️ Como executar
### 🔹 Clonar o projeto
```bash
- 1º git clone https://github.com/seu-repo/sistema-auditoria-jornada.git
- 2º cd sistema-auditoria-jornada
```
### 🔹 Instalar dependências
```bash
- 1º pip install -r requirements.txt
```
### 🔹 Executar aplicação
```bash
- 1º python main.py
```

## 🖥️ Interface

A aplicação possui interface gráfica moderna com CustomTkinter, permitindo:

- Seleção de arquivos PDF
- Visualização de resultados
- Consulta de histórico por colaborador
- Geração automática de relatórios
```
🏗 Estrutura do Projeto
app/
 ├── core/         # Regras de negócio
 ├── services/     # Processamento e lógica
 ├── database/     # SQLite
 ├── ui/           # Interface gráfica

data/
 ├── output/       # Relatórios gerados
 ```
## 📊 Funcionalidades de Auditoria


O sistema realiza análises como:

- 📅 Horas trabalhadas por semana
- ⚠️ Dias com baixa produtividade (<4h)
- 🔥 Dias com excesso de jornada (>8h)
- 🚨 Identificação de faltas
- ❗ Registros incompletos
- 💰 Cálculo de banco de horas
- 🧠 Classificação do Colaborador

**O sistema gera um score de desempenho (0 a 100) baseado em:**

- Presença
- Consistência
- Carga horária
- Produtividade

Classificações:

🏆 Excelente
👍 Bom
⚖️ Regular
⚠️ Atenção
🚨 Crítico
📑 Relatórios Gerados

Os relatórios são automaticamente salvos em:

data/output/

Formato:

relatorio_{nome}_{mes_ano}.pdf

Exemplo:

relatorio_HOZANO_PEREIRA_07_2025.pdf

## 🛠 Fluxo de Funcionamento
PDF → Parser → Cálculo → Banco de Dados → Classificação → Relatório PDF

## 🎯 Objetivos do Sistema
- Automatizar auditoria de jornada
- Reduzir erros manuais
- Gerar insights para RH
- Controlar banco de horas
- Melhorar tomada de decisão

## 🔮 Futuras melhorias
- 📊 Dashboard com gráficos
- 👥 Multiusuário
- 🌐 Versão web (SaaS)
- 📈 Ranking de colaboradores
- 🔗 Integração com folha de pagamento

### 👨‍💻 Autor

**Lucas Fontes**

📌 Versão

**1.0**

© Licença

Uso interno / projeto em desenvolvimento