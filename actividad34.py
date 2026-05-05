import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    if not nombre or not edad:
        messagebox.showwarning("Aviso", "Por favor, completa todos los campos")
        return
    
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número")
        return
    
    messagebox.showinfo("Datos introducidos", f"Nombre: {nombre}\nEdad: {edad}")

def terminar():
    ventana.destroy()  # Cierra la ventana

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario simple")
ventana.geometry("300x220")

# Etiquetas y campos
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack(pady=5)

# Botones
tk.Button(ventana, text="Mostrar datos", command=mostrar_datos).pack(pady=5)
tk.Button(ventana, text="Terminar", command=terminar).pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()