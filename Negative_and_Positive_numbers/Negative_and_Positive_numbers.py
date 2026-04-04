# Databricks notebook source
l=[-4,5,7,8,-9,-6,0]
pos=[]
neg=[]
for i in l:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print("Positive Numbers",pos)
print("Negative Numbers",neg)

# COMMAND ----------

i=1
j=1
print("Right angle triangle * pattern using while loop")
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+1
    print(" ")
