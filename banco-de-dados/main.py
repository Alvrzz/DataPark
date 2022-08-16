import sqlite3
import pandas as pd 
import random


cnx = sqlite3.connect('dbparque.sqlite3')
cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CLIMA; 
""")

cur.execute("""    
    CREATE TABLE CLIMA (
            CLIMA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CLIMA_DATA TEXT NOT NULL,
            CLIMA_CHUVAMM INTEGER,
            CLIMA_TEMPMIN FLOAT NOT NULL,
            CLIMA_TEMPMAX FLOAT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS CLIENTES; 
""")

cur.execute("""
    CREATE TABLE CLIENTES(
        CLIENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLIENTE_DATA TEXT NOT NULL,
        CLIENTE_NOME TEXT NOT NULL, 
        CLIENTE_CPF TEXT NOT NULL,
        CLIENTE_IDADE INTEGER NOT NULL,
        CLIENTE_UF TEXT NOT NULL,
        CLIENTE_CIDADE TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS FUNCIONARIOS; 
""")

cur.execute("""
    CREATE TABLE FUNCIONARIOS(
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FUNCIONARIO_DATA TEXT NOT NULL,
        FUNCIONARIO_NOME TEXT NOT NULL, 
        FUNCIONARIO_ATRACOES_ID INTEGER NOT NULL
        );
""")

cur.execute("""
    DROP TABLE IF EXISTS ATRACOES; 
""")

cur.execute("""
    CREATE TABLE ATRACOES(
        ATRACAO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ATRACAO_NOME TEXT NOT NULL
        );
""")

cnx.commit()

#Atracoes
#https://docs.google.com/spreadsheets/d/e/2PACX-1vREs0dmKxwNbeUE3Hg-fnE5Iok2BcDFFOjbD1BAhVJTBqvbWvJMD2Cr3cK-S_jUMR-MPVaked6F2XZ5/pub?output=csv


#Cidades
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSNCRSky5LXh-rcR9TpHd26yNotvIgeGcGqmgZTEin2kUP9RjKhVAIRu4DfUZstqgRrkZXXapzpG7aw/pub?output=csv


#Clima
# https://docs.google.com/spreadsheets/d/e/2PACX-1vQl72SaiyWVOyzX55ofSzEJOF6F8M3gYQ3_z87f3HqY0650jlcjUK5M7wRxjwkzL8-vL5bRjLa8M55y/pub?output=csv       

#Funcionarios
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSKb39CfrYvHZfTgmt63ZhPNA3L0Bsa6d8pHXF9veAwd4_Sz_3hfeOIFv2Is5DDKmOpkINZQqfpqXtt/pub?output=csv

#Clientes
#https://docs.google.com/spreadsheets/d/e/2PACX-1vToO64gKQo1Je4RNwtJW-f7H6QThRtjW2IwaXeepMkVlBV2kCouHCGykVDe54Dnb86ZPXVLTN3SzHFQ/pub?output=csv




