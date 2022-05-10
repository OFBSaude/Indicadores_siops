Create Table Indicador_de_Capacidade_do_Municipio(
municipio VARCHAR(100),
estado VARCHAR(100),
codigo INT,
ano INT,
Capacidade FLOAT);

Create Table Indicadores_de_Dependência(
municipio VARCHAR(100),
estado VARCHAR(100),
codigo INT,
ano INT,
Dependência_União FLOAT,
Dependência_Estado FLOAT);

Create Table Indicadores_de_Dependência_SUS(
municipio VARCHAR(100),
estado VARCHAR(100),
codigo INT,
ano INT,
Dependência_União FLOAT,
Dependência_Estado FLOAT);

Create Table Indicador_de_Aplicação(
municipio VARCHAR(100),
estado VARCHAR(100),
codigo INT,
ano INT,
ARS FLOAT);
