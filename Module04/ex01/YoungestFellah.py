import pandas as pd

def youngest_fellah(data, year):
    if not isinstance(data, pd.DataFrame):
        print("Error: Data is not a pandas DataFrame")
        return None
    if not isinstance(year, int):
        print("Error: year is not an integer")
        return None

    olympic_year = data[data['Year'] == year]

    woman = olympic_year[olympic_year['Sex'] == 'F']
    man = olympic_year[olympic_year['Sex'] == 'M']

    woman_age = woman['Age'].min()
    man_age = man['Age'].min()

    return {"w": woman_age, "m": man_age}
