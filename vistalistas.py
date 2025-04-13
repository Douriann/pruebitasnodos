import tkinter as tk
from tkinter import messagebox
from Lista import Lista  # Asegúrate de importar correctamente

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Lista Enlazada Visual")
ventana.geometry("800x500")

# Crear lista
lista = Lista()

# Canvas para dibujar
canvas = tk.Canvas(ventana, width=750, height=300, bg="white")
canvas.pack(pady=20)

# Variables para selección
nodo_seleccionado = None

# Función para dibujar la lista
def dibujar_lista():
    global nodo_seleccionado
    canvas.delete("all")
    
    if lista.Vacia():
        canvas.create_text(375, 150, text="[Lista vacía]", font=("Arial", 14))
        return
    
    x = 100  # Posición inicial X
    y = 150  # Posición fija Y
    separacion = 100  # Espacio entre nodos
    
    p = lista.Primero
    while p is not None:
        # Dibujar nodo (círculo + texto)
        color = "red" if p == lista.Primero else ("lightgreen" if p == nodo_seleccionado else "lightblue")
        canvas.create_oval(x-30, y-30, x+30, y+30, fill=color, tags=f"nodo_{p.info}")
        canvas.create_text(x, y, text=str(p.info), font=("Arial", 12))
        
        # Dibujar flecha si hay próximo nodo
        if p.prox is not None:
            canvas.create_line(x+30, y, x+separacion-30, y, arrow=tk.LAST)
        
        # Etiquetar cabeza
        if p == lista.Primero:
            canvas.create_text(x, y-50, text="Primero", fill="red", font=("Arial", 10, "bold"))
        
        # Asignar evento de clic para selección
        canvas.tag_bind(f"nodo_{p.info}", "<Button-1>", lambda e, nodo=p: seleccionar_nodo(nodo))
        
        x += separacion
        p = p.prox

# Selección de nodo
def seleccionar_nodo(nodo):
    global nodo_seleccionado
    nodo_seleccionado = nodo
    dibujar_lista()

# Insertar al inicio
def insertar_inicio():
    valor = entry_valor.get()
    if valor:
        if lista.InsComienzo(valor):
            dibujar_lista()
        else:
            messagebox.showerror("Error", "¡Memoria llena!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    entry_valor.delete(0, tk.END)

# Eliminar al inicio
def eliminar_inicio():
    if lista.Vacia():
        messagebox.showinfo("Info", "Lista vacía")
    else:
        lista.EliComienzo()
        dibujar_lista()

# Insertar después del seleccionado
def insertar_despues():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
        return
    
    valor = entry_valor.get()
    if valor:
        if lista.InsDespues(nodo_seleccionado, valor):
            dibujar_lista()
        else:
            messagebox.showerror("Error", "¡Memoria llena!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    entry_valor.delete(0, tk.END)

# Eliminar después del seleccionado
def eliminar_despues():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
    else:
        valor = lista.EliDespues(nodo_seleccionado)
        if valor is None:
            messagebox.showinfo("Info", "No hay nodo siguiente")
        dibujar_lista()

# Interfaz
frame_botones = tk.Frame(ventana)
frame_botones.pack()

entry_valor = tk.Entry(frame_botones, width=10)
entry_valor.pack(side=tk.LEFT, padx=5)

tk.Button(frame_botones, text="Insertar Inicio", command=insertar_inicio).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar Inicio", command=eliminar_inicio).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Insertar Después", command=insertar_despues).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar Después", command=eliminar_despues).pack(side=tk.LEFT, padx=5)

# Mostrar lista inicial
dibujar_lista()
ventana.mainloop()