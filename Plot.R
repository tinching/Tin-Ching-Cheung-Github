install.packages(c('dplyr','ggplot2'))

library(dplyr)
library(ggplot2)

#Histogram
hist(mpg$cty, col='lightblue',
     xlab="City MPG", ylab="Frequency",
     main="Distribution of City Fuel Efficiency")

#Density plot
plot(density(mpg$cty), main='Density of City MPG',
     xlab='City MPG', col='darkblue', lwd=2)
rug(mpg$cty, col='red')

#Bar Chart
barplot(table(mpg$class), xlab='Vehicle Class', ylab='Frequency',
        col='steelblue',main='Venhicle Classes in mpg Dataset')

#Scatterplot
plot(mpg$hwy, mpg$cty,
     xlab='Highway MPG', ylab="City MPG",
     main='City vs Highway Fuel Efficiency', pch=19)
abline(lm(cty~hwy, data=mpg),col='red', lwd=2)

#line plot
plot(economics$date, economics$psavert, type = "l",
     xlab = "Date", ylab = "Personal Savings Rate (%)",
     main = "US Personal Savings Rate Over Time", col = "darkblue")