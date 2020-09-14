paso = function(pos,dim){
    d=sample(1:dim,1);
    if (runif(1)<0.5) {
        pos[d]=pos [d]-1;
    }else{
         pos[d]=pos[d]+1;
     }
     return(pos);
}

dim=8
largo=50
pos=rep(0,dim)
for(t in 1:largo) {
   pos=paso(pos,dim)
   cat(pos, '\n')
}
caminata <-function(dim, dur, dist){
   pos <- rep (0,dim)
   mayor <- 0
   for (t in 1:dur){
       cambiar <- sample(1:dim,1)
       cambio <- 1
       if (runif(1)<0.5) {
           cambio <- -1
       }
       pos[cambiar] <-pos[cambiar] + cambio
       d <- dist (pos) 
       if (d > mayor) {
           mayor <- d
       }
    }
    return(mayor)
}
euclideana <- function (p1 , p2){
    return(sqrt(sum((p1-p2)**2)))
}

manhattan <- function (p1, p2){
    return(sum(abs(p1-p2)))
}

ed.orig <- function(p){
    dimension <- length (p)
    origen <- rep (0, dimension)
    return(euclideana(p, origen))
}

md.orig <-function (p)'{
    dimension <- length (p)
    origen <- rep (0, dimension)
    return(manhattan (p,origen))
}
registro = data.frame()
dimension = 8
potencia = 10
for (pot in 5:potencia){
  duracion <- 2^potencia
  for (dim in 1:dimension) {
    
    datos = numeric()
    repeticiones = 50
    for (replica in 1:repeticiones) {
      resultado = FALSE
      pos <- rep(0, dim)
      for (t in 1:duracion) {
        modificar = sample(1:dim, 1)
        if (runif(1) < 0.5) {
          pos[modificar] =  pos[modificar] + 1
        } else {
          pos[modificar] =  pos[modificar] - 1
        }
        if (all(pos == 0)) {
          resultado = TRUE
          break
        }
      }
      datos = c(datos, resultado)
}
  porc = 100 * sum(datos) / repeticiones
  registro = rbind(registro, c(pot, porc, dim))
  }
}
names(registro) = c("pot", "porc", "dim")
sink('registro.txt')
print(registro)
sink()
png("pr1sim.png", width=800, height=800, units='px')
par(cex.lab=2) 
par(cex.axis=2) 
boxplot(porc ~ dim, 
data =  registro,
xlab="Dimensi\u{F3}n",
ylab="Porcentaje de regreso al punto de origen",
col=rainbow(8, alpha=0.2),
border = rainbow(8, v=0.6)
)
