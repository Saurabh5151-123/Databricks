# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "4"
# ///
df = spark.sql(f"""
select * from workspace.information_schema.tables
""").display()
