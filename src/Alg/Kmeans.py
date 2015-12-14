from math                import fabs
from Alg.AlgorithmModule import Algorithm



class Kmeans(Algorithm) :


  def __init__(self, scanner, count) :
    super().__init__(scanner)
    self.K = count


  def execution(self, preResult=None) :
    if preResult == None :
      for i in range(self.K) :
        (self.clusters).update({self.points[i]: [self.points[i]]})
      return self.execution(list((self.clusters).keys()))
    else :
      table = dict()
      table = self.__buildTable()
      self.__rebuildClusters(table)
      self.clusters = self.__correctCenter()

      result = list(self.clusters.keys())
      if result == preResult :
        return len(self.clusters), self.clusters
      else :
        return self.execution(result)

  def __buildTable(self) :
    table = dict()
    print(self.clusters)
    for point in self.points :
      if point not in self.clusters :
        table.update({point: [(center, (lambda p1, p2 :\
                     ((fabs(p1[1]-p2[1]))**2+(fabs(p1[2]-p2[2]))**2)**0.5)
                     (point, center))
                     for center in self.clusters]})
    table = self.__minDist(table)
    self.prprint(table)
    return table

  def __minDist(self, table) :

    def getDistance(t) :
      return t[1]

    for key in table :
      table[key] = sorted(table[key], key=getDistance)[0]
      table[key] = table[key][0]
    return table

  def __rebuildClusters(self, table) :
    for key in table :
      self.clusters[table[key]].append(key)

  def __correctCenter(self) :
    clusters  = dict()
    summa     = ['summa', 0, 0]
    newCenter = ['center', 0, 0]

    addVecteros = lambda p1, p2    : ('summa', p1[1]+p2[1], p1[2]+p2[2])
    divVector   = lambda cons, vec :\
                  ('center', round(vec[1]/cons, 2), round(vec[2]/cons, 2))

    for center in self.clusters :
      for vertex in self.clusters[center] :
        summa = addVecteros(summa, vertex)
      if summa[1] != 0 and summa[2] != 0 :
        newCenter = divVector(len(self.clusters[center]), summa)
      clusters.update({tuple(newCenter): self.clusters[center]})

    return clusters

  def prprint(self, table) :
    for key in table :
      print(repr(key), end =':')
      print('', end=' ')
      print(repr(table[key]))