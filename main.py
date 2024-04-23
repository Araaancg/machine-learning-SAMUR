from os import path
from utils import *

csvDirectory = './data'
csvNames = getAllCsvNames(csvDirectory)

allDfs = {}
totalNumberRows = 0
for file in csvNames:
  # get encoding of the file
  filePath = path.join(csvDirectory, file)
  encoding = detectEncoding(filePath) 

  name = file.split(".")[0]

  print(f'The encoding of the file {name} is: {encoding}') 
  
  # ingest all csv
  df = ingestCsv(csvDirectory, file, encoding)

  # transform data
  df = transformDf(df, name)

  exportToCsv(df, "./output", file)

  dfNumRows = getStats(df, name)
  totalNumberRows += dfNumRows

  print()

  # add data to dict
  allDfs[file.split(".")[0]] = df

print("Total number of rows:", {totalNumberRows})