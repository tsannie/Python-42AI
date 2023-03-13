from csvreader import CsvReader

if __name__ == "__main__":
  with CsvReader('good.csv', header=False) as file:
    data = file.getdata()
    print(data)
    header = file.getheader()
    print(header)
