from os import path, makedirs

def exportToCsv(df, outputFolder, filename):
    try:
        if not path.exists(outputFolder):
            makedirs(outputFolder)

        filepath = path.join(outputFolder, filename)
        df.to_csv(filepath, index=False)

        print(f"DataFrame successfully exported to {filepath}")
    except Exception as e:
        print(f"Error exporting DataFrame: {e}")