library(readxl)
data <- read.csv("data.csv")
CA <- read_excel("CA.csv")
CA <- as.data.frame(CA)
CA[is.na(CA)] <- 0
View(CA)
View(data)

