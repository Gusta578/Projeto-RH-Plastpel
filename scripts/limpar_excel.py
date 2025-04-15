import mysql.connector
import pandas as pd


# Aqui vou conectar ao banco de dados (Já criado) com a biblioteca mysql.connector
conexao = mysql.connector.connect(
    host = "3452354",
    user = "4325254",
    password = "345235",
    database = "432141234",
    port = 2341421354
)

# Aqui criei um cursos para executar comandos do SQL
cursor = conexao.cursor()

# Aqui vou criar meu dataframe/base de dados!
df = pd.read_excel(r"C:\xampp\htdocs\Projeto RH Plastpel\Projeto-RH-Plastpel\data\database.xlsx", sheet_name="ATIVOS", engine="openpyxl", header=1)

# Aqui vou substituir celulas vazias por "Não preenchido ou desconhecido
df = df.fillna("Não Preenchido/Desconhecido")

# Aqui vou remover a primeira linha do dataframe, por que está com linhas vazias
df = df.drop(index=0)





