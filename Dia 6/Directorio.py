from pathlib import  Path

#ruta = os.getcwd()
#ruta = os.chdir('C:\\Users\\acsal\\OneDrive\\Documents\\Curso Python')
#Crear directorio
#ruta = 'C:\\Users\\acsal\\Documents\\CursoPython\\Dia 6\\Prueba.txt'

#elemento = os.path.basename(ruta)
#elemento = os.path.split(ruta)
#print(ruta)

#Eliminar carpeta = os.rmdir('C:\\Users\\acsal\\OneDrive\\Documents\\Otros')

carpeta = Path('C:/Users/acsal/OneDrive/Documents/Curso Python')

archivo = carpeta / 'Prueba2.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())