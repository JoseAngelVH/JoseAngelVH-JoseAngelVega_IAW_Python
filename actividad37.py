import tkinter as tk
from tkinter import messagebox

usuarios = []

def mostrar_datos():
    nombre = entry_nombre.get()
    edades = []
    
    if not nombre:
        messagebox.showwarning("Aviso", "Introduce el nombre")
        return
    
    for i, entry in enumerate(entries_edades):
        edad = entry.get()
        if not edad.isdigit():
            messagebox.showerror("Error", f"La edad {i+1} no es válida")
            return
        edades.append(int(edad))
    
    usuarios.append({
        "nombre": nombre,
        "edades": edades
    })
    
    messagebox.showinfo("Guardado", f"Datos de {nombre} guardados correctamente")
    limpiar_campos()

def ver_usuarios():
    if not usuarios:
        print("No hay usuarios guardados\n")
        return
    
    print("\n--- LISTA DE USUARIOS ---")
    for i, u in enumerate(usuarios, 1):
        print(f"Usuario {i}:")
        print(f"Nombre: {u['nombre']}")
        print(f"Edades: {u['edades']}")
        print("------------------------")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    for entry in entries_edades:
        entry.delete(0, tk.END)

def terminar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Formulario con múltiples usuarios")
ventana.geometry("300x550")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Introduce 10 edades:").pack(pady=5)

entries_edades = []
for i in range(10):
    entry = tk.Entry(ventana)
    entry.pack(pady=2)
    entries_edades.append(entry)

tk.Button(ventana, text="Guardar usuario", command=mostrar_datos).pack(pady=10)
tk.Button(ventana, text="Ver usuarios (print)", command=ver_usuarios).pack(pady=5)
tk.Button(ventana, text="Terminar", command=terminar).pack(pady=5)

ventana.mainloop()