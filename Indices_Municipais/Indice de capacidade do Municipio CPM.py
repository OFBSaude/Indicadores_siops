# Bibliotecas 
import pandas as pd 
import numpy as np 
from database import *

# Importando dados da Apuração de Receita 
data = ReceitasApuração.select()
dados = pd.read_sql(data.sql()[0] % tuple(data.sql()[1]), database.connection())

# Filtrando o banco de dados 
dados_f = dados[(dados['estado'] == "Ceará") & ((dados['campo'] == "RECEITA DE IMPOSTOS LÍQUIDA (I)") | (dados['campo']=="TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II"))]

# Calculando o indicador 
for i in range(2,2562,2):
    indice = dados_f.iloc[i:i+2]
    if float(indice[indice['campo']=='TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['previsão_atualizada']) !=0:
        index = float(indice[indice['campo']=='RECEITA DE IMPOSTOS LÍQUIDA (I)']['previsão_atualizada'])/float(indice[indice['campo']=='TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['previsão_atualizada'])
        Capacidade = index
        ano = np.unique(indice['ano'])[0]
        municipio = np.unique(indice['municipio'])[0]
        codigo = np.unique(indice['codigo_Municipio'])[0]
        row = {'municipio':municipio,'estado':'Ceará','codigo':codigo,'ano':ano,'Capacidade':index}
        indicador = IndicadorCapacidade.insert(row)
        indicador.execute()