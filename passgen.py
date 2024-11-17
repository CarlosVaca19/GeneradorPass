import tkinter as tk
from tkinter import messagebox
import string
import random

def generar_contrasena():
    # Obtener la longitud de la entrada
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido mayor a 0.")
        return

    # Determinar el conjunto de caracteres
    caracteres = ""
    if var_letras.get():
        caracteres += string.ascii_letters
    if var_numeros.get():
        caracteres += string.digits
    if var_signos.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showerror("Error", "Seleccione al menos un tipo de carácter.")
        return

    # Generar la contraseña
    password = "".join(random.choice(caracteres) for _ in range(longitud))

    # Mostrar la contraseña en el cuadro de texto
    entry_resultado.config(state="normal")  # Habilitar edición temporalmente
    entry_resultado.delete(0, tk.END)      # Borrar texto previo
    entry_resultado.insert(0, password)   # Insertar la nueva contraseña
    entry_resultado.config(state="readonly")  # Bloquear edición nuevamente

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x300")

# Etiqueta para la longitud
label_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)

# Entrada para la longitud
entry_longitud = tk.Entry(ventana, width=10)
entry_longitud.pack(pady=5)

# Checkboxes para las opciones
var_letras = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_signos = tk.BooleanVar()

checkbox_letras = tk.Checkbutton(ventana, text="Incluir letras", variable=var_letras)
checkbox_letras.pack()

checkbox_numeros = tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros)
checkbox_numeros.pack()

checkbox_signos = tk.Checkbutton(ventana, text="Incluir signos de puntuación", variable=var_signos)
checkbox_signos.pack()

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack(pady=20)

# Cuadro de texto para mostrar la contraseña generada
label_resultado = tk.Label(ventana, text="Contraseña generada:")
label_resultado.pack(pady=5)

entry_resultado = tk.Entry(ventana, width=40, state="readonly")
entry_resultado.pack(pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
