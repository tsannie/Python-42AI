import pandas as pd


def how_many_medals(df, name):
    if not isinstance(df, pd.DataFrame):
        print("Error: df is not a pandas DataFrame")
        return None
    if not isinstance(name, str):
        print("Error: name is not a string")
        return None

    ret = {}
    df = df[df["Name"] == name]
    df = df[["Year", "Medal"]]
    df = df.groupby(["Year"])
    for year, group in df:
        ret[year] = {"G": 0, "S": 0, "B": 0}
        for medal in group["Medal"]:
            if medal == "Gold":
                ret[year]["G"] += 1
            elif medal == "Silver":
                ret[year]["S"] += 1
            elif medal == "Bronze":
                ret[year]["B"] += 1
    return ret
