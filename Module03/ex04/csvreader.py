class CsvReader():

  def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
    self.filename = filename
    self.sep = sep
    self.header = header
    self.skip_top = skip_top
    self.skip_bottom = skip_bottom
    self.data = []
    self.fd = None

  def __enter__(self):
    try:
      print(self.filename)
      self.fd = open(self.filename, 'r')
      self.data = self.fd.read().splitlines()
      self.data = [line.split(self.sep) for line in self.data]
      for line in self.data:
        if len(line) != len(self.data[0]):
          return None
    except:
      return None
    return self


  def __exit__(self, type, value, traceback):
    self.data = []
    self.fd.close()

  def getdata(self):
    """ Retrieves the data/records from skip_top to skip bottom.
    Return:
    nested list (list(list, list, ...)) representing the data.
    """
    start = self.skip_top
    end = len(self.data) - self.skip_bottom
    if self.header:
      start += 1
    return self.data[start:end]


  def getheader(self):
    """ Retrieves the header from csv file.
    Returns:
    list: representing the data (when self.header is True).
    None: (when self.header is False).
    """
    if not self.header:
      return None
    return self.data[0]
