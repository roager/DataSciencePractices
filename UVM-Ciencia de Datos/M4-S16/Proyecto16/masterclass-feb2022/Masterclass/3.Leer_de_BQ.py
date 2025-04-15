# Objetivo: Vamos a crear la conexión con BigQuery y vamos a leer mediante consulta SQL desde Python.


# Generamos conexion a BQ
from google.oauth2 import service_account # para generar conexion
bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')

# Si queremos leer una tabla
import pandas as pd # para leer BQ

sql = """SELECT * FROM `masterclass-python-bigquery.data_warehouse.masterclass_feb22`"""
df_bq = pd.read_gbq(sql, project_id='masterclass-python-bigquery', credentials = bq_cred, dialect='standard') #Dialect standard: para usar BigQuery’s standard SQL dialect
print(df_bq)

sql_ak = """SELECT * FROM `masterclass-python-bigquery.data_warehouse.masterclass_feb22` where state = 'AK'"""
df_bq_ak = pd.read_gbq(sql_ak, project_id='masterclass-python-bigquery', credentials = bq_cred, dialect='standard')
print(df_bq_ak)

