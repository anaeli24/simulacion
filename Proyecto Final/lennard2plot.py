#-*- coding: utf8 -*-
from math import *
from time import clock
from vpython import *
from random import uniform
import pickle
import matplotlib.pyplot as plt 
##CONSTANTES FISICAS 
npl=4
np=int(pow(npl,3))
rho=1.0
L=pow((np/rho),1./3.)
radio=L/float(np)
vinicial=1.0
masa=18.0
rc=L/2.
dt=1.e-5
tiempo=10000
tgrad=1.5043
h0=4999
ntermal=5000
nombre1='Lenard-Jones-R640.062499999999999991.0'
nombre2='Lenard-Jones-V640.062499999999999991.0'
print ('np=', np, 'L=', L, 'T=', tgrad, 'radio=', radio)
m=[masa for i in range (np)]
###############################################################################
################## Parte gráfica de la simulación #############################
##################### Declaración de parámetros gráficos ######################
lc=L
tvp=50
Lmin=radio          ## ANCHO DE LAS TAPAS DE LA CELDA
Ly=lc/2. + Lmin     ## LONGITUD DEL LADO DE LA CELDA GRAFICA
Lx=lc/2. + Lmin     ## LONGITUD DEL LADO DE LA CELDA GRAFICA
Lz=lc/2. + Lmin     ## LONGITUD DEL LADO DE LA CELDA GRAFICA
Lb= 2.*(lc/3.)      ## LONGITUD EJES DE REFERENCIA
win=600             ## ANCHO DE LA VENTANA
angulo=1.5          ## RANGO VISUALIZACION CAMARA
thk = 0.001         ## GROSOR PARED
Rejes = 0.05        ## RADIO EJES CELDA

###############################################################################
############### Declaración del sistema de referencia #########################
scene = canvas(title="Liquidio L-J", width=win, height=win, x=1000, y=0, center=vector(0,0,0))
 
axisX = arrow(pos=vector(0,0,0), axis=vector(Lb,0,0), shaftwidth=0.001, color=color.red)
axisY = arrow(pos=vector(0,0,0), axis=vector(0,Lb,0), shaftwidth=0.001, color=color.blue)
axisZ = arrow(pos=vector(0,0,0), axis=vector(0,0,Lb), shaftwidth=0.001, color=color.green)
label(pos=vector(Lb,0,0), text='x')
label(pos=vector(0,Lb,0), text='y')
label(pos=vector(0,0,Lb), text='z')

xaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(Lx,-Ly,-Lz)], color=color.white, radius=Rejes)
yaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(-Lx,Ly,-Lz)], color=color.white, radius=Rejes)
zaxis = curve(pos=[vector(-Lx,-Ly,-Lz), vector(-Lx,-Ly,Lz)], color=color.white, radius=Rejes)
xaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(-Lx,Ly,Lz), vector(-Lx,-Ly,Lz), vector(Lx,-Ly,Lz)], color=color.white, radius=Rejes)
yaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(Lx,-Ly,Lz), vector(Lx,-Ly,-Lz), vector(Lx,Ly,-Lz)], color=color.white, radius=Rejes)
zaxis2 = curve(pos=[vector(Lx,Ly,Lz), vector(Lx,Ly,-Lz), vector(-Lx,Ly,-Lz), vector(-Lx,Ly,Lz)], color=color.white, radius=Rejes)

############################# MÓDULO DE TERMALIZACIÓN ##########################
###vs = [vector(0.0, 0.0, 0.0) for i in range(np)]
###v= vs
def termalizacion():
    enervk=0.0
    for k in range(np):
        vel2=v[k].x*v[k].x+v[k].y*v[k].y+v[k].z*v[k].z
        enervk=enervk+0.5*m[k]*vel2
    escala=sqrt((3.0*tgrad)/(2.0*enervk))
    return escala,enervk
############################################################################
############ DECLARACION DE VELOCIDADES Y POSICIONES INICIALES ############# 
############################################################################
#rpos = open('canonico_'+str(rho)+'_'+str(np)+'_rinicial.pkl', 'rb')
#r0 = pickle.load(rpos)
#rpos.close()
##vpos = open(nombre'_'+str(rho)+'_'+str(np)+'_vinicial.pkl', 'rb')
##v0 = pickle.load(vpos)
##vpos.close()
####m=[] 
bolas=[]
for i in range(np):
    bola = sphere(color = color.cyan, radius=radio)
    bola.pos = vector(0.0,0.0,0.0)
    bolas.append(bola)
    ###m.append(masa)#

################### CICLO SOBRE EL TIEMPO################################################
t=0.0
pintervalo=1000
h=h0
tt=clock()
ecinet=[]
listat=[]
listattt=[]
listah=[]
l=ntermal
while t < tiempo:
    rate(tvp)
    t = t + dt
    h=h+1
    l = l + pintervalo
    if h% pintervalo ==0:
        rpos = open(nombre1+str(l)+'.pkl','rb')
        posarray=pickle.load(rpos)
        rpos.close()
        ttt = clock() - tt 
        print ('tiempo=', ttt, 'segundos despues de', t, 'iteraciones')
        listattt.append(ttt)
        listah.append(l) 
        vpos = open(nombre2 + str(l) + '.pkl','rb')
        v=pickle.load(vpos)
        vpos.close()
        tescala,ecinetica = termalizacion()       # termalizacion
        v = escala*v
        ecinet.append(ecinetica)
        listat.append(l*dt)
        for i in arange(np):
            bolas[i].pos=posarray[i]
tt = clock() - tt

plt.plot(listat, ecinet)
plt.ylabel('Tiempo')
plt.xlabel('Temperatura')
plt.savefig('ecineticavstiempo.png')
plt.show()
plt.close()
