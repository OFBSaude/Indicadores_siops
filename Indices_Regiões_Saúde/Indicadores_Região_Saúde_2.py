# Biblioteca 
import pandas as pd 
import numpy as np 
import json 
from database import * 

# Importando dados da Apuração da Receita 
dados = ReceitasApuração.select(ReceitasApuração.municipio, ClassificaçõesMunicipio.Região,ReceitasApuração.codigo_Municipio, ReceitasApuração.estado, ReceitasApuração.ano, ReceitasApuração.campo, ReceitasApuração.Receitas_realizadas_Bimestre).join(ClassificaçõesMunicipio,on=(ReceitasApuração.municipio == ClassificaçõesMunicipio.Municipio)).where((ReceitasApuração.campo =='RECEITA DE IMPOSTOS LÍQUIDA (I)')|(ReceitasApuração.campo == 'Cota-Parte FPM') | (ReceitasApuração.campo == 'Cota-Parte ITR') | (ReceitasApuração.campo == 'Desoneração ICMS (LC 87/96)') | (ReceitasApuração.campo == 'Cota-Parte ICMS') | (ReceitasApuração.campo == 'Cota-Parte IPI-Exportação') | (ReceitasApuração.campo == 'Cota-Parte IPVA') | (ReceitasApuração.campo == 'TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II') & (ReceitasApuração.estado == "Ceará"))
Apuração= pd.DataFrame(dados.dicts())

# Importando dados de Receitas Adicionais
data = ReceitasAdicionais.select(ReceitasAdicionais.municipio, ClassificaçõesMunicipio.Região,ReceitasAdicionais.codigo_Municipio, ReceitasAdicionais.estado, ReceitasAdicionais.ano, ReceitasAdicionais.campo, ReceitasAdicionais.Receitas_realizadas_Bimestre).join(ClassificaçõesMunicipio,on=(ReceitasAdicionais.municipio == ClassificaçõesMunicipio.Municipio)).where((ReceitasAdicionais.campo=='Provenientes da União')|(ReceitasAdicionais.campo == 'Provenientes dos Estados')| (ReceitasAdicionais.campo== "TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE") &(ReceitasAdicionais.estado == "Ceará"))
Adicional = pd.DataFrame(data.dicts())

Indicador_subregião =  {'Região':[],'ano':[],'capacidade':[],'Dependência_união':[],'Dependência_estadual':[],'Dependência_sus_união':[],'Dependência_sus_estado':[]}

## Calculando os indicadores 
for Região in np.unique(Apuração['Região']):
    try:
        for ano in np.unique(Apuração['ano']):
            região = Apuração[(Apuração['Região']==Região) & (Apuração['ano']==ano)]

            # Indice de capacidade 
            numerador = sum(região[região['campo']=='RECEITA DE IMPOSTOS LÍQUIDA (I)']['Receitas_realizadas_Bimestre'])
            denominador = sum(região[região['campo']== 'TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['Receitas_realizadas_Bimestre'])
            Indicador_subregião['capacidade'].append(numerador / denominador)
            
            # Indice de Dependência - União
            numerador = sum(região[região['campo']=="Cota-Parte FPM"]['Receitas_realizadas_Bimestre']) + sum(região[região['campo']=="Cota-Parte ITR"]['Receitas_realizadas_Bimestre']) + sum(região[região['campo']=="Desoneração ICMS (LC 87/96)"]['Receitas_realizadas_Bimestre'])
            denominador = sum(região[região['campo']== 'TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['Receitas_realizadas_Bimestre'])
            Indicador_subregião['Dependência_união'].append(numerador/denominador)

            # Indice de Dependência - Estadual 
            numerador = sum(região[região['campo']=="Cota-Parte ICMS"]['Receitas_realizadas_Bimestre']) + sum(região[região['campo']=="Cota-Parte IPI-Exportação"]['Receitas_realizadas_Bimestre']) + sum(região[região['campo']=="Cota-Parte IPVA"]['Receitas_realizadas_Bimestre'])
            denominador = sum(região[região['campo']== 'TOTAL DAS RECEITAS PARA APURAÇÃO DA APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II']['Receitas_realizadas_Bimestre'])
            Indicador_subregião['Dependência_estadual'].append(numerador/denominador)

            região = Adicional[(Adicional['Região']==Região) & (Adicional['ano']==ano)]

            # Indice de Dependência SUS - União 
            numerador = sum(região[região['campo']=='Provenientes da União']['Receitas_realizadas_Bimestre']) 
            denominador =  sum(região[região['campo']=='TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE']['Receitas_realizadas_Bimestre'])
            Indicador_subregião['Dependência_sus_união'].append(numerador/denominador)

            # Indice de Dependência SUS - Estadual 
            numerador = sum(região[região['campo']=='Provenientes dos Estados']['Receitas_realizadas_Bimestre']) 
            denominador =  sum(região[região['campo']=='TOTAL RECEITAS ADICIONAIS PARA FINANCIAMENTO DA SAÚDE']['Receitas_realizadas_Bimestre'])
            Indicador_subregião['Dependência_sus_estado'].append(numerador/denominador)

            Indicador_subregião['Região'].append(Região)
            Indicador_subregião['ano'].append(ano)
    except:
        print("Continua")
