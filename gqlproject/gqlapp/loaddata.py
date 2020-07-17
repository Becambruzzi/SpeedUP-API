import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/bernardocambruzzi/Desktop/gqlAPI/gqlproject/db.sqlite3')
df = pd.read_csv('/Users/bernardocambruzzi/Desktop/Python/energy/export/subistema_dia.csv')
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


df.dropna().to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)

#df=df[['id','Segment','Country','Product','Units','Sales','Datesold']]
#df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)