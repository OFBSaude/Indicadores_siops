# Bibliotecas 
import pandas as pd 
import numpy as np 
from database import *

# Importando dados da Apuração da Receita 
data = =Receitas_Recursos.select()
dados = pd.read_sql(data.sql()[0] % tuple(data.sql()[1]), database_remote.connection())

# Filtrando o banco de dados
dados_uf = dados[(dados['estado'] == "Ceará") & ((dados['campo'] == "União (XII)")| (dados['campo'] == "Total (XVI = XII + XIII + XIV + XV)"))]

# Calculando o indicador
for i in np.unique(dados_uf['municipio']):
    for j in np.unique(dados_uf['ano']):
        pre_index = dados_uf[(dados_uf['municipio']==i) & (dados_uf['ano']==j)]
        if len(pre_index) !=2:
            a=pre_index[pre_index['campo']=="União (XII)"]['Previsão_atualizada'].iloc[0]/ pre_index[pre_index['campo']=="Total (XVI = XII + XIII + XIV + XV)"]['Previsão_atualizada']
            print(a)