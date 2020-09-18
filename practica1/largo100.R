registro = data.frame()
dimension = 8
potencia = 10
largo=100
for (pot in 5:potencia){
  largo = 2^potencia
  for (dim in 1:dimension) {
    
   datos = numeric()
    repeticiones = 50
    for (replica in 1:repeticiones) {
      resultado = FALSE
      pos = rep(0, dim)
      for (paso in 1:largo) {
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
}
}
png("100.png", width=800, height=800, units='px')
par(cex.lab=2) 
par(cex.axis=2) 
boxplot(datos ~ dim, 
data =resultado,
xlab="Dimensi\u{F3}n",
ylab="tiempo regreso al origen",
col=pastel2, alpha=0.2),
border = pastel2, v=0.6)
)
dev.off()