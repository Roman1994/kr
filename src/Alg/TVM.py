from Alg.AlgorithmModule import Algorithm
from math                import fabs



class ATV(Algorithm) :

  THRESHOLD = 2

  def __init__(self, scanner) :
    super().__init__(scanner)

  def execution(self) :
    """
       Проверить расстояние между i вершиной и всеми центрами кластеров
          Если расстояние меньше граничного значения, то добавить вершину
          к текущкму кластеру
          Если расстояние между вершиной и всеми центрами больше,
          то создать новый кластер
    """

    for point in self.points :
      center = self.__searchCluster(point)
      if center != None :
        (self.clusters[center]).append(point)
      else :
        (self.clusters).update({point: []})
    print(repr(self.clusters))

  def __searchCluster(self, point) :
    if len(self.clusters) == 0 :
      return None
    else :
      for center in self.clusters :
        if super().distance(center, point) < ATV.THRESHOLD :
          return center
      return None