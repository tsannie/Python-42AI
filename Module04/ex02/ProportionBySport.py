import pandas as pd

def proportion_by_sport(df, year, sport, gender):
    if not isinstance(df, pd.DataFrame):
        print("Error: df is not a pandas DataFrame")
        return None
    if not isinstance(year, int):
        print("Error: year is not an integer")
        return None
    if not isinstance(sport, str):
        print("Error: sport is not a string")
        return None
    if gender not in ['F', 'M']:
        print("Error: invalid gender")
        return None

    try:
        total = df[(df['Year'] == year) & (df['Sex'] == gender)]
        total_sport = total[total['Sport'] == sport]
        return total_sport['ID'].unique().shape[0] / total['ID'].unique().shape[0]
    except:
        print("Error.")
        return 0



