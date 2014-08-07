#!/usr/bin/Rscript
# Rscript fixedEffectAnova.R > fe-anova-out.txt

library(R2jags)

## get data
data = read.csv("fe-svl.csv")

# Write model
cat("
model{
# Priors
for (i in 1:5){ # Implicitly define alpha as a vector
    alpha[i] ~ dnorm(0, 0.001)
}
sigma ~ dunif(0, 100)

# Likelihood
for (i in 1:50) {
    y[i] ~ dnorm(mean[i], tau)
    mean[i] <- alpha[x[i]]
}

# Derived quantities
tau <- 1 / ( sigma * sigma)
effe2 <- alpha[2] - alpha[1]
effe3 <- alpha[3] - alpha[1]
effe4 <- alpha[4] - alpha[1]
effe5 <- alpha[5] - alpha[1]

# Custom hypothesis test / Define your own contrasts
test1 <- (effe2+effe3) - (effe4+effe5) # Equals zero when 2+3 4+5
test2 <- effe5 - 2 * effe4 # Equals zero when effe5 2*effe4
}
",fill=TRUE,file="fe-anova.txt")

# Bundle data
jagsData <- list(y=data$y,x=data$x)
params <- c("alpha", "sigma", "effe2", "effe3", "effe4", "effe5", "test1", "test2")
inits <- function(){list(alpha=rnorm(5,mean=mean(data$y)),
                         sigma=runif(1,1,30))}

## parameters for MCMC sampling
nc <- 3       # Number of Chains
ni <- 5000    # Number of draws from posterior (for each chain)
nb <- 200     # Number of draws to discard as burn in
nt <- 2       # Thinning rate

jagsfit <- jags(jagsData,inits=inits,parameters.to.save=params,
                model.file="fe-anova.txt",n.thin=nt,
                n.chains=nc,n.burnin=nb,n.iter=ni)

## make some plots
jagsfit.mcmc <- as.mcmc(jagsfit)
pdf("fe-anova-chains.pdf")
xyplot(jagsfit.mcmc)
dvo <- dev.off()

pdf("fe-anova-densities.pdf")
densityplot(jagsfit.mcmc)
dvo <- dev.off()

## print results to screen and file
print(jagsfit['BUGSoutput'])
