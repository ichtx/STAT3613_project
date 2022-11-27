# 1: NTE, 2: NTW 3:KL 4: HK Island

library(psych)
library(ggplot2)
library(reshape2)
data <- read.csv("data.csv")



describe(data,skew=F,ranges=F)

data$Gender <- as.factor(data$Gender)
data$Year.of.Study <- as.factor(data$Year.of.Study)
data$Living.District <- as.factor(data$Living.District)
data$Transportation <- as.factor(data$Transportation)
data$Monthly.Expense <- as.factor(data$Monthly.Expense)
data$Num_transfer<- as.factor(data$Num_transfer)
exp = scale(subset(data, select = c(4, 7)))

h1<-cbind(
  model.matrix( ~ Gender - 1, data),
  model.matrix( ~ Monthly.Expense - 1, data),
  model.matrix( ~ Num_transfer - 1, data),
  model.matrix( ~ Living.District - 1, data),
  model.matrix( ~ Transportation - 1, data))


dist<-dist(h1,method="euclidean")^2

fit <- hclust(dist, method="ward.D")
history<-cbind(fit$merge,fit$height)
history

ggplot(mapping=aes(x=1:length(fit$height),y=fit$height))+
  geom_line()+
  geom_point()+
  labs(x="stage",y="height")


plot(fit,labels=data$X,hang=-1,main="",axes=FALSE)
axis(side = 2, at = seq(0, 70))

cutree(fit, k=4) #cluster index
sol <- data.frame(cluster=cutree(fit, k=4),id=h1)
sol[ order(sol$cluster),1:15 ]

table(sol[,1])


tb<-aggregate(x=sol[,], by=list(cluster=sol$cluster),FUN=mean)
print(tb,digits=2)


tbm<-melt(tb,id.vars='cluster')
tbm$cluster<-factor(tbm$cluster)
ggplot(tbm, 
       aes(x = variable, y = value, group = cluster, colour = cluster)) + 
  geom_line(aes(linetype=cluster))+
  geom_point(aes(shape=cluster)) +
  geom_hline(yintercept=0) +
  labs(x=NULL,y="mean")
