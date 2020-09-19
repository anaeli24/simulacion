experimento = function(largo) {
pos = 0
for (paso in 1:largo) {
if (runif(1) < 0.5 ) {
pos = pos + 1
} else { 
pos = pos - 1 
}
if (pos == 0) {
return(paso)
}
}
return(0)
}

for (p in 1:largo) {
for (d in 1:8) {
for (r in 1:50) { 
cat(p, d, r, '\n')
}
}
}

for (p in 1:largo) {
for (d in 1:8) {
for (r in 1:50) {
pos = rep(0, d)
for (t in 1:p) { 
dd = sample(1:d, 1)
if (runif(1) < 0.5 ) {
pos[dd] = pos [dd] + 1 
} else { 
pos[dd] = pos [dd] - 1 
}
if (all(pos == 0)) { 
cat(p, d, r, t, '\n')
break
}
}
cat(p, d, r, 0, '\n')
}
}
}

regresaron = data.frame()
escaparon = data.frame()
for (p in 1:largo) {
for (d in 1:8) {
for (r in 1:50) {
pos = rep(0, d)
for (t in 1:p) { 
dd = sample(1:d, 1)
if (runif(1) < 0.5 ) {
pos [dd] = pos [dd] + 1 
} else { 
pos [dd] = pos [dd] - 1 
}
if (all(pos == 0)) { 
regresaron = rbind(regresaron, c(p, d, t))
break
}
}
escaparon = rbind(escaparon, c(p, d))
}
}
}
names(regresaron) = c("largo", "dim", "tiempo" )
names(escaparon) = c("largo", "dim")
head(regresaron)
head(escaparon)

regresaron = data.frame()
escaparon = data.frame()
for (e in 5:10) {
p = 2**e
for (d in 1:8) { 
for (r in 1:50) {
pos = rep(0, d)
for (t in 1:p) { 
dd = sample(1:d, 1)
if (runif(1) < 0.5 ) {
pos [dd] = pos [dd] + 1 
} else { 
pos [dd] = pos [dd] - 1 
}
if (all(pos == 0)) { 
regresaron = rbind(regresaron, c(p, d, t))
break
}
}
escaparon = rbind(escaparon, c(p, d))
}
}
}
names(regresaron) = c("largo", "dim", "tiempo")
names(escaparon) = c("largo", "dim")
dim(regresaron)
dim(escaparon)

regresaron = data.frame()
escaparon = data.frame()
for (e in 5:10) {
p = 2**e
for (d in 1:8) { 
for (r in 1:50) {
pos = rep(0, d)
regresa = FALSE
for (t in 1:p) { 
dd = sample(1:d, 1)
if (runif(1) < 0.5 ) {
pos [dd] = pos [dd] + 1 
} else { 
pos [dd] = pos [dd] - 1 
}
if (all(pos == 0)) { 
regresaron = rbind(regresaron, c(p, d, t))
regresa = TRUE
break
}
}
if(!regresa) { 
escaparon = rbind(escaparon, c(p, d))
}
}
}
}
names(regresaron) = c("largo", "dim", "tiempo")
names(escaparon) = c("largo", "dim")
dim(regresaron)
dim(escaparon)

names(regresaron) = c("largo", "dim", "tiempo")
sink('regrearon.txt')
print(regresaron)
sink()
png("pr1sim.png", width=800, height=800, units='px')
par(cex.lab=2) 
par(cex.axis=2) 
boxplot(tiempo~ dim 
data =  regresaron,
xlab="Dimensi\u{F3}n",
ylab="tiempo de regreso",
col=rainbow(8, alpha=0.2),
border = rainbow(8, v=0.6)
)
dev.off()
