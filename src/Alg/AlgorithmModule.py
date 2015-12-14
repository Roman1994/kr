from math import fabs



class Algorithm :

  def __init__(self, scanner) :
    self.points = scanner.getPoints()
    self.clusters = dict()

  def distance(self, point1, point2) :
    """ (x1, y1), (x2, y2) """
    return (((fabs(point1[1]-point2[1]))**2)+
            ((fabs(point1[2]-point2[2]))**2))**0.5