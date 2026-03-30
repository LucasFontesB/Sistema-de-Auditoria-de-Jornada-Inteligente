import customtkinter as ctk
from tkinter import filedialog
from app.services.processador import processar_pdf_completo
from app.services.processador import obter_historico_funcionario
from PIL import Image
import customtkinter as ctk

# tema global
ctk.set_appearance_mode("dark")  # "light" ou "dark"
ctk.set_default_color_theme("blue")  # pode trocar depois

def iniciar_interface():

    def ver_historico():
        nome = label_nome.cget("text").replace("Colaborador: ", "")

        if nome and nome != "Nenhum":
            historico = obter_historico_funcionario(nome)
            label_resultado.configure(text=historico)

    def selecionar_pdf():
        caminho = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf")])

        if caminho:
            label_arquivo.configure(text=f"📂 {caminho}")

            resultado, nome = processar_pdf_completo(caminho)
            label_resultado.configure(text=f"PDF gerado com sucesso!\n{resultado}")
            label_nome.configure(text=f"Colaborador: {nome}")

    # janela principal
    janela = ctk.CTk()
    janela.iconbitmap("assets/Logo_com_fundo.ico")
    janela.title("Sistema de Gestão de Ponto")
    janela.geometry("700x600")

    # container principal
    container = ctk.CTkFrame(janela, corner_radius=15)
    container.pack(padx=20, pady=20, fill="both", expand=True)

    # ================= HEADER =================
    logo_img = ctk.CTkImage(
        light_image=Image.open("assets/logo_com_fundo.png"),
        dark_image=Image.open("assets/logo_com_fundo.png"),
        size=(70, 70)
    )

    header = ctk.CTkFrame(container, fg_color="transparent")
    header.pack(pady=10)

    logo_label = ctk.CTkLabel(header, image=logo_img, text="")
    logo_label.pack()

    titulo = ctk.CTkLabel(
        header,
        text="Sistema de Gestão de Ponto",
        font=ctk.CTkFont(size=22, weight="bold")
    )
    titulo.pack(pady=(5, 0))

    subtitulo = ctk.CTkLabel(
        header,
        text="Análise inteligente de jornada de trabalho",
        font=ctk.CTkFont(size=12)
    )
    subtitulo.pack()

    # ================= BOTÕES =================
    acoes_frame = ctk.CTkFrame(container, fg_color="transparent")
    acoes_frame.pack(pady=15)

    btn_pdf = ctk.CTkButton(
        acoes_frame,
        text="📂 Selecionar PDF",
        command=selecionar_pdf,
        height=40,
        width=200
    )
    btn_pdf.grid(row=0, column=0, padx=10)

    btn_historico = ctk.CTkButton(
        acoes_frame,
        text="📊 Ver Histórico",
        command=ver_historico,
        height=40,
        width=200
    )
    btn_historico.grid(row=0, column=1, padx=10)

    # ================= CARD ARQUIVO =================
    card_arquivo = ctk.CTkFrame(container, corner_radius=10)
    card_arquivo.pack(fill="x", padx=20, pady=5)

    label_arquivo_titulo = ctk.CTkLabel(
        card_arquivo,
        text="📁 Arquivo selecionado",
        font=ctk.CTkFont(weight="bold")
    )
    label_arquivo_titulo.pack(anchor="w", padx=10, pady=(5, 0))

    label_arquivo = ctk.CTkLabel(
        card_arquivo,
        text="Nenhum arquivo selecionado",
        wraplength=600
    )
    label_arquivo.pack(anchor="w", padx=10, pady=(0, 5))

    # ================= CARD COLABORADOR =================
    card_nome = ctk.CTkFrame(container, corner_radius=10)
    card_nome.pack(fill="x", padx=20, pady=5)

    label_nome_titulo = ctk.CTkLabel(
        card_nome,
        text="👤 Colaborador",
        font=ctk.CTkFont(weight="bold")
    )
    label_nome_titulo.pack(anchor="w", padx=10, pady=(5, 0))

    label_nome = ctk.CTkLabel(
        card_nome,
        text="Nenhum selecionado"
    )
    label_nome.pack(anchor="w", padx=10, pady=(0, 5))

    # ================= CARD RESULTADO =================
    card_resultado = ctk.CTkFrame(container, corner_radius=10)
    card_resultado.pack(fill="both", expand=True, padx=20, pady=10)

    label_resultado_titulo = ctk.CTkLabel(
        card_resultado,
        text="📊 Resultado da Análise",
        font=ctk.CTkFont(weight="bold")
    )
    label_resultado_titulo.pack(anchor="w", padx=10, pady=(5, 0))

    label_resultado = ctk.CTkLabel(
        card_resultado,
        text="Aguardando análise...",
        justify="left"
    )
    label_resultado.pack(anchor="w", padx=10, pady=(0, 10))

    janela.mainloop()