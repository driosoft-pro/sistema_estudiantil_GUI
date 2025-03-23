# 📚 Sistema Estudiantil con GUI en Tkinter  

## 📝 Descripción  
Este es un **Sistema Estudiantil** desarrollado en **Python** con una **Interfaz Gráfica (GUI) en Tkinter**.  
Permite gestionar estudiantes ingresando sus datos personales y calificaciones, mostrando estadísticas y cálculos automáticos del promedio de la clase.  

## 🚀 **Características**  
✅ **Interfaz intuitiva y fácil de usar** con `Tkinter`.  
✅ **Campos predefinidos** como institución, materia y profesor.  
✅ **Validaciones estrictas** para evitar entradas incorrectas.  
✅ **Cálculo automático del promedio** del estudiante y la clase.  
✅ **Tamaño de ventana fijo (`530x800`)** para mejor experiencia.  
✅ **Selección automática del texto** al hacer clic en los campos de entrada (excepto el código).  
✅ **Manejo de errores y validaciones** con `messagebox`.  

## 🛠️ **Tecnologías utilizadas**  
- 🐍 **Python** (Lenguaje de programación)  
- 🎨 **Tkinter** (Interfaz gráfica de usuario - GUI)  

## 📂 **Estructura del Proyecto**  
```
/sistema_estudiantil  
│── estudiante.py       # Lógica de la clase Estudiante  
│── main.py             # Interfaz gráfica y lógica de la aplicación  
│── README.md           # Documentación del proyecto  
```

## APP
[Screenshot-2025-03-22-223238.png](https://postimg.cc/LYPD6Npx)

[Screenshot-2025-03-22-223742.png](https://postimg.cc/1g2MQbLg)

## 🏗️ **Instalación y ejecución**  

### 1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/tu_usuario/sistema_estudiantil.git
cd sistema_estudiantil
```

### 2️⃣ Ejecutar el programa  
Asegúrate de tener Python instalado en tu sistema. Luego, ejecuta:  
```bash
python main.py
```

## 🖥️ **Uso del Sistema**  
1. **Ingresar los datos del estudiante**, incluyendo notas (entre `1.0` y `5.0`).  
    1. **Registro de Estudiantes**:
       - El sistema solicita el nombre, código y notas de cada estudiante.
       - El código debe comenzar con `DRZ0` seguido de 4 dígitos (por ejemplo, `DRZ01234`).
       - Las notas deben estar en el rango de 1.0 a 5.0.

    2. **Cálculo de Promedios**:
       - El sistema calcula automáticamente la nota final como el promedio de las notas de `Actividades`, `Projecto` y `Parcial`.
       - También se calcula el promedio de la clase al final.

    3. **Visualización de Datos**:
       - Al final, el sistema muestra la lista de estudiantes con sus notas y promedios, junto con el promedio general de la clase.
2. **Presionar "Agregar Estudiante"** para guardar los datos.  
3. **Presionar "Mostrar Estudiantes"** para visualizar la lista de estudiantes y el promedio de la clase.  



## ⚠️ **Validaciones Importantes**  
✅ **Código del estudiante:** Debe iniciar con `DRZ0` seguido de 4 dígitos.  
✅ **Notas:** Solo valores entre `1.0` y `5.0`.  
✅ **Nombre, código y otros datos son obligatorios.**  

## 📸 **Capturas de Pantalla**  
🔹 **Pantalla Principal:**  
![Pantalla Principal](ruta_a_la_imagen.png)  

🔹 **Validaciones en acción:**  
![Validación](ruta_a_la_imagen_validacion.png)  

## 🤝 **Contribuciones**  
¡Las contribuciones son bienvenidas! Si encuentras un error o quieres mejorar algo, puedes hacer un **Pull Request** o abrir un **Issue** en GitHub.  

## 📜 **Licencia**  
Este proyecto está bajo la **Licencia MIT**. ¡Siéntete libre de usarlo y modificarlo! 🎉  

---  

✍️ **Desarrollado por:** **Deyton Riasco Ortiz**  
📅 **Fecha:** 2025  
📧 **Contacto:** [deyton007@gmail.com](mailto:deyton007@gmail.com)