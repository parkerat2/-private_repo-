args = commandArgs(trailingOnly=TRUE)
df <- read.csv(args[1])
##Iris is pre loaded in R

ir.pca <- prcomp(x = df[,c(1:4)], center = T, scale = T) 
df <- as.data.frame(ir.pca$x)

png(args[2])

stars(df,
      len = -.1,
      locations = matrix(c(-df$PC1, 2.0*df$PC3), ncol = 2, nrow = 150, byrow = F),
      xlab = '-PC1',
      ylab = '2.0 * PC3',
      main = 'PC1 v PC3',
      axes = T,
      col.lines = rep('#1DA42F',150))

dev.off()

##No clue why my stars are rotated, have tried just about every type of PCA 
##manipulation but it doesn't seem to compute it the same way the book does.
##Had to just set the len parameter to a negative, which worked.
##Also, the base graphics don't allow me to change the cross color.

