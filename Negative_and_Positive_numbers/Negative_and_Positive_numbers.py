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
