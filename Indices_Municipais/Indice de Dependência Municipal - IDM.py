# Bibliotecas 
import pandas as pd 
import numpy as np 
from database import *

# Importando dados da Apuração da Receita 
data = ReceitasApuração.select()
dados = pd.read_sql(data.sql()[0] % tuple(data.sql()[1]), database.connection())

# Filtrando o banco de dados
dados_uf = dados[(dados['estado'] == "Ceará") & ( (dados['campo']=="Cota-Parte FPM") | (dados['campo']=="Cota-Parte ITR") | (dados['campo']=="Desoneração ICMS (LC 87/96)") | (dados['campo']=="Cota-Parte ICMS") |(dados['campo']=="Cota-Parte IPI-Exportação") |(dados['campo']=="Cota-Parte IPVA") | (dados['campo']=="TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II"))]

# Calculando o indicador 
for i in np.unique(dados_uf['municipio']):
    for j in np.unique(dados_uf['ano']):
        pre_index = dados_uf[(dados_uf['municipio']==i) & (dados_uf['ano']==j)]
        if len(pre_index) !=0:
            list_index_união =[] 
            list_index_estado =[]        
            for k in range(len(pre_index)-1):

                # Indicador para o estado
                if pre_index.iloc[k]['campo'] in ["Cota-Parte FPM","Cota-Parte ITR","Desoneração ICMS (LC 87/96)"]:
                    list_index_união.append(float(pre_index.iloc[k]['previsão_atualizada']))

                # Indicador para municipio 
                else:
                    list_index_estado.append(float(pre_index.iloc[k]['previsão_atualizada']))

            Dependência_união = sum(list_index_união)/ pre_index[pre_index['campo']=='TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['previsão_atualizada']
            Dependência_estadual = sum(list_index_estado)/ pre_index[pre_index['campo']=='TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['previsão_atualizada']
            try:
                ano = j 
                municipio = i
                codigo = np.unique(pre_index['codigo_Municipio'])[0]
                row = {'municipio':municipio,'estado':'Ceará','codigo':codigo,'ano':ano,'Dependência_União':Dependência_união.iloc[0],'Dependência_Estado':Dependência_estadual.iloc[0]}
                indicador = IndicadoresDependência.insert(row)
                indicador.execute()
            except:
                print('e')