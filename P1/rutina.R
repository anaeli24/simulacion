#Shaffer.E Conversacion en Discord, #Solis.D conversacion por Discord, #Qui�onez.O conversacion por Discord.
buenos = data.frame()
malos = data.frame()
for (e in 5:10) {
l = 2**e
for (d in 1:8) {       #para 8 dimensiones
for (r in 1:50) {      #repeticiones 
pos = rep(0, d)
regresa = FALSE
for (t in 1:l) {                #para el tiempo
dd = sample(1:d, 1)
if (runif(1) < 0.5 ) {
pos [dd] = pos [dd] + 1 
} else { 
pos [dd] = pos [dd] - 1 
}
if (all(pos == 0)) { 
buenos = rbind(buenos, c(l, d, t))
regresa = TRUE
break
}
}
if(!regresa) { 
malos = rbind(malos, c(l, d))
}
}
}
}
names(buenos) = c("largo", "dim", "tiempo")
names(malos) = c("largo", "dim")
dim(buenos)
dim(malos)

names(buenos) = c("largo", "dim", "tiempo")
sink('buenos.txt')                            #Tellez.C Repositorio practica 1
print(buenos)
png('demo.png')
boxplot(formula = tiempo ~ dim, data =  buenos,
 col=rainbow(8, alpha=0.2),
border = rainbow(8, v=0.6)
)
graphics.off()
file.show('demo.png')


