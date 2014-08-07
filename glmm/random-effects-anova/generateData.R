#!/usr/bin/Rscript

### generate data for fixed effects ###
ngroups <- 5
nsample <- 10
popMeans <- c(50,40,45,55,60)
sigma <- 3

n <- ngroups * nsample
resid <- rnorm(n,0,sigma)
means <- rep(popMeans, rep(nsample,ngroups))
x <- rep(1:5,rep(nsample,ngroups))

## create design matrix and target variables
X <- as.matrix(model.matrix(~as.factor(x)-1))
y <- as.numeric(X%*% as.matrix(popMeans) + resid)

## plot the data
pdf("fe-svl-data.pdf",height=6,width=6)
boxplot(y~x,col="grey",xlab="population",ylab="SVL",main="",las=1)
dev.off()

## write to outfile
xyFrame <- data.frame(x,y)
write.csv(xyFrame,file="fe-svl.csv",row.names=FALSE)

### generate data for random effects ###
npop <- 10 
nsample <- 12
n <- npop * nsample
popGrandMean <- 50
popSd <- 5
popMeans <- rnorm(n=npop,mean=popGrandMean,sd=popSd)
sigma <- 3

resid <- rnorm(n,0,sigma)
x <- rep(1:npop, rep(nsample, npop))

## create the design matrix and target variables
X <- as.matrix(model.matrix(~ as.factor(x)-1))
y <- as.numeric(X %*% as.matrix(popMeans)+resid) 

# Plot of generated data
pdf("re-svl-data.pdf",height=6,width=6)
boxplot(y~x, col="grey", xlab="population", ylab="SVL",main="", las=1)
dev.off()

## write to outfile
xyFrame <- data.frame(x,y)
write.csv(xyFrame,file="re-svl.csv",row.names=FALSE)
print("done.")
