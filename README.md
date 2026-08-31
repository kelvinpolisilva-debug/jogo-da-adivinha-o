import tkinter as tk
import random


# -----------------------------
# VARIÁVEIS DO JOGO
# -----------------------------

numero_secreto = 0
tentativas = 0
limite = 20


# -----------------------------
# JANELA
# -----------------------------

janela = tk.Tk()

janela.title("Jogo de Adivinhação")
janela.geometry("450x500")


# -----------------------------
# TÍTULO
# -----------------------------

titulo = tk.Label(
    janela,
    text="JOGO DE ADIVINHAÇÃO",
    font=("Arial", 20)
)

titulo.pack(pady=20)


# -----------------------------
# NOME DO JOGADOR
# -----------------------------

texto_nome = tk.Label(
    janela,
    text="Digite seu nome:"
)

texto_nome.pack()


campo_nome = tk.Entry(
    janela,
    font=("Arial", 14)
)

campo_nome.pack(pady=5)


# -----------------------------
# DIFICULDADE
# -----------------------------

texto_dificuldade = tk.Label(
    janela,
    text="Escolha a dificuldade:"
)

texto_dificuldade.pack(pady=10)


dificuldade = tk.StringVar()
dificuldade.set("Fácil")


menu_dificuldade = tk.OptionMenu(
    janela,
    dificuldade,
    "Fácil",
    "Médio",
    "Difícil"
)

menu_dificuldade.pack()


# -----------------------------
# CAMPO DO PALPITE
# -----------------------------

texto_palpite = tk.Label(
    janela,
    text="Digite seu palpite:"
)

texto_palpite.pack(pady=15)


campo_palpite = tk.Entry(
    janela,
    font=("Arial", 16),
    justify="center"
)

campo_palpite.pack()


# -----------------------------
# RESULTADO
# -----------------------------

resultado = tk.Label(
    janela,
    text="Digite seu nome e clique em INICIAR.",
    font=("Arial", 12)
)

resultado.pack(pady=20)


# -----------------------------
# FUNÇÃO PARA INICIAR O JOGO
# -----------------------------

def iniciar_jogo():
    global numero_secreto
    global tentativas
    global limite

    tentativas = 0

    nivel = dificuldade.get()

    if nivel == "Fácil":
        limite = 20

    elif nivel == "Médio":
        limite = 50

    else:
        limite = 100

    numero_secreto = random.randint(1, limite)

    resultado.config(
        text="Jogo iniciado!\nAdivinhe um número entre 1 e " + str(limite)
    )


# -----------------------------
# FUNÇÃO PARA VERIFICAR PALPITE
# -----------------------------

def verificar_palpite():
    global tentativas

    if numero_secreto == 0:
        resultado.config(
            text="Primeiro clique em INICIAR JOGO!"
        )
        return

    try:
        palpite = int(campo_palpite.get())
    except ValueError:
        resultado.config(
            text="Digite um número válido!"
        )
        campo_palpite.delete(0, tk.END)
        return

    if palpite < 1 or palpite > limite:
        resultado.config(
            text=f"Digite um número entre 1 e {limite}!"
        )
        campo_palpite.delete(0, tk.END)
        return

    tentativas += 1

    if palpite == numero_secreto:

        nome = campo_nome.get()

        if nome == "":
            nome = "Jogador"

        resultado.config(
            text="Parabéns, " + nome +
                 "!\nVocê acertou em " +
                 str(tentativas) +
                 " tentativas!"
        )

    elif palpite < numero_secreto:

        resultado.config(
            text="O número secreto é MAIOR!"
        )

    else:

        resultado.config(
            text="O número secreto é MENOR!"
        )

    campo_palpite.delete(0, tk.END)


# -----------------------------
# BOTÃO INICIAR
# -----------------------------

botao_iniciar = tk.Button(
    janela,
    text="INICIAR JOGO",
    command=iniciar_jogo,
    font=("Arial", 12)
)

botao_iniciar.pack(pady=10)


# -----------------------------
# BOTÃO TENTAR
# -----------------------------

botao_tentar = tk.Button(
    janela,
    text="TENTAR",
    command=verificar_palpite,
    font=("Arial", 12)
)

botao_tentar.pack(pady=10)


# -----------------------------
# INICIAR JANELA
# -----------------------------

janela.mainloop()
