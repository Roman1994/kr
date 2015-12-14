class IOFile :

  def __init__(self, name) :
    self.fileName = name
    self.points = []

  def setPoints(self) :
    i = 0
    line = self.readLine(i)
    while line :
      if '\n' in line :
        line = line[:len(line)-1]
      line = line.split()
      line = [line[0], int(line[1]), int(line[2])]
      line = tuple(line)
      (self.points).append(line)
      i += 1
      line = self.readLine(i)

  def readLine(self, index) :
    inFile = open('../Points/%s.txt' % (self.fileName))
    for i,line in enumerate(inFile) :
      if i == index :
        inFile.close()
        return line

  def getPoints(self) :
    self.setPoints()
    return self.points