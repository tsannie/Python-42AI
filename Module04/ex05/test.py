from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
# Output
# Loading dataset of dimensions 271116 x 15

from HowManyMedalsByCountry import how_many_medals_by_country

print(how_many_medals_by_country(data, "France"))
