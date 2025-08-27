archivo =  open('Prueba.txt', 'w')
archivo.write('''Limpia tu corazón, 
              dale tiempo al tiempo, Dios es bueno''')

archivo.writelines(['Hola', 'Andre', 'Tu', 'Puedes'])
archivo.close()

#Ejercicio2
archivo1 = open('Prueba1.txt', 'w')
lista = ['Tiempo', 'Al', 'Tiempo']
for p in lista:
  archivo1.writelines(p + '\n')
archivo1.close()

#Practica1 ---Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto". Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

open("mi_archivo.txt", "w").write("Nuevo texto")
print(open("mi_archivo.txt", "r").read())

#Practica2 ----Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

open("mi_archivo.txt" , "a").write("Nuevo inicio de sesión")

print(open("mi_archivo.txt", "r").read())

#Practica 3
# Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
open("registro.txt" , "a").writelines("\t".join(registro_ultima_sesion) + "\n")
print(open("registro.txt", "r").read())



