require(grDevices)
require(stats)
library(ggplot2)
args <- commandArgs()
x <- read.table(args[6],header=T,sep=",")
PCA_data <- princomp(x[1:4],cor="False")
pc.comp <- PCA_data$scores
pc.comp1 <- -1*pc.comp[,1] 
pc.comp2 <- -1*pc.comp[,2]
m <- matrix(c(pc.comp1,pc.comp2),ncol=2)
colors <- c(rep(3,150))
png(filename=args[7])
stars(x[, 1:4], locations=m,len=.2,xlim=c(-3,3),col.lines = colors, main="Iris Data Set", key.loc = c(-2,2))
dev.off()
