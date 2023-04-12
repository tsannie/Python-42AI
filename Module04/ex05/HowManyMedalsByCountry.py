import pandas as pd


def how_many_medals(data, year, color):
    all_sports = data["Sport"].unique()
    team_sports = [
        "Basketball",
        "Football",
        "Tug-Of-War",
        "Badminton",
        "Sailing",
        "Handball",
        "Water Polo",
        "Hockey",
        "Rowing",
        "Bobsleigh",
        "Softball",
        "Volleyball",
        "Synchronized Swimming",
        "Baseball",
        "Rugby Sevens",
        "Rugby",
        "Lacrosse",
        "Polo",
    ]
    df = data[(data["Year"] == year) & (data["Medal"] == color)]

    c = 0
    for sport in all_sports:
        if sport not in team_sports:
            c += len(df[df["Sport"] == sport])
        else:
            c += len(df[df["Sport"] == sport].groupby("Event").count())
    return c


def how_many_medals_by_country(data, country):
    if not isinstance(data, pd.DataFrame):
        print("Error: Data is not a pandas DataFrame")
        return None
    df = data[data["Team"] == country]
    years = df["Year"].unique()
    years.sort()

    ret = {}
    for year in years:
        ret[year] = {
            "G": how_many_medals(df, year, "Gold"),
            "S": how_many_medals(df, year, "Silver"),
            "B": how_many_medals(df, year, "Bronze"),
        }
    return ret
