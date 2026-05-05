import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    nombre = entry_nombre.get()
    edades = []
    
    if not nombre:
        messagebox.showwarning("Aviso", "Introduce el nombre")
        return
    
    # Recoger las 10 edades
    for i, entry in enumerate(entries_edades):
        edad = entry.get()
        if not edad.isdigit():
            messagebox.showerror("Error", f"La edad {i+1} no es válida")
            return
        edades.append(int(edad))
    
    messagebox.showinfo(
        "Datos introducidos",
        f"Nombre: {nombre}\nEdades: {edades}"
    )

def terminar():
    ventana.destroy()

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario con 10 edades")
ventana.geometry("300x500")

# Nombre
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Edades
tk.Label(ventana, text="Introduce 10 edades:").pack(pady=5)

entries_edades = []
for i in range(10):
    entry = tk.Entry(ventana)
    entry.pack(pady=2)
    entries_edades.append(entry)

# Botones
tk.Button(ventana, text="Mostrar datos", command=mostrar_datos).pack(pady=10)
tk.Button(ventana, text="Terminar", command=terminar).pack(pady=5)

ventana.mainloop()