# Bibliotecas 
from peewee import *
from playhouse.db_url import connect 

# Estabelecendo conexão 
database = connect("mysql://alexandre:34340012@localhost:3306/Data_saude")

# Criando a classe de conexão mysql 
class MySQLBitField(Field):
    field_type = "bit" 
    
    def __init__(self,*_,**__):
        pass

# Criando a classe do modelo basico 
class BaseModel(Model):
    class Meta:
        database = database 

# Tabela de Capacidade do Municipio 
class IndicadorCapacidade(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntegerField()
    ano = IntegerField()
    Capacidade = FloatField()

    class Meta:
        primary_key = False
        table_name = "Indicador_de_Capacidade_do_Municipio" 

# Indicadores de Dependência 
class IndicadoresDependência(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntegerField()
    ano = IntegerField()
    Dependência_União = FloatField()
    Dependência_Estado = FloatField()
    class Meta:
        primary_key =False
        table_name = "Indicadores_de_Dependência"

# Indicadores de Dependência do Sus 
class IndicadoresDependênciaSUS(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntegerField()
    ano = IntegerField()
    Dependência_União = FloatField()
    Dependência_Estado = FloatField()
    class Meta:
        primary_key= False
        table_name = "Indicadores_de_Dependência_SUS"

# Receitas de Apuração 
class ReceitasApuração(BaseModel):
    municipio = TextField()
    codigo_Municipio = TextField()
    estado = TextField()
    ano = IntegerField() 
    campo = IntegerField() 
    previsao_inicial =  FloatField() 
    previsão_atualizada = FloatField() 
    Receitas_realizadas_Bimestre = FloatField() 
    Receitas_realizadas_Porcentagem = FloatField() 
    class Meta:
        primary_key = False
        table_name = "Receitas_apuração_sps"

class ReceitasAdicionais(BaseModel):
    municipio = TextField()
    codigo_Municipio = TextField()
    estado = TextField()
    ano = IntegerField() 
    campo = IntegerField() 
    previsao_inicial =  FloatField() 
    previsão_atualizada = FloatField() 
    Receitas_realizadas_Bimestre = FloatField() 
    Receitas_realizadas_Porcentagem = FloatField() 
    class Meta:
        primary_key =False
        table_name = 'Receitas_adicionais_financiamento'

class Receitas_Recursos(BaseModel):
    municipio = TextField()
    codigo_Municipio = TextField()
    estado = TextField()
    ano = IntegerField() 
    campo = IntegerField()  
    Previsão_atualizada = FloatField() 
    Receita_Realizada = FloatField()
    Receita_orçada = FloatField()
    class Meta:
        primary_key = False 
        table_name = "2_Receitas_Recursos"