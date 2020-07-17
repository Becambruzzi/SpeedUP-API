from django.db import models

class ProductModel(models.Model):
	Datetime = models.CharField(max_length=100)
	Subsistema = models.CharField(max_length=100)
	Demanda_Maxima_Instantanea_MW = models.CharField(max_length=100)
	ENA_Bruta_MLT = models.CharField(max_length=100)
	EAR_MAX_MWmes = models.CharField(max_length=100)
	Carga_de_Energia_MWmed = models.CharField(max_length=100)
	ENA_Bruta_MWmed = models.CharField(max_length=100)
	Demanda_Maxima_horaria_MWh_h = models.CharField(max_length=100)
	Geracao_de_Energia_dia_GWh = models.CharField(max_length=100)
	Carga_de_Energia_GWh = models.CharField(max_length=100)
	EAR_MWmes = models.CharField(max_length=100)
	ENA_armazenavel_MWmed = models.CharField(max_length=100)
	EAR_GWh = models.CharField(max_length=100)
	Geracao_de_Energia_dia_MWmed = models.CharField(max_length=100)
	ENA_armazenavel_MLT = models.CharField(max_length=100)
	EAR = models.CharField(max_length=100)

	def __str__():
		return self.Product


#Data,Subsistema,Demanda Maxima Instantanea (MW),
#Datetime,ENA Bruta (% MLT),EAR MAX (MWmes),Carga de Energia (MWmed),
#ENA Bruta (MWmed),Demanda Maxima horaria (MWh_h),
#Geracao de Energia - dia - (GWh),Carga de Energia (GWh),
#EAR (MWmes),ENA armazenavel (MWmed),
#EAR (GWh),Geracao de Energia - dia - (MWmed) ,
#ENA armazenavel (% MLT),EAR (%)