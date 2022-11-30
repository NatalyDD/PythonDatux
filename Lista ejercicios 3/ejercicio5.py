def obtener_nom_archivo():
    import os
    ruta = r"D:\Workspace\Pythonclases\Ejercicios tarea 3\ejercicio5.py"
    nombre_archivo = os.path.basename(ruta)
    print("El nombre de este archivo es: ",nombre_archivo)

