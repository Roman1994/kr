from Alg.AlgorithmModule import Algorithm
from math                import fabs



class MinMax(Algorithm) :


  def __init__(self, scanner) :
    super().__init__(scanner)


  def execution(self) :
    distance = lambda p1, p2 :\
           ((fabs(p1[1]-p2[1]))**2+(fabs(p1[2]-p2[2]))**2)**0.5
    if len(self.clusters) == 0 :
      (self.clusters).update({self.points[0]: None})
      return self.execution()
    else :
      table = dict()
      for point in self.points :
        if point not in self.clusters :
          table.update({point: min([distance(point, center)
                        for center in self.clusters])})
      newCenter = self.__maxDistance(table)
      if newCenter[1] > self.__average()/2 :
        (self.clusters).update({newCenter[0]: None})
        return self.execution()
      else :
        return len(self.clusters), self.clusters

  def __average(self) :
    summa = 0
    l = [point for point in self.points if point in self.clusters]
    for i in range(1, len(l)) :
      summa += super().distance(l[i-1], l[i])
    return summa/len(l)

  def __maxDistance(self, table) :
    """ point, distance """
    maximum = [0, 0]
    for point in table :
      if table[point] > maximum[1] :
        maximum = [point, table[point]]
    return maximum