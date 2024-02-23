import tkinter as tk

class MiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rectángulo Animado")

        self.canvas_width = 900  # Ancho inicial de la ventana
        self.canvas_height = 500  # Altura inicial de la ventana
        self.root.geometry(f"{self.canvas_width}x{self.canvas_height}")

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.altura_rectangulo = 50
        self.altura_maxima = 200  # Altura máxima del rectángulo
        self.extremo_inferior_y = 450  # Coordenada y del extremo inferior fijo
        self.posicion_x = 50  # Coordenada x del extremo izquierdo del rectángulo

        # Título centrado
        self.titulo = tk.Label(root, text="Panel de control", font=("Helvetica", 16))
        self.titulo.place(relx=0.5, rely=0.05, anchor="center")

        # Campos de entrada
        self.label_posicion = tk.Label(root, text="Posición de equilibrio:")
        self.label_posicion.place(x=10, y=30)
        self.entry_posicion = tk.Entry(root)
        self.entry_posicion.place(x=150, y=30)

        self.label_volumen = tk.Label(root, text="Volumen:")
        self.label_volumen.place(x=10, y=60)
        self.entry_volumen = tk.Entry(root)
        self.entry_volumen.place(x=150, y=60)

        # Texto a la derecha del rectángulo
        self.texto_altura = tk.Label(root, text="Altura", font=("Helvetica", 12))
        self.texto_altura.place(x=self.posicion_x + 120, y=self.extremo_inferior_y - self.altura_rectangulo + 10, anchor="w")

        # Número justo debajo del texto
        self.numero_altura = tk.Label(root, text="0.01", font=("Helvetica", 12))
        self.numero_altura.place(x=self.posicion_x + 120, y=self.extremo_inferior_y - self.altura_rectangulo + 30, anchor="w")

        # Iniciar la animación con el método after de Tkinter
        self.actualizar_altura()

    def actualizar_altura(self):
        # Variar la altura del rectángulo en cada actualización
        if self.altura_rectangulo < self.altura_maxima:
            self.altura_rectangulo += 1

        # Actualizar el número de altura
        self.numero_altura.config(text=f"{self.altura_rectangulo / 100:.2f}")

        # Limpiar la representación gráfica actual del canvas
        self.canvas.delete("all")

        # Dibujar un rectángulo azul con el extremo inferior fijo y altura variable
        self.canvas.create_rectangle(self.posicion_x, self.extremo_inferior_y - self.altura_rectangulo,
                                     self.posicion_x + 100, self.extremo_inferior_y,
                                     fill='blue')

        # Programar la próxima actualización después de 30 milisegundos (60 FPS)
        self.root.after(60, self.actualizar_altura)

if __name__ == '__main__':
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
