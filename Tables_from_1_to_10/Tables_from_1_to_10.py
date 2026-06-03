# Databricks notebook source
print("Tables from 1 to 10 in python using nested while loop")
for i in range (1,11):
    for j in range (1,11):
        print(i*j,end="\t")
    print()
print("Table completed successfully")
