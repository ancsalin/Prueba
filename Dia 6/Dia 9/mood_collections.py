#from collections import Counter
from  collections import defaultdict

mi_dic = {'uno':'azul', 'dos':'amarillo'}

mi_dic = defaultdict(lambda : ' nada')
print(mi_dic['tres'])

#numeros =[5,6,8,9,7,4,5,6]
#print(Counter(numeros))
#frase = 'Todo va a mejorar'
#print(Counter(frase.split()))
#serie = Counter([1,1,2,3,3,3,4,4,5,5,5])
#print(serie.most_common()