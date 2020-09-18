experimento = function(largo) {
 pos = 0
 for (paso in 1:largo) {
 if (runif(1) < 0.5 ) {
 pos = pos +1
 } else { 
 pos = pos - 1 
 }
 if (pos == 0) {
 return(paso)
 }
 }
 return(0)
}
largo = 100
experimento(largo)
experimento(largo)
experimento(largo)
experimento(largo)
experimento(largo)
experimento(largo)
replicas = numeric()
for (r in 1:30) {
replicas = c(replicas, experimento(largo))
 }
replicas
replicas[replicas == 0]
replicas[replicas == 0]
replicas[replicas == 0]
replicas[replicas == 0]
replicas[replicas == 0]
replicas[replicas == 0]
replicas[replicas > 0]
length(replicas[replicas == 0])
buenos = replicas [replicas > 0]
min(buenos)
max(buenos)
mean(buenos)
> png('demo.png')
> boxplot(buenos)
> graphics.off()