# Bibliotecas 
import pandas as pd 
import numpy as np 
from database import *

# Importando dados da Apuração da Receita 
data = ReceitasAdicionais.select()
dados = pd.read_sql(data.sql()[0] % tuple(data.sql()[1]), database.connection())

# Filtrando o banco de dados  
dados_uf = dados[(dados['estado']=="Ceará") & ((dados['campo']=='Provenientes da União')| (dados['campo']=='Provenientes dos Estados')| (dados['campo']=='TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE'))]

# Calculando o indicador 
for i in np.unique(dados_uf['municipio']):
    for j in np.unique(dados_uf['ano']):
        pre_index = dados_uf[(dados_uf['municipio']==i) & (dados_uf['ano']==j)]
        if len(pre_index) !=0:

            # Indicador para a união
            Dependência_união = pre_index[pre_index['campo']=='Provenientes da União']['previsão_atualizada'].iloc[0]/pre_index[pre_index['campo']=='TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE']['previsão_atualizada']

            # Indicador para o estado 
            Dependência_estadual = pre_index[pre_index['campo']=='Provenientes dos Estados']['previsão_atualizada'].iloc[0]/pre_index[pre_index['campo']=='TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE']['previsão_atualizada']            

            try: 
                ano = j 
                municipio = i
                codigo = np.unique(pre_index['codigo_Municipio'])[0]
                row = {'municipio':municipio,'estado':'Ceará','codigo':codigo,'ano':ano,'Dependência_União':Dependência_união.iloc[0],'Dependência_Estado':Dependência_estadual.iloc[0]}
                indicador = IndicadoresDependênciaSUS.insert(row)
                indicador.execute()
            except Exception as e :
                print(e)                