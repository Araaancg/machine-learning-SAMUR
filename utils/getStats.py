def getStats(df, name):
    try:
        print()
        print(f"Number of rows - {df.shape[0]}")
        print(f"Number of different emergency code - {df['codigo_emergencia'].nunique()}")
        print(f"Number of different districts - {df['distrito'].nunique()}")
        print(f"Number of different hospitals - {df['hospital'].nunique()}")
        print(f"Number of interventions canceled - {len(df[df['hora_intervencion'].isnull() | (df['hora_intervencion'] == '')])}")
        print(f"Number of interventions not requiring hospitalisation - {len(df[df['hospital'].isnull() | (df['hospital'] == '')])}")
        print(f"Number of interventions without assigned district - {len(df[df['distrito'].isnull() | (df['distrito'] == '')])}")
        print(f"Number of interventions without assigned emergency code - {len(df[df['codigo_emergencia'].isnull() | (df['codigo_emergencia'] == '')])}")
        print()
        return df.shape[0]
    except Exception as e: 
        print(f"something went wrong when calculating stats in {name}. Error: {e}")