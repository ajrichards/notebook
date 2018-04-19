#!/usr/bin/Rscipt

drug <- as.table(cbind(c(90,80),c(10,20)))
colnames(drug) <- c("Winners","Losers")
rownames(drug) <- c("Drug","Placebo")
print(drug)

result <- fisher.test(drug) 
print(result)
