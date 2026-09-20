import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()

    if nombre == "":
        resultado.config(
            text = "> ERROR: IDENTIDAD NO DETECTADA"
        )
    else:
        resultado.config(
        text = f"> Bienvenido, {nombre}\n> STATUS: ACCESS GRANTED"
    )

def limpiar():
    entrada_nombre.delete(0, tk.END)
    resultado.config(
        text="> SYSTEM READY"
    )
    entrada_nombre.focus()

def ejecutar_con_enter(event):
    saludar()

ventana = tk.Tk()

ventana.title("CyberSaludo")
ventana.geometry("600x420")
ventana.configure(bg="#05070a")

titulo = tk.Label(
    ventana,
    text= "CYBER // SALUDO",
    font = ("Consolas", 24, "bold"),
    bg = "#05070a",
    fg = "#00f5ff"
)

titulo.pack(pady=(40, 10))

subtitulo_nombre = tk.Label(
    ventana,
    text= ("SYSTEM // USER IDENTIFICATION"),
    font=("Consolas", 11),
    bg=("#05070a"),
    fg= ("#7df9ff")
)

subtitulo_nombre.pack(pady=5)

etiqueta_nombre = tk.Label(
    ventana,
    text = "IDENTIDAD",
    font = ("Consolas", 12),
    bg = "#05070a",
    fg = "white"
)

etiqueta_nombre.pack(pady=(20, 5))

entrada_nombre = tk.Entry(
    ventana,
    font = ("Consolas", 14),
    width = 30,
    bg = "#101020",
    fg = "#00f5ff",
    insertbackground = "#00f5ff",
    relief = "flat"
)

entrada_nombre.pack(ipady = 8)

boton = tk.Button(
    ventana,
    text="EJECUTAR",
    font = ("Consolas", 12, "bold"),
    bg = "#00f5ff",
    fg = "#05070a",
    activebackground = "#7df9ff",
    relief = "flat",
    padx = 30,
    pady = 10,
    command= saludar
)

boton.pack(pady =(30, 10))

boton_limpiar = tk.Button(
    ventana,
    text=("LIMPIAR"),
    font=("Consolas", 10),
    bg="#101820",
    fg="white",
    activebackground="#202b33",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=limpiar
)

boton_limpiar.pack()

resultado = tk.Label(
    ventana,
    text = ">SYSTEM READY",
    font = ("Consolas", 12),
    bg = ("#05070a"),
    fg = ("#39ff14"),
    justify="left"
)

resultado.pack(pady=20)

entrada_nombre.bind("<Return>", ejecutar_con_enter)

entrada_nombre.focus()

ventana.mainloop()