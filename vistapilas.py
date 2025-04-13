import tkinter as tk
from tkinter import messagebox
from Pila import Pila  # Asegúrate de importar correctamente

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Visualización de Pila")
ventana.geometry("600x500")

# Crear una instancia de tu Pila
pila = Pila()

# Canvas para dibujar la pila
canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack(pady=20)

# Función para dibujar la pila
def dibujar_pila():
    canvas.delete("all")  # Limpiar el canvas
    
    if pila.Vacia():
        canvas.create_text(200, 150, text="[Pila vacía]", font=("Arial", 14))
        return
    
    x = 200  # Posición fija en X (centro)
    y = 50   # Posición inicial en Y (parte SUPERIOR, donde empieza el Tope)
    separacion = 50  # Espacio vertical entre nodos
    
    p = pila.Tope
    while p is not None:
        # Dibujar nodo (rectángulo + texto)
        canvas.create_rectangle(x-30, y, x+30, y+40, fill="lightblue", outline="black")
        canvas.create_text(x, y+20, text=str(p.info), font=("Arial", 12))
        
        # Resaltar el Tope (rojo)
        if p == pila.Tope:
            canvas.create_text(x, y-15, text="Tope", fill="red", font=("Arial", 10, "bold"))
        
        # Dibujar línea que conecta con el nodo inferior (si existe)
        if p.ap is not None:
            canvas.create_line(x, y+40, x, y+separacion, arrow=tk.LAST)
        
        y += separacion  # Moverse hacia ABAJO para el próximo nodo
        p = p.ap

# Botones para operaciones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Insertar elemento
entry_valor = tk.Entry(frame_botones, width=10)
entry_valor.pack(side=tk.LEFT, padx=5)

def insertar():
    valor = entry_valor.get()
    if valor:
        if pila.Insertar(valor):
            dibujar_pila()
        else:
            messagebox.showerror("Error", "¡Pila llena (memoria)!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    entry_valor.delete(0, tk.END)

tk.Button(frame_botones, text="Apilar (Push)", command=insertar).pack(side=tk.LEFT, padx=5)

# Remover elemento
def remover():
    if pila.Vacia():
        messagebox.showinfo("Info", "La pila está vacía.")
    else:
        pila.Remover()
        dibujar_pila()

tk.Button(frame_botones, text="Desapilar (Pop)", command=remover).pack(side=tk.LEFT, padx=5)

# Mostrar pila inicial
dibujar_pila()
ventana.mainloop()