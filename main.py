import tkinter as tk
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0 and a != 0:
        return a / b
    else:
        return "Divisão por zero"

def calcular():
    entradaA = float(inputA.get())
    entradaB = float(inputB.get())
    operacao = combo_operacao.get()

    if operacao == "Soma":
        resultado = soma(entradaA, entradaB)
    elif operacao == "Subtração":
        resultado = subtracao(entradaA, entradaB)
    elif operacao == "Multiplicação":
        resultado = multiplicacao(entradaA, entradaB)
    elif operacao == "Divisão":
        resultado = divisao(entradaA, entradaB)

    if type(resultado) == float:
        resultado = round(resultado, 1)

    label_resultado.config(text="Resultado: " + str(resultado))

# Cria a janela principal
window = tk.Tk()
window.title("Calculadora Python")

# Cria os widgets da interface
label_a = tk.Label(window, text="Valor A:")
label_a.pack()

inputA = tk.Entry(window)
inputA.pack()

label_b = tk.Label(window, text="Valor B:")
label_b.pack()

inputB = tk.Entry(window)
inputB.pack()

label_operacao = tk.Label(window, text="Operação:")
label_operacao.pack()

import tkinter.ttk as ttk

combo_operacao = ttk.Combobox(window, values=["Soma", "Subtração", "Multiplicação", "Divisão"])
combo_operacao.pack()

button_calcular = tk.Button(window, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(window, text="Resultado:")
label_resultado.pack()

# Inicia o loop de eventos da interface
window.mainloop()
