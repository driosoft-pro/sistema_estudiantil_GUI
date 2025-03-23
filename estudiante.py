class Estudiante:
    def __init__(self, institucion, materia, profesor, nombre, codigo, notas):
        """Inicializa un estudiante con toda la información requerida."""
        self.__institucion = institucion
        self.__materia = materia
        self.__profesor = profesor
        self.__nombre = nombre
        self.__codigo = codigo
        self.__notas = notas

    def calcular_promedio(self):
        """Calcula y retorna el promedio de las notas del estudiante."""
        return sum(self.__notas.values()) / len(self.__notas)

    def mostrar_todo(self):
        """Retorna un string con toda la información del estudiante."""
        promedio = self.calcular_promedio()
        return (
            "========================================\n"
            f"Institución: {self.__institucion}\n"
            f"Materia: {self.__materia}\n"
            f"Profesor(a): {self.__profesor}\n"
            "========================================\n"
            "      Calificaciones\n"
            "========================================\n"
            f"Nombre: {self.__nombre}\n"
            f"Código: {self.__codigo}\n"
            "Las notas del estudiante son:\n"
            + "\n".join([f"{key}: {nota}" for key, nota in self.__notas.items()]) +
            f"\nPromedio del estudiante: {promedio:.2f}\n"
            "========================================\n"
        )
