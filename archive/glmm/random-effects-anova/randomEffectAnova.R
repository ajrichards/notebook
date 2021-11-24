#!/usr/bin/Rscript
# Rscript randomEffectAnova.R > re-anova-out.txt

library(R2jags)

## get data
data <- read.csv("re-svl.csv")
npop <- length(unique(data$x))
n <- length(data$x)

# Write model
cat("
model{
# priors and some derived things
for (i in 1:npop){
    pop.mean[i] ~ dnorm(mu,tau.group) # prior for population means
    effe[i] <- pop.mean[i] - mu       # population effects as derived quant’s
}

mu ~ dnorm(0,0.001)                   # hyperprior for grand mean svl
sigma.group ~ dunif(0, 10)            # hyperprior for sd of population effects
sigma.res ~ dunif(0, 10)              # prior for residual sd

# likelihood
for (i in 1:n) {
    y[i] ~ dnorm(mean[i], tau.res)
    mean[i] <- pop.mean[x[i]]
}

# derived quantities
tau.group <- 1 / (sigma.group * sigma.group)
tau.res <- 1 / (sigma.res * sigma.res)
}
",fill=TRUE,file="re-anova.txt")

# Bundle data
jagsData <- list(y=data$y,x=data$x,npop=npop,n=n)
params <- c("mu", "pop.mean", "effe", "sigma.group", "sigma.res")
inits <- function(){list(mu=runif(1,0,100),
                         sigma.group=rlnorm(1),
                         sigma.res=rlnorm(1))}

## parameters for MCMC sampling
nc <- 3       # Number of Chains
ni <- 5000    # Number of draws from posterior (for each chain)
nb <- 200     # Number of draws to discard as burn in
nt <- 2       # Thinning rate

jagsfit <- jags(jagsData,inits=inits,parameters.to.save=params,
                model.file="re-anova.txt",n.thin=nt,
                n.chains=nc,n.burnin=nb,n.iter=ni)

## make some plots
jagsfit.mcmc <- as.mcmc(jagsfit)
pdf("re-anova-chains.pdf")
xyplot(jagsfit.mcmc)
dvo <- dev.off()

pdf("re-anova-densities.pdf")
densityplot(jagsfit.mcmc)
dvo <- dev.off()

## print results to screen and file
print(jagsfit['BUGSoutput'])
