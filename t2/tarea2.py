#Shcaeffer,E cambio en el codigo
#Solis,D., Quiñones, O, en apoyo para modificaciones en el codigo
import numpy as np 
from random import uniform,random 
import matplotlib.cm as cm
import matplotlib.pyplot as plt


dim = 20               #definir 20x20
num = dim**2
#for prob in [0.1-0.9]:
prob = uniform(0.1,0.9)
valores = [round(random())< prob for i in range(num)]   #prob
actual = np.reshape(valores, (dim, dim))
#hasta aqui termina la declaracion de variables y librerias
#inicia depclaracion de modulos o funciones
def mapeo(pos):
    fila = pos // dim
    columna = pos % dim
    return actual[fila, columna]

assert all([mapeo(x) == valores[x]  for x in range(num)])

def paso(pos):
    fila = pos // dim
    columna = pos % dim
    vecindad = actual[max(0, fila - 1):min(dim, fila + 2),
                      max(0, columna - 1):min(dim, columna + 2)]
    return 1 * (np.sum(vecindad) - actual[fila, columna] == 3)

print(actual)
#termina la parte modular
#inicia el programa principal
if __name__ == "__main__":
    fig = plt.figure()
    plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
    fig.suptitle('Estado inicial')
    plt.savefig('p2_0_.png')  #genera archivo png
    plt.close()
#hasta aqui termina la parte grafica
    lista_actual=[]                 #modf
    lista_posx=[]             #vacia
    lista_posy=[]
    listaiter=[]
    salida=open('vivos.txt','w')        #para crear doc de texto con las posiciones
    for iteracion in range(50): #num de repeticiones
        print("Iter", iteracion)
        valores = [paso(x) for x in range(num)]   #regla de la vida
        vivos = sum(valores)
        print(iteracion, vivos)
        if vivos == 0:
            print('# Game Over.')
            break;                           #rompe el for
        actual = np.reshape(valores, (dim, dim))
        lista_actual.append(actual)
        print(actual)
        mvivos=np.equal(actual,1)
        #print(mvivos)
        for n in range(dim):
            for m in range (dim):
                if mvivos[n,m]==True:
                   print(n,m,iteracion)
                   lista_posx.append(n)                     # para poder llenar el text
                   lista_posy.append(m)
                   listaiter.append(iteracion)
                   salida.write("%f %f %f \n" % (n,m,iteracion))           
        fig = plt.figure()
        plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)     #para las imagenes del gif
        fig.suptitle('Paso {:d}'.format(iteracion + 1))
        plt.savefig('p2_t{:d}_p.png'.format(iteracion + 1))  
        plt.close()
    salida.close()
    plt.plot(lista_posx,lista_posy,'o')           #graficar las posiciones mapeadas
    plt.xlabel('x')                               #manual mathplotlib
    plt.ylabel('y')
    for i,txt in enumerate (listaiter):
        plt.annotate(str(txt),(lista_posx[i],lista_posy[i]))
    plt.show()
   
