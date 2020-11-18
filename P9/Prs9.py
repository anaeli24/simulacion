import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colorbar as colorbar
from matplotlib.colors import LinearSegmentedColormap
from math import fabs, sqrt, floor, log
import multiprocessing
from itertools import repeat
from os import popen
from random import uniform
import seaborn as sns
import pylab as pl

n = 50   #numero de particulas
dt=1

x = np.random.normal(size = n)    #crea los datos normales normalizaxion
y = np.random.normal(size = n)
c = np.random.normal(size = n)
m = np.random.normal(size = n) #Para agregar la masa
vx = np.random.normal(size = n)
vy = np.random.normal(size = n)
magv = (vx**2 + vy**2)**0.5

print(m)

#se normalizan las x para que sean entre 0 y 1

xmax = max(x)
xmin = min(x)

#de cada valor se resta el minimo y se divide entre (el rango) la x maxima menos la x minima
#para que el minimo sea 0 y el maximo 1 

x = (x - xmin) / (xmax - xmin) # de 0 a 1

#se normalizan las (cargas) "y" para que sean entre -1 y 1 
ymax = max(y)
ymin = min(y)
y = (y - ymin) / (ymax - ymin) 
cmax = max(c)
cmin = min(c)

c = 2 * (c - cmin) / (cmax - cmin) - 1 #Normalizacion entre -1 y 1
g = np.round(5 * c).astype(int)        #crea las G (carga)
cgravity=6.67e-11           #¿para la fuerza de coulumb que unidades se tomaron?
print(g)

p = pd.DataFrame({'x': x, 'y': y, 'c': c, 'g': g, 'm':m}) #hace un data para indicar donde van las x y las y
v = pd.DataFrame({'vx': vx, 'vy': vy, 'c': c, 'magv': magv, 'm':m})

#mecanica para los colores 
paso = 256 // 10
niveles = [i/256 for i in range(0, 256, paso)]
colores = [(niveles[i], 0, niveles[-(i + 1)]) for i in range(len(niveles))]
 
palette = LinearSegmentedColormap.from_list('tonos', colores, N = len(colores))

#hasta aqui es la primera parte del codigo cada particula tiene una carga una posicion en x y una carga en y,  las rojas tienen carga positiva, las azules carga negativa y las moradas es una carga neutra
#las particulas se crean de manera aleatoria , azules negativos, rojos positivos
#se crea la atraccion para signos opuestos y repulsion para signos iguales.
#sesuman los vectores de fuerza y se normalizan como si fuera una posicion
 
eps = 0.001                 #factor de descuento 
def fuerza(i):              #se crea la funcion fuerza, toma a cual particula hace los cambios 
    pi = p.iloc[i]          
    xi = pi.x           
    yi = pi.y                
    ci = pi.c               #carga que tienen
    mi = abs(pi.m)
    fx, fy = 0, 0           #se inicializan las fuerzas en 'x' y 'y' en cero
    fx1,fy1= 0, 0
    for j in range(n):       
        pj = p.iloc[j]      #se saca la particula en posicion j 
        cj = pj.c
        mj = abs(pj.m)
        dire = (-1)**(1 + (ci * cj < 0))    #saca la direccion y sacar las fuerzas
        dire2= (-1)**(1 + (mi < mj))
        dx = xi - pj.x
        dy = yi - pj.y
        factor = dire * fabs(ci * cj) / (sqrt(dx**2 + dy**2) + eps)
        factor2 =dire2 *(mi *  mj) / (sqrt(dx**2+ dy**2) +eps)
        fx -= dx * factor
        fy -= dy * factor
        fx1 -= dx * factor2
        fy1 -= dy * factor2
        print(fy,m,g)
    return (fx + fx1, fy +fy1)

def velocidades(i):
    pi = p.iloc[i]
    mi = abs(pi.m)
    #for j in range (n):
    fuerzai = fuerza(i)
    v = (fuerzai*dt)/(2*mi)       #calculo de velocidad
    return (v)
    
popen('rm -f p9p_t*.png') # borramos anteriores en el caso que lo hayamos corrido
tmax = 150
digitos = floor(log(tmax, 10)) + 1
fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = "rainbow")
fig.colorbar(pos, ax=ax)
plt.title('Estado inicial')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
fig.savefig('p9p_t0.png')
plt.close()


def actualiza(pos, fuerza, de):
    return max(min(pos + de * fuerza, 1), 0)
 
 
if __name__ == "__main__":
    vtotal=[]
    for t in range(tmax):
        with multiprocessing.Pool() as pool: # rehacer para que vea cambios en p
            f = pool.map(fuerza, range(n))
            vv = pool.map(velocidades, range(n))
            delta = 0.02 / max([max(fabs(fx), fabs(fy)) for (fx, fy) in f])   #normalizacion de delta
            #actualiza las posiciones en 'x' y 'y' 
            p['x'] = pool.starmap(actualiza, zip(p.x, [v[0] for v in f], repeat(delta)))
            p['y'] = pool.starmap(actualiza, zip(p.y, [v[1] for v in f], repeat(delta)))
            v['vx'] = pool.starmap(actualiza, zip(v.vx, [v[0] for v in vv], repeat(delta)))
            v['vy'] = pool.starmap(actualiza, zip(v.vy, [v[1] for v in vv], repeat(delta)))
            v['magv'] = pool.starmap(actualiza, zip(v.magv, [v[0] for v in vv], repeat(delta)))
            vtotal.append(v.magv)    #sacarun promedio de las velocidades
            print(v,vv,v.shape)
            #parte grafica
            
            fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
            pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = "rainbow")
            fig.colorbar(pos, ax=ax)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.xlim(-0.1, 1.1)
            plt.ylim(-0.1, 1.1)            
            plt.title('Paso {:d}'.format(t + 1))
            fig.savefig('p9p_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()

        
            N, bins, patches= plt.hist(v.magv)
            plt.xlabel('velocidades')
            jet = plt.get_cmap('jet', len(patches))
            for i in range(len(patches)):
              patches[i].set_facecolor(jet(i))
            plt.savefig('velocidad_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()
            
            N, bins, patches = plt.hist(v.m)
            plt.xlabel('Masas')     #la masa permanece constante
            jet = plt.get_cmap('jet', len(patches))
            for i in range(len(patches)):
              patches[i].set_facecolor(jet(i))
            plt.savefig('p9masa_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()

            N, bins, patches = plt.hist(v.c)   #las cargas permanecen constantes 
            plt.xlabel('Cargas')
            jet = plt.get_cmap('jet', len(patches))
            for i in range(len(patches)):
              patches[i].set_facecolor(jet(i))
            plt.savefig('p9carga_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()

            N, bins, patches = plt.hist(sum(vtotal)/tmax)
            plt.xlabel('Promedio de velocidades')
            jet = plt.get_cmap('jet', len(patches))
            for i in range(len(patches)):
              patches[i].set_facecolor(jet(i))
            plt.savefig('promediovelocidades.png')
            plt.close()

            df = sns.load_dataset('iris')
            sns_plotp = sns.pairplot(v)
            sns_plotp.savefig('tiempsov_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()
    
            df = sns.load_dataset('iris')
            sns_plotp = sns.pairplot(p)
            sns_plotp.savefig('tiempsop_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close


    
    

    

    
#popen('convert -delay 50 -size 300x300 p9p_t*.png -loop 0 p9p.gif') # requiere ImageMagick


