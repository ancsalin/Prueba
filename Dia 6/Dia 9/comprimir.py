import zipfile

'''
Comprimir un archivo
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('Mi_textoA.txt')
mi_zip.write('Mi_textoBy.txt')

mi_zip.close()'''

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()