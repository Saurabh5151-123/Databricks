# Databricks notebook source
df = spark.sql(f"""
select * from workspace.information_schema.tables
""")
