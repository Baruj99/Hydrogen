import tkinter as tk

class MiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rectángulo Animado")

        self.canvas_width = 300  # Ancho inicial de la ventana
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

        # Botones
        self.boton_iniciar = tk.Button(root, text="Iniciar Animación", command=self.iniciar_animacion)
        self.boton_iniciar.place(x=10, y=90)

        self.boton_detener = tk.Button(root, text="Detener Animación", command=self.detener_animacion)
        self.boton_detener.place(x=150, y=90)

        self.animacion_activa = False  # Variable para controlar si la animación está activa

    def iniciar_animacion(self):
        if not self.animacion_activa:
            self.animacion_activa = True
            self.actualizar_altura()

    def detener_animacion(self):
        self.animacion_activa = False

    def actualizar_altura(self):
        if self.animacion_activa:
            if self.altura_rectangulo < self.altura_maxima:
                self.altura_rectangulo += 1

            self.numero_altura.config(text=f"{self.altura_rectangulo / 100:.2f}")

            self.canvas.delete("all")

            self.canvas.create_rectangle(self.posicion_x, self.extremo_inferior_y - self.altura_rectangulo,
                                         self.posicion_x + 100, self.extremo_inferior_y,
                                         fill='blue')

            self.root.after(60, self.actualizar_altura)

if __name__ == '__main__':
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
