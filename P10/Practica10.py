#Version mejorada
import numpy as np
import pandas as pd
from random import random, randint, sample, uniform
  #un algoritmo, opera en terminos de cual es el peso total de todos los objetos
def knapsack(peso_permitido, pesos, valores):
    assert len(pesos) == len(valores)
    peso_total = sum(pesos) #cual es el peso total de toda la rutina
    valor_total = sum(valores)
    if peso_total < peso_permitido:   # cabe todo
        return valor_total
    else:
        V = dict()
        for w in range(peso_permitido + 1):
            V[(w, 0)] = 0
        for i in range(len(pesos)):
            peso = pesos[i]
            valor = valores[i]
            for w in range(peso_permitido + 1):
                cand = V.get((w - peso, i), -float('inf')) + valor
                V[(w, i + 1)] = max(V[(w, i)], cand)
        return max(V.values())
 #llena una tabla de manera sistematica y extrae
    
def factible(seleccion, pesos, capacidad): #respeta la capacidad si la seleccion da 1 se toma en cuenta el peso, y si da 0 el peso no se toma en cuenta
    return np.inner(seleccion, pesos) <= capacidad
  
def objetivo(seleccion, valores):   #toma la totalidad de valor que contribuye a la seleccion
    return np.inner(seleccion, valores)
 
def normalizar(data): #normalizar, tomamos el minimo el maximo, las diferencias y todo para que de entre 0 y 1
    menor = min(data)
    mayor = max(data)
    rango  = mayor - menor
    data = data - menor # > 0
    return data / rango # entre 0 y 1 
  
def generador_pesos(cuantos, low, high): #generamos pesos
    return np.round(normalizar(np.random.normal(size = cuantos)) * (high - low) + low)
 
def generador_valores(pesos, low, high): #usa el peso para generar el valor
    n = len(pesos)
    valores = np.empty((n))
    for i in range(n):     #usa el peso para generar el valor
        valores[i] = np.random.normal(pesos[i], random(), 1)
    return normalizar(valores) * (high - low) + low 
 
def poblacion_inicial(n, tam):  #creamos la poblacion inicial
    pobl = np.zeros((tam, n))
    for i in range(tam):
        pobl[i] = (np.round(np.random.uniform(size = n))).astype(int)
    return pobl
 
def mutacion(sol, n):  #mutamos al individuo
    pos = randint(0, n - 1)
    mut = np.copy(sol)
    mut[pos] = 1 if sol[pos] == 0 else 0
    return mut
  
def reproduccion(x, y, n): #se hace la reproduccion entre los iniciales y los mutados
    pos = randint(2, n - 2)
    xy = np.concatenate([x[:pos], y[pos:]])
    yx = np.concatenate([y[:pos], x[pos:]])
    return (xy, yx)

def regla(a, v, i) :
    if regla == 1:
        peso = exp(a*t)
        valor =exp(v*t)
        return peso, valor
    if regla2 ==2:
        peso = exp(a*t)
        valor = peso*uniform(0, 0.1)
        return peso, valor
    if regla3 ==3:
        peso = exp(a*t)
        valor= uniform(0,0.1)/peso
        return peso, valor
 
n = 50 #numero de objetos a variar
pesos = generador_pesos(n, 15, 80)
valores = generador_valores(pesos, 10, 500)
capacidad = int(round(sum(pesos) * 0.65))
optimo = knapsack(capacidad, pesos, valores)
init = 200
p = poblacion_inicial(n, init)
tam = p.shape[0]
assert tam == init
pm = 0.05  #probabilidad de mutacion 
rep = 50
tmax = 50
mejor = None
mejores = []
for t in range(tmax):
    for i in range(tam): # mutarse con probabilidad pm
        if random() < pm:
            p = np.vstack([p, mutacion(p[i], n)])
    for i in range(rep):  # reproducciones
        padres = sample(range(tam), 2)
        hijos = reproduccion(p[padres[0]], p[padres[1]], n)
        p = np.vstack([p, hijos[0], hijos[1]])
    tam = p.shape[0]
    d = []
    for i in range(tam):
        d.append({'idx': i, 'obj': objetivo(p[i], valores),
                  'fact': factible(p[i], pesos, capacidad)})
    d = pd.DataFrame(d).sort_values(by = ['fact', 'obj'], ascending = False)
    mantener = np.array(d.idx[:init])
    p = p[mantener, :]
    tam = p.shape[0]
    assert tam == init
    factibles = d.loc[d.fact == True,]
    mejor = max(factibles.obj)
    mejores.append(mejor)
 
import matplotlib.pyplot as plt
  
plt.figure(figsize=(7, 3), dpi=300)
plt.plot(range(tmax), mejores, 'ks--', linewidth=1, markersize=5)
plt.axhline(y = optimo, color = 'green', linewidth=3)
plt.xlabel('Paso')
plt.ylabel('Mayor valor')
plt.ylim(0.95 * min(mejores), 1.05 * optimo)
plt.savefig('p10p.png', bbox_inches='tight') 
plt.close()
print(mejor, (optimo - mejor) / optimo)
