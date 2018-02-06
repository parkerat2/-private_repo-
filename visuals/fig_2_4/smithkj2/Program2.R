#Program2
t <- proc.time()

#iris <- datasets::iris
library(readr)
args <- commandArgs(T)
print(args)
name <- args[1]
iris <- read_csv(name)

iris_mat <- as.matrix(iris[,c(1:4)]/100)
pca <- prcomp(x = iris[,c(1:4)], 2, center=T)
comps <- pca$x



symbols(x=comps[,1],
        y=comps[,2],
        stars=(iris_mat[,c(1:4)]),
        inches=.15,
        fg='darkgreen',
        xlab = 'PC 1',
        ylab = 'PC 2',
        main='Iris PCA')

iris_loc = matrix(c(comps[,1],comps[,2]), ncol=2, nrow=150, byrow=F)

png(filename=args[2],
    width = 6,
    height = 5,
    units = 'in',
    res = 300)

stars(iris_mat[,c(1:4)],
      locations=iris_loc,
      len=.15,
      axes = T,
      xlab='PC1',
      ylab='PC2',
      main='Iris PCA')



print(t-proc.time())

