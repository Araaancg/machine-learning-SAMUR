from os import path
import pandas as pd

def ingestCsv(dir, csvFile, encoding):
  try:
    filePath = path.join(dir, csvFile)
    df = pd.read_csv(filePath, sep=';', encoding=encoding, dtype=str)
    print(f'the df ingestation of {csvFile} was successfull')
    return df

  except Exception as e:
    print(f'something went wrong with the ingestation of df {csvFile}. Error: {e}')
    return False