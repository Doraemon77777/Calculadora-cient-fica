import tkinter as tk
from tkinter import messagebox
import math

historial = []

def guardar_historial(texto):
    historial.append(texto)
    with open("historial.txt", "a") as f:
        f.write(texto + "\n")

def sumar():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        r = a + b
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"{a} + {b} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def restar():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        r = a - b
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"{a} - {b} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def multiplicar():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        r = a * b
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"{a} * {b} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def dividir():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if b == 0:
            messagebox.showerror("Error","Division por cero")
            return
        r = a / b
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"{a} / {b} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def potencia():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        r = a ** b
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"{a}^{b} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def raiz():
    try:
        a = float(entry1.get())
        r = math.sqrt(a)
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"√{a} = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def absoluto():
    try:
        a = float(entry1.get())
        r = abs(a)
        resultado.config(text="Resultado: " + str(r))
        guardar_historial(f"|{a}| = {r}")
    except:
        messagebox.showerror("Error","Entrada invalida")

def ver_historial():
    try:
        with open("historial.txt","r") as f:
            datos = f.read()
        messagebox.showinfo("Historial",datos)
    except:
        messagebox.showinfo("Historial","No hay historial")

ventana = tk.Tk()
ventana.title("Calculadora Cientifica")
ventana.geometry("400x400")
ventana.configure(bg="#202020")

titulo = tk.Label(ventana,text="Calculadora Cientifica",font=("Arial",16),bg="#202020",fg="white")
titulo.pack(pady=10)

entry1 = tk.Entry(ventana,font=("Arial",12))
entry1.pack(pady=5)

entry2 = tk.Entry(ventana,font=("Arial",12))
entry2.pack(pady=5)

resultado = tk.Label(ventana,text="Resultado:",font=("Arial",14),bg="#202020",fg="white")
resultado.pack(pady=10)

tk.Button(ventana,text="Sumar",width=15,command=sumar).pack(pady=2)
tk.Button(ventana,text="Restar",width=15,command=restar).pack(pady=2)
tk.Button(ventana,text="Multiplicar",width=15,command=multiplicar).pack(pady=2)
tk.Button(ventana,text="Dividir",width=15,command=dividir).pack(pady=2)
tk.Button(ventana,text="Potencia",width=15,command=potencia).pack(pady=2)
tk.Button(ventana,text="Raiz",width=15,command=raiz).pack(pady=2)
tk.Button(ventana,text="Valor absoluto",width=15,command=absoluto).pack(pady=2)
tk.Button(ventana,text="Ver historial",width=15,command=ver_historial).pack(pady=10)

ventana.mainloop()