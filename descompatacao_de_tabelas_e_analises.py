# Importando as bibliotecas que usarei para a carga de dados
import pandas as pd
import sqlite3

# conectando o python com o meu banco de dados que está no pc
conexao = sqlite3.connect('Caminho/do/Seu/computador/database.sqlite')
print('Conexão Bem sucedida')

#  habilitando o cursor, que é basicamente quem vai executar os códigos SQL
cursor = conexao.cursor()

# pegando todas as 'tabelas' presentes no banco de dados por meio do sqlite_master
cursor = conexao.execute('''SELECT name FROM sqlite_master WHERE type ='table';''')

# armazenando na table_list todas as tabelas que o cursor buscou anteriormente
table_list = cursor.fetchall()
print(table_list)
# output: 
# [('sqlite_sequence',), ('Player_Attributes',), ('Player',), ('Match',), ('League',), ('Country',), ('Team',), ('Team_Attributes',)]

# função resposável por transformar o arquivo (tabelas) em csv e posteriormente salvá-las
def save(tabelas):
    command = 'SELECT * FROM '+ tabelas
    df_tabelas = pd.read_sql(command, conexao)
    modelpath = 'Caminho/do/Seu/computador/'
    df_tabelas.to_csv(modelpath + tabelas + '.csv', index = False)
    
# salvando cada tabela por meio da função 'save'
for tabela in table_list:
    print(f"Salvando tabela: {tabela[0]}")
    save(tabela[0])
# output:    
# Salvando tabela: sqlite_sequence
# Salvando tabela: Player_Attributes
# Salvando tabela: Player
# Salvando tabela: Match
# Salvando tabela: League
# Salvando tabela: Country
# Salvando tabela: Team
# Salvando tabela: Team_Attributes

# salvando as tabelas já separadas em data frames pandas 
caminho = 'Caminho/do/Seu/computador/'
df_Country = pd.read_csv(caminho + 'Country.csv')
df_League = pd.read_csv(caminho + 'League.csv')
df_Match = pd.read_csv(caminho + 'Match.csv')
df_Player = pd.read_csv(caminho + 'Player.csv')
df_Player_Attributes = pd.read_csv(caminho + 'Player_Attributes.csv')
df_Team = pd.read_csv(caminho + 'Team.csv')
df_Team_Attributes = pd.read_csv(caminho + 'Team_Attributes.csv')
df_sequence = pd.read_csv(caminho + 'sqlite_sequence.csv')

# --------------------------------------ANÁLISES-------------------------------
# teste para ver os resultados:

# Mostrando a estrutura de uma das tabelas
print(df_Team_Attributes.head())
#output:
# id  team_fifa_api_id  team_api_id                 date  buildUpPlaySpeed  \
# 0   1               434         9930  2010-02-22 00:00:00                60   
# 1   2               434         9930  2014-09-19 00:00:00                52   
# 2   3               434         9930  2015-09-10 00:00:00                47   
# 3   4                77         8485  2010-02-22 00:00:00                70   
# 4   5                77         8485  2011-02-22 00:00:00                47   

#   buildUpPlaySpeedClass  buildUpPlayDribbling buildUpPlayDribblingClass  \
# 0              Balanced                   NaN                    Little   
# 1              Balanced                  48.0                    Normal   
# 2              Balanced                  41.0                    Normal   
# 3                  Fast                   NaN                    Little   
# 4              Balanced                   NaN                    Little   

#    buildUpPlayPassing buildUpPlayPassingClass  ... chanceCreationShooting  \
# 0                  50                   Mixed  ...                     55   
# 1                  56                   Mixed  ...                     64   
# 2                  54                   Mixed  ...                     64   
# 3                  70                    Long  ...                     70   
# 4                  52                   Mixed  ...                     52   

#    chanceCreationShootingClass chanceCreationPositioningClass  \
# 0                       Normal                      Organised   
# 1                       Normal                      Organised   
# 2                       Normal                      Organised   
# ...
# 3                    Cover  
# 4                    Cover  

# [5 rows x 25 columns]

# Mostrando as informações de uma das tabelas
print(df_Team_Attributes.info())
# output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1458 entries, 0 to 1457
# Data columns (total 25 columns):
 #   Column                          Non-Null Count  Dtype  
# ---  ------                          --------------  -----  
#  0   id                              1458 non-null   int64  
#  1   team_fifa_api_id                1458 non-null   int64  
#  2   team_api_id                     1458 non-null   int64  
#  3   date                            1458 non-null   object 
#  4   buildUpPlaySpeed                1458 non-null   int64  
#  5   buildUpPlaySpeedClass           1458 non-null   object 
#  6   buildUpPlayDribbling            489 non-null    float64
#  7   buildUpPlayDribblingClass       1458 non-null   object 
#  8   buildUpPlayPassing              1458 non-null   int64  
#  9   buildUpPlayPassingClass         1458 non-null   object 
#  10  buildUpPlayPositioningClass     1458 non-null   object 
#  11  chanceCreationPassing           1458 non-null   int64  
#  12  chanceCreationPassingClass      1458 non-null   object 
#  13  chanceCreationCrossing          1458 non-null   int64  
#  14  chanceCreationCrossingClass     1458 non-null   object 
#  15  chanceCreationShooting          1458 non-null   int64  
#  16  chanceCreationShootingClass     1458 non-null   object 
#  17  chanceCreationPositioningClass  1458 non-null   object 
#  18  defencePressure                 1458 non-null   int64  
#  19  defencePressureClass            1458 non-null   object 
# ...
#  24  defenceDefenderLineClass        1458 non-null   object 
# dtypes: float64(1), int64(11), object(13)
# memory usage: 284.9+ KB
# None


# Descrevendo os dados das tabelas e já tirando alguns insights
print(df_Team_Attributes.describe())
# output:
#                 id  team_fifa_api_id    team_api_id  buildUpPlaySpeed  \
# count  1458.000000       1458.000000    1458.000000       1458.000000   
# mean    729.500000      17706.982167    9995.727023         52.462277   
# std     421.032659      39179.857739   13264.869900         11.545869   
# min       1.000000          1.000000    1601.000000         20.000000   
# 25%     365.250000        110.000000    8457.750000         45.000000   
# 50%     729.500000        485.000000    8674.000000         52.000000   
# 75%    1093.750000       1900.000000    9904.000000         62.000000   
# max    1458.000000     112513.000000  274581.000000         80.000000   

#        buildUpPlayDribbling  buildUpPlayPassing  chanceCreationPassing  \
# count            489.000000         1458.000000            1458.000000   
# mean              48.607362           48.490398              52.165295   
# std                9.678290           10.896101              10.360793   
# min               24.000000           20.000000              21.000000   
# 25%               42.000000           40.000000              46.000000   
# 50%               49.000000           50.000000              52.000000   
# 75%               55.000000           55.000000              59.000000   
# max               77.000000           80.000000              80.000000   

#        chanceCreationCrossing  chanceCreationShooting  defencePressure  \
# count             1458.000000             1458.000000      1458.000000   
# mean                53.731824               53.969136        46.017147   
# std                 11.086796               10.327566        10.227225   
# min                 20.000000               22.000000        23.000000   
# ...
# 25%            44.000000         47.000000  
# 50%            48.000000         52.000000  
# 75%            55.000000         58.000000  
# max            72.000000         73.000000 

# Mostrando uma tabelas específica no modelo data frame pandas
display(df_Team_Attributes)
# output: impossível mostrar

# Exemplo de contagem de valores únicos
print(df_Team_Attributes['chanceCreationShooting'].unique())
# output:
# [55 64 70 52 57 63 50 75 69 60 65 66 44 38 67 46 39 30 40 47 48 35 43 42
#  56 34 51 59 37 36 79 54 49 72 53 68 61 22 41 58 45 76 73 62 80 78 33 32
#  71 28 31 23 77 24 27 74 29]

# Exemplo de histograma
import matplotlib.pyplot as plt
df_Team_Attributes['chanceCreationShooting'].hist()
plt.xlabel('Variável')
plt.ylabel('Frequência')
plt.title('Histograma da Variável')
plt.show()
# output: impossível mostrar
