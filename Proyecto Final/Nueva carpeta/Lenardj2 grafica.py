#-*- coding: utf8 -*-
#from Numeric import *
from math import *
from time import clock
from vpython import *
from random import uniform
from numpy import *
import pickle
import matplotlib.pyplot as plt 
############# DECLARACIÓN DE PARÁMETROS FÍSICOS DE LA SIMULACIÓN ##############
npl=4
np=int(pow(npl,3))    # número de partículas del sistema
rho=1.0               # densidad del fluido simucaion de agua
L=pow((np/rho),1./3.) # longitud de la celda unitaria
radio=L/np            # radio de la esfera
vinicial=1.0           # velocidad inicial
masa=18.0              # masa de la partícula al agua
rc=L/2.0               # radio de corte
tgrad=1.5043          # temperatura de termalización
epsilon=1.0
dt=1.e-5              # paso de tiempo
tiempo=100000          # tiempo total medio de número de iteraciones
pintervalo=1000        # número del periodo de iteraciones
ntermal=5000          # número de iteracines de termalización
print ("L=", L, "np=", np, "T=", tgrad, "R=", radio)

###############################################################################
################## PARTE GRÁFICA DE LA SIMULACIÓN #############################
tvp=100               # tiempo gráfico de visualización
Lmin=radio            # ancho de las tapas de la celda
Ly=L/2. + Lmin        # longitud grafica del lado de la celda 
Lx=L/2. + Lmin        # longitud grafica del lado de la celda 
Lz=L/2. + Lmin        # longitud grafica del lado de la celda 
Lb= 2.*(L/3.)         # longitud de los ejes de referencia
win=600               # ancho de la ventana
angulo=1.5            # rango de visualización para camara
thk = 0.001           # grosor de la pared
Rejes = 0.05          # radio de ejes de la celda

############### DECLARACIÓN DEL SISTEMA DE REFERENCIA #########################
scene = canvas(title="Líquidio L-J", width=win, height=win, x=1000, y=0, center=vector(0,0,0)) 
axisX = arrow(pos=vector(0,0,0), axis=vector(Lb,0,0), shaftwidth=0.001, color=color.red)
axisY = arrow(pos=vector(0,0,0), axis=vector(0,Lb,0), shaftwidth=0.001, color=color.blue)
axisZ = arrow(pos=vector(0,0,0), axis=vector(0,0,Lb), shaftwidth=0.001, color=color.green)
label(pos=vector(Lb,0,0), text='x')
label(pos=vector(0,Lb,0), text='y')
label(pos=vector(0,0,Lb), text='z')

######################## SE CREA LA CELDA UNITARIA ############################
xaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(Lx,-Ly,-Lz)], color=color.white, radius=Rejes)
yaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(-Lx,Ly,-Lz)], color=color.white, radius=Rejes)
zaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(-Lx,-Ly,Lz)], color=color.white, radius=Rejes)
xaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(-Lx,Ly,Lz), vector(-Lx,-Ly,Lz), vector(Lx,-Ly,Lz)], color=color.white, radius=Rejes)
yaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(Lx,-Ly,Lz), vector(Lx,-Ly,-Lz), vector(Lx,Ly,-Lz)], color=color.white, radius=Rejes)
zaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(Lx,Ly,-Lz), vector(-Lx,Ly,-Lz), vector(-Lx,Ly,Lz)], color=color.white, radius=Rejes)

####################### SE CREAN LAS ESFERAS Y SE #############################
####### DECLARAN LAS LISTAS PARA VELOCIDADES, POSICIONES Y ACELERACIONES ######
bolas=[]
listavel=[] 
listapos=[]
R=[]
m=[] #
maxV=vinicial
for i in arange(np):
        bola = sphere(color = color.cyan, radius=radio)
        vel = vector(maxV*uniform(-1,1), maxV*uniform(-1,1),maxV*uniform(-1,1))
        listavel.append(vel)
        posi = vector(uniform(-L/2., L/2.), uniform(-L/2., L/2.),uniform(-L/2., L/2.))
        listapos.append(posi) 
        bola.pos = posi
        bolas.append(bola)
        R.append(radio)
        m.append(masa)#
v0=array(listavel)
r0=array(listapos)      

###############################################################################
############ DECLARACIÓN DE FUNCIONES NECESARIAS PARA EL PROGRAMA #############
############### MÓDULO DE DETECCIÓN DE COLISIONES ENTRE ESFERAS ###############
def choques():
    rs = array([vector(0.0, 0.0, 0.0) for i in range(np)])
    vs = array([vector(0.0, 0.0, 0.0) for i in range(np)])    
    for i in range(np-1):
        for j in range(i+1,np):
            distancia = mag(r[i] - r[j])
            # checar colision
            if distancia < (R[i]+R[j]):
                # vector unitario en direccion de la colision
                direccion = norm(r[j]-r[i])
                vi=dot(v[i], direccion)
                vj=dot(v[j], direccion)
                # velocidad de choque
                intercambio = vj - vi
                # intercambio de momento
                v[i] = v[i] + intercambio*direccion
                v[j] = v[j] - intercambio*direccion
                # se ajusta posicion
                traslape1 = 2.0*R[i] - distancia
                traslape2 = 2.0*R[j] - distancia
                r[i] = r[i] - traslape1*direccion
                r[j] = r[j] + traslape2*direccion
    rs = r
    vs = v#
    return rs, vs

###################### DECLARACIÓN DE LA FUNCIÓN ANINT ########################
#u=vector(0.0,0.0,0.0)
def anint(posi):
    if posi.x < 0.5: # cambia coomponente de v
             #print(posi.x,'anintx')
             posi.x = 0.0
    elif posi.x < -0.5:
             #print(posi.x,'anintx')
             posi.x=-1.0
    else:
             #print(posi.x,'anintx')
             posi.x=1.0
    if posi.y < 0.5: # cambia coomponente de v
             #print(posi.y,'aninty')
             posi.y = 0.0
    elif posi.y < -0.5:
             #print(posi.y,'aninty')
             posi.y=-1.0
    else:
             #print(posi.y,'aninty')
             posi.y=1.0
    if posi.z < 0.5: # cambia coomponente de v
             #print(posi.z,'anintz')
             posi.z = 0.0
    elif posi.z < -0.5:
             #print(posi.z,'anintz')
             posi.z=-1.0
    else:
             #print(posi.z,'anintz')
             posi.z=1.0
    return vector(posi.x,posi.y,posi.z) 
     
        

################### DEFINICIÓN DE LA FUERZA LENNARD-JONES ######################
def FuerzaLJ(r, i, j):
    if r < rc :
        S = (24.0*epsilon)*(2.0/pow(r,13)-1.0/pow(r,7))
        return S
    else :
        return 0.0
################################## MÓDULO DE FUERZAS ###########################
def cfuerzas():
    a=array([vector(0.0,0.0,0.0) for i in range(np)])
    for i in range(np-1):
        for j in range(i+1,np):
            rij = r[i]-r[j]
            #print(rij)
            rij = rij-L*anint(rij/L)
            norma_rij = mag(rij)
            FLJij = FuerzaLJ(norma_rij,i,j)
            ruij = rij/norma_rij
            a[i] = a[i] + (FLJij/m[i])*ruij
            a[j] = a[j] - (FLJij/m[i])*ruij
    return a
############################# MÓDULO DE TERMALIZACIÓN ##########################
def termalizacion():
    enervk=0.0
    for k in range(np):
        vel2=v[k].x*v[k].x+v[k].y*v[k].y+v[k].z*v[k].z
        enervk=enervk+0.5*m[k]*vel2
    escala=sqrt((3.0*tgrad)/(2.0*enervk))
    return escala, enervk

################################################################################
############# PARTE PRINCIPAL DEL PROGRAMA (ALGORITMO DE VERLER) ###############
r=r0                                # declaración de posiciones iniciales
v=v0                                # declaración de velocidades iniciales
PDE=choques                         # corrección para las posiciones iniciales   
a=cfuerzas()                        # declaración de aceleraciones iniciales para calcular velocidad inicial 
t=0
l=ntermal
tt=clock()
listattt=[]
listah=[]
ecinet=[]
while t < tiempo:                     # ciclo sobre el tiempo
    r = r+v*dt+0.5*(a*dt**2)        # verlet para posiciones   (mover)  resuelve las posiciones
    for i in range(np):
        r[i] = r[i]-anint(r[i]/L)*L # imagen mínima            (mover)   checa que no se salgan de la celda  
    v = v+0.5*(a*dt)                # cálculo de velocidades   (mover)   optiene las velocidades apartir de la aceleracion por la segunda ley de newton     
    a = cfuerzas()                  # cálculo de aceleraciones (fuerzas)  
    v = v+0.5*(a*dt)                # cálculo de velocidades   (velocidades)
    tescala = termalizacion()       # termalizacion
    v = tescala*v
    if 0 <= t <= 25 :
        for i in arange(len(bolas)):    # gráfica de posiciones finales
            bolas[i].pos=r[i]
	#print ("ri=", r[np/2], "vi=", v[np/2], "ai=", a[np/2])

    t = t+1                         # conteo de lapsos tiempo de la corrida 
    if t == l :
        archivo1=open("Lenard-Jones-R"+str(np)+str(radio)+str(epsilon)+str(t)+".pkl","wb")
        pickle.dump(r,archivo1)
        archivo1.close()
        archivo2=open("Lenard-Jones-V"+str(np)+str(radio)+str(epsilon)+str(t)+".pkl","wb")
        pickle.dump(r,archivo2)
        archivo2.close()
        for i in arange(len(bolas)):    # gráfica de posiciones finales
            bolas[i].pos=r[i]

        ttt = clock() - tt 
        print ('tiempo=', ttt, 'segundos despues de', t, 'iteraciones')
        tescala,ecinetica = termalizacion()       # termalizacion
        v = tescala*v
        ecinet.append(ecinetica)
        listat.append(l*dt)
        listattt.append(ttt)
        listah.append(l)
        l = l + pintervalo

tt = clock() - tt

plt.plot(listah, listattt)
plt.ylabel('Tiempo')
plt.xlabel('Iteraciones')
plt.show()
plt.savefig('tiempodecalculo.png')
plt.close()

plt.plot(listah, ecinet)
plt.ylabel('Tiempo')
plt.xlabel('Temperatura')
plt.savefig('ecineticavstiempo.png')
plt.show()
plt.close()

plt.plot(listah, ecinet)
plt.ylabel('Temperatura')
plt.xlabel('Tiempo')
plt.savefig('ecineticavstiempoaa.png')
plt.show()
plt.close()

#print '%0.1f' % tt
#print 'tiempo aproximado en segundos ',tt
