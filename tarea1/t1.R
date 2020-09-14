paso = function(pos,dim){
    d=sample(1:dim,1);
    if (runif(1)<0.5) {
        pos[d]=pos [d]-1;
    }else{
         pos[d]=pos[d]+1;
     }
     return(pos);
}

dim=3
largo=12
pos=rep(0,dim)
for(t in 1:largo) {
   pos=paso(pos,dim)
   cat(pos, '\n')
}

