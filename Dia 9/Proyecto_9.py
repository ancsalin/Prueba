import re
import os
import time
import datetime
from  pathlib import Path
import math

inicio = time.time()

ruta = 'C:C:\\Users\\acsal\\Documents\\CursoPython\\Dia 9\\Proyecto+Dia+9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3} \d{5}'
hoy = datetime.date.today()
num_encontrados =[]
arc_encontrado = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a) , mi_patron)
            if resultado!= '':
                num_encontrados.append((resultado.group()))
                arc_encontrado.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO . SERIE')
    print('--------\t\t\t---------')

    for a in arc_encontrado:
        print(f'{a}\t{num_encontrados[indice]}')
        indice +=1

    print('\n')
    print(f'Numeros encontrados: {len(num_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()