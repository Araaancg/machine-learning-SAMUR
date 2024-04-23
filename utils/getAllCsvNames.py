from os import listdir

def getAllCsvNames(dir):
  # get all file names in a given directory
  try:
      csvNames = listdir(dir)
      return csvNames
  except FileNotFoundError:
      print(f'Directory {dir} not found')
      return None