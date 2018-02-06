library(readr)
library(dplyr)
library(tidyr)
library(RColorBrewer)
t <- proc.time()

args <- commandArgs(T)
print(args)
name <- args[1]
cars <- read_csv(name)

cars <- cars %>% 
  gather(class, value, c(`Small/Sporty/ Compact/Large Sedan`, `Sports Car`, SUV, Wagon, Minivan, Pickup)) %>% 
  filter(value == 1)
cars$class <- ifelse(cars$class == 'Small/Sporty/ Compact/Large Sedan', 'Compact', cars$class)
cars$Weight[is.na(cars$Weight)] <- median(cars$Weight)
cars$Weight <- as.numeric(cars$Weight)

colors <- with(cars,
               data.frame(class = levels(factor(class)),
                          color = I(brewer.pal(nlevels(factor(cars$class)),
                                               name = 'Accent'))))
png(filename=args[2],
    width = 6,
    height = 5,
    units = 'in',
    res = 300)
plot(cars$HP, 
     cars$`City MPG`, 
     xlab = 'HP',
     ylab = 'City MPG',
     main = 'Horsepower vs. City MPG',
     col = colors$color[match(cars$class, colors$class)],
     pch = 15,
     cex = cars$Weight/1500)
legend(x = 'topright',
       legend = as.character(colors$class),
       col = colors$color,
       pch = 15,
       bty = 'n')

#dev.off()
t-proc.time()

