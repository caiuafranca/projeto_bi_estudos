import pandas as pd
import sqlite3

# Criando a conexão com a Base Relacional SQLITE.
conexaoSqlite = sqlite3.connect('../../files/dataMirrors/empresas.db')
empresas = pd.read_sql_query("SELECT * FROM Empresas", conexaoSqlite)

empresasCalc = pd.read_csv('../../files/spreadsheets/empresasCalc.csv',sep=";")

dt_empresas = empresas.join(empresasCalc.set_index("cd_cnpj"), on="cd_cnpj")

# Consulta para verificar
# dt_empresas.query("cd_cnpj == 7297742000170")

# Comando para dropar a coluna Index criada pelo pandas
dt_empresas = dt_empresas.drop(columns=['index'])

# ajustas os campos vazios do dataframe
dt_empresas.fillna(0, inplace=True)

#Exportando Dataframe para Mirrors
dt_empresas.to_csv("../../files/dataMirrors/extract_empresas.csv", sep=";", index=False)