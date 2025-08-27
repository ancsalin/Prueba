#Ejercicios 1
from pathlib import Path
ruta_completa = Path("Curso Python", "Día 6", "practicas_path.py")

ruta = ruta_completa.relative_to("Curso Python")

print(ruta_completa)


#Ejercicios 2
from pathlib import Path

# Obtenemos la carpeta base del usuario
base_usuario = Path.home()

# Creamos la ruta absoluta hacia el archivo
ruta = base_usuario / "Curso Python" / "Día 6" / "practicas_path.py"

# Mostramos la ruta absoluta
print(ruta)

#Ejercicios 3
def abrir_leer(archivo):
    archivo = open(archivo, 'r')
    return archivo.read()

#Ejercicio 4

def sobrescribir(mi_archivo):
    mi_archivo = open(mi_archivo, 'w')
    mi_archivo.write("contenido eliminado")
    mi_archivo.close()

