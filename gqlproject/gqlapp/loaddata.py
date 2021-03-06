import sqlite3
import psycopg2
import pandas as pd

#conn = psycopg2.connect(host="localhost", port = 5432, database="gqlproject", user="becambruzzi", password="")

df = pd.read_csv('subistema_dia2.csv')
df['id'] = df.index


df.columns = [
	'Datetime',
	'Subsistema',
	'Demanda_Maxima_Instantanea_MW',
	'ENA_Bruta_MLT',
	'EAR_MAX_MWmes',
	'Carga_de_Energia_MWmed',
	'ENA_Bruta_MWmed',
	'Demanda_Maxima_horaria_MWh_h',
	'Geracao_de_Energia_dia_GWh',
	'Carga_de_Energia_GWh',
	'EAR_MWmes',
	'ENA_armazenavel_MWmed',
	'EAR_GWh',
	'Geracao_de_Energia_dia_MWmed',
	'ENA_armazenavel_MLT',
	'EAR',
	'id'

]
df = df[
	['id',
	'Datetime',
	'Subsistema',
	'Demanda_Maxima_Instantanea_MW',
	'ENA_Bruta_MLT',
	'EAR_MAX_MWmes',
	'Carga_de_Energia_MWmed',
	'ENA_Bruta_MWmed',
	'Demanda_Maxima_horaria_MWh_h',
	'Geracao_de_Energia_dia_GWh',
	'Carga_de_Energia_GWh',
	'EAR_MWmes',
	'ENA_armazenavel_MWmed',
	'EAR_GWh',
	'Geracao_de_Energia_dia_MWmed',
	'ENA_armazenavel_MLT',
	'EAR'
	]
]
print(df.columns)

from sqlalchemy import create_engine
engine = create_engine('postgresql://becambruzzi:@localhost:5432/gqlproject')
df.to_sql('gqlapp_productmodel', engine,if_exists='replace')   

