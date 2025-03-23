import tkinter as tk
from tkinter import messagebox
from estudiante import Estudiante

class SistemaEstudiantilApp:
    def __init__(self, root):
        """Inicializa la ventana principal del sistema estudiantil."""
        self.root = root
        self.root.title("Sistema Estudiantil")
        self.root.geometry("530x800")  # Tamaño fijo de la ventana
        self.root.resizable(False, False)  # No permite cambiar el tamaño de la ventana

        # Lista para almacenar estudiantes
        self.estudiantes = []

        # Variables para los campos de entrada
        self.institucion_var = tk.StringVar(value="Universidad Autónoma de Occidente")
        self.materia_var = tk.StringVar(value="Programación")
        self.profesor_var = tk.StringVar(value="Profesor(a) Nombre")
        self.nombre_var = tk.StringVar()
        self.codigo_var = tk.StringVar(value="DRZ0")
        self.actividades_var = tk.DoubleVar()
        self.projecto_var = tk.DoubleVar()
        self.parcial_var = tk.DoubleVar()

        # Crear la interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea los elementos de la interfaz gráfica."""
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        def seleccionar_texto(event):
            """Selecciona automáticamente el texto cuando se hace clic en un campo de entrada."""
            event.widget.select_range(0, tk.END)
            event.widget.icursor(tk.END)

        # Campos de entrada
        tk.Label(frame, text="Institución:").grid(row=0, column=0, sticky=tk.W)
        entry_institucion = tk.Entry(frame, textvariable=self.institucion_var, state="readonly")
        entry_institucion.grid(row=0, column=1, sticky=tk.EW)

        tk.Label(frame, text="Materia:").grid(row=1, column=0, sticky=tk.W)
        entry_materia = tk.Entry(frame, textvariable=self.materia_var)
        entry_materia.grid(row=1, column=1, sticky=tk.EW)
        entry_materia.bind("<FocusIn>", seleccionar_texto)

        tk.Label(frame, text="Profesor(a):").grid(row=2, column=0, sticky=tk.W)
        entry_profesor = tk.Entry(frame, textvariable=self.profesor_var)
        entry_profesor.grid(row=2, column=1, sticky=tk.EW)
        entry_profesor.bind("<FocusIn>", seleccionar_texto)

        tk.Label(frame, text="Nombre del Estudiante:").grid(row=3, column=0, sticky=tk.W)
        entry_nombre = tk.Entry(frame, textvariable=self.nombre_var)
        entry_nombre.grid(row=3, column=1, sticky=tk.EW)
        entry_nombre.bind("<FocusIn>", seleccionar_texto)

        tk.Label(frame, text="Código (DRZ0XXXX):").grid(row=4, column=0, sticky=tk.W)
        entry_codigo = tk.Entry(frame, textvariable=self.codigo_var)
        entry_codigo.grid(row=4, column=1, sticky=tk.EW)
        # No se agrega bind para evitar que seleccione el texto

        tk.Label(frame, text="Actividades (1.0-5.0):").grid(row=5, column=0, sticky=tk.W)
        entry_actividades = tk.Entry(frame, textvariable=self.actividades_var)
        entry_actividades.grid(row=5, column=1, sticky=tk.EW)
        entry_actividades.bind("<FocusIn>", seleccionar_texto)

        tk.Label(frame, text="Proyecto (1.0-5.0):").grid(row=6, column=0, sticky=tk.W)
        entry_proyecto = tk.Entry(frame, textvariable=self.projecto_var)
        entry_proyecto.grid(row=6, column=1, sticky=tk.EW)
        entry_proyecto.bind("<FocusIn>", seleccionar_texto)

        tk.Label(frame, text="Parcial (1.0-5.0):").grid(row=7, column=0, sticky=tk.W)
        entry_parcial = tk.Entry(frame, textvariable=self.parcial_var)
        entry_parcial.grid(row=7, column=1, sticky=tk.EW)
        entry_parcial.bind("<FocusIn>", seleccionar_texto)

        # Botones
        tk.Button(frame, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Mostrar Estudiantes", command=self.mostrar_estudiantes).grid(row=9, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar resultados
        self.resultado_text = tk.Text(frame, height=15, width=60)
        self.resultado_text.grid(row=10, column=0, columnspan=2, pady=10)

    def validar_nota(self, nota):
        """Valida que una nota esté en el rango de 1.0 a 5.0"""
        return 1.0 <= nota <= 5.0

    def agregar_estudiante(self):
        """Agrega un nuevo estudiante validando los datos ingresados."""
        institucion = self.institucion_var.get()
        materia = self.materia_var.get().strip()
        profesor = self.profesor_var.get().strip()
        nombre = self.nombre_var.get().strip()
        codigo = self.codigo_var.get().strip().upper()
        actividades = self.actividades_var.get()
        projecto = self.projecto_var.get()
        parcial = self.parcial_var.get()

        # Validaciones
        if not materia or not profesor or not nombre or not codigo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if not codigo.startswith("DRZ0") or len(codigo) != 8 or not codigo[4:].isdigit():
            messagebox.showerror("Error", "El código debe ser 'DRZ0' seguido de 4 dígitos.")
            return

        if not (self.validar_nota(actividades) and self.validar_nota(projecto) and self.validar_nota(parcial)):
            messagebox.showerror("Error", "Las notas deben estar entre 1.0 y 5.0.")
            return

        # Crear el diccionario de notas
        notas = {
            "Actividades": actividades,
            "Proyecto": projecto,
            "Parcial": parcial,
            "Final": round((actividades + projecto + parcial) / 3, 1)
        }

        # Crear y agregar el estudiante
        estudiante = Estudiante(institucion, materia, profesor, nombre, codigo, notas)
        self.estudiantes.append(estudiante)

        messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")

    def mostrar_estudiantes(self):
        """Muestra la lista de estudiantes registrados en el área de texto."""
        self.resultado_text.delete(1.0, tk.END)  # Limpiar el área de texto

        if not self.estudiantes:
            self.resultado_text.insert(tk.END, "No hay estudiantes registrados.\n")
            return

        # Mostrar la información de cada estudiante
        for estudiante in self.estudiantes:
            self.resultado_text.insert(tk.END, estudiante.mostrar_todo() + "\n\n")

        # Calcular y mostrar el promedio de la clase
        promedio_clase = sum(est.calcular_promedio() for est in self.estudiantes) / len(self.estudiantes)
        self.resultado_text.insert(tk.END, f"Total de estudiantes: {len(self.estudiantes)}\n")
        self.resultado_text.insert(tk.END, f"Promedio de la clase: {promedio_clase:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaEstudiantilApp(root)
    root.mainloop()