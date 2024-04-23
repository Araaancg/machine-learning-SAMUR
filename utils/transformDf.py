import pandas as pd
from incidentData import codes, districts, hospitals

monthMap = {
  "ENERO": "01",
  "FEBRERO": "02",
  "MARZO": "03",
  "ABRIL": "04",
  "MAYO": "05",
  "JUNIO": "06",
  "JULIO": "07",
  "AGOSTO": "08",
  "SEPTIEMBRE": "09",
  "OCTUBRE": "10",
  "NOVIEMBRE": "11",
  "DICIEMBRE": "12"
}

def transformDf(df, name):
  try:

    # Change column names
    newColumnNames = ['ano', 'mes', 'hora_activacion', 'hora_intervencion', 'codigo_emergencia', 'distrito', 'hospital']
    df.columns = newColumnNames

    # Create date column from ano and mes
    df['mes'] = df['mes'].map(monthMap)
    df['fecha'] = df['ano'] + '-' + df['mes']
    df['fecha'] = pd.to_datetime(df['fecha'])

    df.drop(['mes', 'ano'], axis=1, inplace=True) # remove columns ano and mes once fecha is established

    # Create new column tiempo_intervencion
    df['hora_activacion'] = pd.to_datetime(df['hora_activacion'], format='%H:%M:%S')
    df['hora_intervencion'] = pd.to_datetime(df['hora_intervencion'], format='%H:%M:%S')

    df['tiempo_intervencion'] = df['hora_intervencion'] - df['hora_activacion']
    df['tiempo_intervencion'] = df['tiempo_intervencion'].astype(str).str.split().str[-1]

    df['hora_activacion'] = df['hora_activacion'].dt.strftime('%H:%M:%S')
    df['hora_intervencion'] = df['hora_intervencion'].dt.strftime('%H:%M:%S')

    # standarized data -> also remove special latin characters
    df['codigo_emergencia'] = df['codigo_emergencia'].map(codes)
    df['distrito'] = df['distrito'].map(districts)
    df['hospital'] = df['hospital'].map(hospitals)

    print(f'the transformation of {name} was succesful')
    return df
  except Exception as e:
    print(f'something went wrong with the transformation of df {name}. Error: {e}')
    return False