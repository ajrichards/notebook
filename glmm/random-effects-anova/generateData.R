#!/usr/bin/Rscript
## this example is adopted from Marc Kery's Book
## Introduction to WinBUGS for ecologists (pp119)

## basic variables
## sigma is the residual standard deviation
ngroups <- 5
nsample <- 10
popMeans <- c(50,40,45,55,60)
sigma <- 3

n <- ngroups * nsample
resid <- rnorm(n,0,sigma)
means <- rep(popMeans, rep(nsample,ngroups))
x <- rep(1:5,rep(nsample,ngroups))

## create design matrix
X <- as.matrix(model.matrix(~as.factor(x) -1))
y <- as.numeric(X%*% as.matrix(popMeans) + resid)

print(x)
print(y)

## plot the data
pdf("svl-data.pdf",height=6,width=6)
boxplot(y~x,col="grey",xlab="population",ylab="SVL",main="",las=1)
dev.off()

## write to outfile
xyFrame <- data.frame(x,y)
write.csv(xyFrame,file="svl.csv",row.names=FALSE)
print("done.")
