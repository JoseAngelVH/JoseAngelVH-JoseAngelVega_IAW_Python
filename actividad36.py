import tkinter as tk
from tkinter import messagebox

usuarios = []  # Lista para guardar todos los usuarios

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
    
    # Guardar usuario
    usuarios.append({
        "nombre": nombre,
        "edades": edades
    })
    
    messagebox.showinfo("Guardado", f"Datos de {nombre} guardados correctamente")
    
    limpiar_campos()

def ver_usuarios():
    if not usuarios:
        messagebox.showinfo("Usuarios", "No hay usuarios guardados")
        return
    
    texto = ""
    for i, u in enumerate(usuarios, 1):
        texto += f"Usuario {i}:\n"
        texto += f"Nombre: {u['nombre']}\n"
        texto += f"Edades: {u['edades']}\n\n"
    
    messagebox.showinfo("Todos los usuarios", texto)

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    for entry in entries_edades:
        entry.delete(0, tk.END)

def terminar():
    ventana.destroy()

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario con múltiples usuarios")
ventana.geometry("300x550")

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
tk.Button(ventana, text="Guardar usuario", command=mostrar_datos).pack(pady=10)
tk.Button(ventana, text="Ver todos los usuarios", command=ver_usuarios).pack(pady=5)
tk.Button(ventana, text="Terminar", command=terminar).pack(pady=5)

ventana.mainloop()