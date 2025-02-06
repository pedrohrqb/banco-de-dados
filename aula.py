import pandas as pd

#Atribuo os arquivos .csv as variáveis e com ajuda da biblioteca panda para ler os arquivos csv
#Com o parametro delimiter, eu separo os titulo da tabela por ordem
df_operacoes = pd.read_csv("OPERAÇÕES.csv", delimiter=";")
df_eventos = pd.read_csv("EVENTOS.csv", delimiter=";")


#Aqui eu faço a junção das 2 tabelas, atribuindo da tabela eventos somente o que tiver compátivel com a tabela operaçães.
#Para isso, passo o paramentro "on" e indico qual atributo levar em consideração.
#O parametro "how", indicará qual coluna da tabela "ID_OPERAÇÃO" irá comparar, que no caso é a esquerda "left" 
df_consolidado = pd.merge(df_operacoes, df_eventos, on="ID_OPERAÇÃO", how="left")

print(df_consolidado)