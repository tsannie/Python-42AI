from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
#Loading dataset of dimensions 271116 x 15

from MyPlotLib import MyPlotLib

mpl = MyPlotLib()
print("Test histogram")
mpl.histogram(data, ['Height', 'Weight'])

print("Test density")
mpl.density(data, ['Weight', 'Height'])

print("Test pair plot")
mpl.pair_plot(data, ['Weight', 'Height'])

print("Test box plot")
mpl.box_plot(data, ['Weight', 'Height'])
