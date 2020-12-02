library(ggplot2) 
pick.one <- function(x) {
    if (length(x) == 1) {
        return(x)
    } else {
        return(sample(x, 1))
    }
}
 
poli <- function(maxdeg, varcount, termcount) { generar un polinomio, cual es el grado maxino, cuantas variables y cuantos terminos quiere
    f <- data.frame(variable=integer(), coef=integer(), degree=integer())  #lo representa cn un dataframe
    for (t in 1:termcount) {
        var <- pick.one(1:varcount)  #cual variable entra
        deg <- pick.one(1:maxdeg)   #en que grado aparece
        f <-  rbind(f, c(var, runif(1), deg))  #elige un coeficiente al azar
    }
    names(f) <- c("variable", "coef", "degree")  #los mete al data
    return(f)
}
 
eval <- function(pol, vars, terms) {  # toma el polinomio, luego los valores de as variables y da los terminos, los evalua y los suma para q el valor de la variable sea lo q termine de los vars
    value <- 0.0
    for (t in 1:terms) {
        term <- pol[t,]
        value <-  value + term$coef * vars[term$variable]^term$degree
    }
    return(value)
}
 
domin.by <- function(target, challenger) {
    if (sum(challenger < target) > 0) {
        return(FALSE) # hay empeora
    } # si no hay empeora, vemos si hay mejora
    return(sum(challenger > target) > 0)
}
##########se agrego al codigo base###########
verify <- function(i){
 val <- c()
 for (j in 1:k){
   val <-c(val, eval(obj[[j]],sol[i, ], tc))
   }
   return(val)
}
prop <- function(i){
  return(list(poli(vc, md, tc)))
}
############## se agregaron al codigo base########

vc <- 4  #cantidad de variables posibles  va primero
md <- 3  #Mayor grado permitido va segundo
tc <- 5  #cuantos terminos se generan para el polinomio va tercero
funciones <- seq (2,12,by=1)
#k <- 2 # cuantas funciones objetivo
for (k in funciones){
  for (replicas in 1:30){
obj <- list() #crear objetivos
for (i in 1:k, prop) {
    obj[[i]] <- poli(vc, md, tc)
}
minim <- (runif(k) > 0.5)
sign <- (1 + -2 * minim)
n <- 200 # cuantas soluciones aleatorias
sol <- matrix(runif(vc * n), nrow=n, ncol=vc)  #matriz cn n renglones y vc columnas
val <- matrix(rep(NA, k * n), nrow=n, ncol=k)  #matriz para crear el espacio
for (i in 1:n) { # evaluamos las soluciones # evaluamos las soluciones para cada solucion y para cada objetivo
    for (j in 1:k, verify) { # para todos los objetivos
        val[i, j] <- eval(obj[[j]], sol[i,], tc)
    }
}
mejor1 <- which.max(sign[1] * val[,1])  #mejor valor para uno
mejor2 <- which.max(sign[2] * val[,2]) #mejor valor para el otro
cual <- c("max", "min")  #cual es el mejor
######parte grafica#################
xl <- paste("Primer objetivo (", cual[minim[1] + 1], ")", sep="")
yl <- paste("Segundo objetivo (", cual[minim[2] + 1], ")", sep="")
png("p11_init.png")
plot(val[,1], val[,2], xlab=xl, ylab=yl, main="Ejemplo bidimensional")
graphics.off()
#############grafica2#########
png("p11_mejores.png")
plot(val[,1], val[,2], xlab=paste(xl, "mejor con cuadro azul"),
     ylab=paste(yl,"mejor con bolita naranja"),
     main="Ejemplo bidimensional")
points(val[mejor1, 1], val[mejor1, 2], col="blue", pch=15, cex=1.5)
points(val[mejor2, 1], val[mejor2, 2], col="orange", pch=16, cex=1.5)
graphics.off()
######empieza la 3 ##########
no.dom <- logical()
dominadores <- integer()
for (i in 1:n) {
    d <- logical()
    for (j in 1:n) {
        d <- c(d, domin.by(sign * val[i,], sign * val[j,], k))
    }
    cuantos <- sum(d)
    dominadores <- c(dominadores, cuantos)
    no.dom <- c(no.dom, cuantos == 0) # nadie le domina
}
frente <- subset(val, no.dom) # solamente las no dominadas

######################    Algoritmo genetico    ########################
library(testit)

########### funcion mutacion ###########
mutacion <- function(sol, vc) {
  pos <- sample(1:vc, 1)
  mut <- sol
  delta <- 0.1
  mut[pos] <- (sol[pos]) * delta
  return(mut)
}

muta <- function(i){
  if (runif(1) < pm) {
    return(mutacion(sol[i,], vc))
  }
  else{
    return(sol[i,])
  }
}
########### funcion reproduccion ############
reproduccion <- function(x, y, vc) {
  pos <- sample(2:(vc-1), 1)
  xy <- c(x[1:pos], y[(pos+1):vc])
  yx <- c(y[1:pos], x[(pos+1):vc])
  return(c(xy, yx))
}


cluster <- makeCluster(detectCores() - 1)

##########  parametros  ###########################
pm <- 0.05 # Probabilidad de mutación
rep <- 50 # Cantidad de veces que se realiza reproduccion
tmax <- 100 # Cantidad de generaciones


####################  Inicia genetico ############################
for (iter in 1:tmax) {
 ############### fase mutacion ####################    
  clusterExport(cluster, "pm")
  clusterExport(cluster, "vc")
  clusterExport(cluster, "sol")
  clusterExport(cluster, "mutacion")
  clusterExport(cluster, "muta")
  
  sol <- t(parSapply(cluster, 1:n,muta))
  
  ################ fase reproduccion  ##########################
  for (i in 1:rep) {
    padres <- sample(1:n, 2, replace=FALSE)
    hijos <- reproduccion(sol[padres[1],], sol[padres[2],], vc)
    sol <- rbind(sol, hijos[1:vc]) # primer hijo
    sol <- rbind(sol, hijos[(vc+1):(2*vc)]) # segundo hijo
  }
  
  ############### fase evalua ######################
  val <- matrix(rep(NA, k * nrow(sol)), nrow=nrow(sol), ncol=k)
  clusterExport(cluster, "evalua")
  clusterExport(cluster, "eval")
  clusterExport(cluster, "obj")
  clusterExport(cluster, "sol")
  clusterExport(cluster, "tc")
  clusterExport(cluster, "k")
  clusterExport(cluster, "n")
  
  val <- parSapply(cluster, 1:nrow(sol), evalua)
  val <- t(val)
  
  
  no.dom <- logical()
  dom <- logical()
  dominadores <- integer()
  
  clusterExport(cluster, "dominado")
  clusterExport(cluster, "domin.by")
  clusterExport(cluster, "val")
  clusterExport(cluster, "sign")
  clusterExport(cluster, "k")
  clusterExport(cluster, "n")
  
  d <- parSapply(cluster, 1:nrow(sol), dominado)
  
  for(x in 1:nrow(sol)){
    cuantos <- sum(d[,x])
    dominadores <- c(dominadores, cuantos)
    no.dom <- c(no.dom, cuantos == 0) # nadie le domina
    dom <- c(dom, cuantos != 0)
  }
  
  
  frente_sol <- subset(sol, no.dom) # solamente las no dominadas
  dominadas <- subset(sol, dom)
  frente <- subset(val, no.dom) # solamente las no dominadas
  domi <- order(dominadores)
  domi <- domi[1:n]
  
  sol <- sol[domi,]
  val <- val[domi,]
  digitos <- floor(log(tmax, 10)) + 1
  tl <- paste0(iter, "", sep="")
  while (nchar(tl) < digitos) {
    tl <- paste("0", tl, sep="")
  }
  
  png(paste0("R2AG",tl,".png"))
  plot(val[,1], val[,2], xlab=xl, ylab=yl, main=paste("Generación",iter))
  points(frente[,1], frente[,2], col="green", pch=16, cex=1.5)
  graphics.off()
  
  ####################################################################################    
  if(nrow(frente) == n)
  {
    break;
  }
}
stopCluster(cluster)

###########para el boxplot#######3
png("p200.png",, height = 10, width = 20, units = "cm", res = 900)
ggplot(datos, aes(x=k, y=Porcentaje, fill=k)) + geom_violin(scale = "width") + 
  scale_fill_brewer(palette="RdPu")+ theme_light() + 
  geom_boxplot(inherit.aes = TRUE, fill="blue", color="black", width = 0.1)
graphics.off()
#######analisis estadistico#############3
a <- shapiro.test(datos$Porcentaje)
a$p.value
a$p.value < 0.05
b <- kruskal.test(datos$Porcentaje~datos$k)
b$p.value
b$p.value < 0.05
c <- pairwise.wilcox.test(datos$Porcentaje, datos$k, p.adjust.method = "none")
c$p.value
c$p.value < 0.05
