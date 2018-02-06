args <- commandArgs()
x <- read.table(args[6],header=T,sep=",")
str(x)
ex <- as.numeric(as.character(x$City.MPG))
qu <- as.numeric(as.character(x$HP))
w <- as.numeric(as.character(x$Weight))
x$Color = "black"
x$Color[x$Small.Sporty..Compact.Large.Sedan == 1] = "green"
x$Color[x$Sports.Car == 1] = "red"
x$Color[x$SUV == 1] = "blue"
x$Color[x$Wagon == 1] = "yellow"
x$Color[x$Minivan == 1] = "cyan"
x$Color[x$Pickup == 1] = "black"

png(filename=args[7])
par(bg = "grey")
plot(qu,ex,pch=22,xlab = "HP",ylab = "City MPG", main = 'City MPG vs HP of Cars of Different Types and Weights', cex=w/1500, bg=x$Color)
dev.off()
