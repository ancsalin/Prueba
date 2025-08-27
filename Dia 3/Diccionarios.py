diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)
resultado = diccionario['c1']
print(resultado)
 
#Ejemplo real
cliente ={'nombre':'Andrea','apelido':'Salinas','peso':86}
consulta = (cliente['nombre'])
print(consulta)

#Ejemplo complemento entre lista y diccionarios.
dic = {'c1':55,'c2':[10,20,30], 'c3':{'s1':100,'s2':200}}
print(dic['c2'][0])

#Ejemplo 2
dir = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dir['c1'][0].upper())

dicc ={1:'a',2:'b'}
print(dicc)
dicc[3] = 'c'

print(dicc)

dicc[2] = 'B'
print(dicc)

print(dicc.keys())
print(dicc.values())
print(dicc.items())