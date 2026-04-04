# Databricks notebook source
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
