from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/acsal/Documents/CursoPython/Dia 6/Prueba.txt')

ruta_w = PureWindowsPath(carpeta)

print(ruta_w)

if not carpeta.exists():
  print("Este archivo no esta")
else:
 print("Si existe, tontis")

#Name = nombre del archivo. suffix = extension de archivo.  stem = nombre sin la extension
