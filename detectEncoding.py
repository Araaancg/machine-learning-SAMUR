import os
import chardet

def detectEncoding(filePath): 
    with open(filePath, 'rb') as file: 
        detector = chardet.universaldetector.UniversalDetector() 
        for line in file: 
            detector.feed(line) 
            if detector.done: 
                break
        detector.close() 
    return detector.result['encoding'] 

def getAllFilesWithEncoding(directory):
    filesWithEncoding = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            encoding = detectEncoding(filePath)
            filesWithEncoding.append((filePath, encoding))
    return filesWithEncoding

csvDirectory = './data'
files_with_encoding = getAllFilesWithEncoding(csvDirectory)

for file, encoding in files_with_encoding:
    name = os.path.basename(file)
    print(f'The encoding of the file {name} is: {encoding}')

