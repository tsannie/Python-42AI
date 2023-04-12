from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
# Output
# Loading dataset of dimensions 271116 x 15

from Komparator import Komparator

kmp = Komparator(data)

print("Test compare_box_plots:")
kmp.compare_box_plots("Medal", "Age")

print("Test density:")
kmp.density("Sex", "Age")

print("Test compare_histograms:")
kmp.compare_histograms("Medal", "Age")
