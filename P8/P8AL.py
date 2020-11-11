#primero mandamos llamar las librerias que usaremos
import numpy as np
from random import randint
from math import exp, floor, log
from random import random
from numpy.random import shuffle
import matplotlib.pyplot as plt      


 #para cada k se saca el valor maximo de filtración

cums = [1000,1500,2000,5000]             #numero de cumulos con diferentes variaciones
parts = [100000,500000,1000000,10000000]                              #numero de particulas
filtradosT=[]
filtran=[]
for k in cums:
  c=0
  for n in parts:
    orig = np.random.normal(size = k)
    cumulos = orig - min(orig)              
    cumulos += 1                            # El menor vale uno
    cumulos = cumulos / sum(cumulos)        # Suman a uno
    cumulos *= n                            # Suman a n, pero son valores decimales
    cumulos = np.round(cumulos).astype(int) # Redondea los numeros para que sean enteros
    diferencia = n - sum(cumulos)           # Por cuanto le hemos fallado para la meta 
    cambio = 1 if diferencia > 0 else -1    #Si sobran o faltan 
    while diferencia != 0:                  #empareja la diferencia si sobro o falto 
        p = randint(0, k - 1)
        if cambio > 0 or (cambio < 0 and cumulos[p] > 0): # sin vaciar
            cumulos[p] += cambio
            diferencia -= cambio
    assert all(cumulos != 0)
    print(c)
    assert sum(cumulos) == n                #verifica que los cumulos sumen a "n"
 
    c = np.median(cumulos)           # tamaño crítico de cúmulos (toma la mediana)
    d = np.std(cumulos) / 4          # factor arbitrario para suavizar la curva (desviacion estandar/4 para usar la misma d) 
 
    def rotura(x, c, d):
        return 1 / (1 + exp((c - x) / d))    #define el sigmoidal
     
    def union(x, c):
        return exp(-x / c)                      #no filtran
 
    def romperse(tam, cuantos):
        if tam == 1:                # no se puede romper
            return [tam] * cuantos
        res = []
        for cumulo in range(cuantos):
            if random() < rotura(tam, c, d):
                primera = randint(1, tam - 1)
                segunda = tam - primera
                assert primera > 0
                assert segunda > 0
                assert primera + segunda == tam
                res += [primera, segunda]
            else:
                res.append(tam) # no rompió
        assert sum(res) == tam * cuantos
        return res
 
    def unirse(tam, cuantos):
        res = []
        for cumulo in range(cuantos):
            if random() < union(tam, c):
                res.append(-tam) # marcamos con negativo los que quieren unirse
            else:
                res.append(tam)
        return res
 
    duracion = 100               #variamos la duracion 
    digitos = floor(log(duracion, 10)) + 1
    nofiltra=[]
    sifiltra=[]
    for paso in range(duracion):
        assert sum(cumulos) == n
        assert all([c > 0 for c in cumulos]) 
        (tams, freqs) = np.unique(cumulos, return_counts = True)
        print(tams,freqs,'cumulos')      #maximo de cumulos
        cumulos = []
        assert len(tams) == len(freqs)
        for i in range(len(tams)):           #for anidado
            cumulos += romperse(tams[i], freqs[i]) 
        assert sum(cumulos) == n
        assert all([c > 0 for c in cumulos]) 
        (tams, freqs) = np.unique(cumulos, return_counts = True)
        sifiltra.append(max(freqs))
        cumulos = []
        assert len(tams) == len(freqs)
        for i in range(len(tams)):
            cumulos += unirse(tams[i], freqs[i])
        cumulos = np.asarray(cumulos)
        nofiltra.append([tams])
        neg = cumulos < 0
        a = len(cumulos)
        juntarse = -1 * np.extract(neg, cumulos)     # sacarlos y hacerlos positivos
        cumulos = np.extract(~neg, cumulos).tolist() # los demás van en una lista
        assert a == len(juntarse) + len(cumulos)
        nt = len(juntarse)
        if nt > 1:
            shuffle(juntarse)                        # orden aleatorio
        j = juntarse.tolist()
        while len(j) > 1:                            # agregamos los pares formados
            cumulos.append(j.pop(0) + j.pop(0))
        if len(j) > 0:                               # impar
            cumulos.append(j.pop(0))                 # el ultimo no alcanzó pareja
        assert len(j) == 0
        assert sum(cumulos) == n
        assert all([c != 0 for c in cumulos])
        cortes = np.arange(min(cumulos), max(cumulos), 50)
        print(cortes,paso,'tam')         #tamaños

    filtradosT.append(sifiltra)
  filtran.append(filtradosT)  
print(filtran, kum)
'''     
#parte grafica
#plt.hist(cumulos, bins = cortes, align = 'right', density = True)
#plt.xlabel('Tamaño')
#plt.ylabel('Frecuencia relativa')
#plt.ylim(0, 0.05)
#plt.title('Paso {:d} con ambos fenómenos'.format(paso + 1))
#plt.savefig('p9p_ct' + format(paso, '0{:d}'.format(digitos)) + '.png')
#plt.close()
#fig = plt.figure()
no nos enfocamos en los histogramas
'''
plt.boxplot([filtrat[i] for i in range(len(kum))])
box = plt.boxplot([filtrat[i] for i in range(len(kum))], notch=True, patch_artist=True)  #para poner los picos de las graficas
colors = ['cyan', 'lightblue', 'lightgreen', 'pink']   #linea 129-132 es parte del codigo de matplotlib para poner color a las graficas
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.xticks([i for i in range(1, len(kum)+1)], kum)
plt.grid(True)                            #agrega cuadros al grafico
plt.ylabel('Porcentaje de Filtrados')
plt.xlabel('Cumulos')
plt.savefig('Grafica40.png')
plt.show()
plt.close()


