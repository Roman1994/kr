from IOFile.IOFile import IOFile
from Alg.TVM       import ATV
from Alg.AMM       import MinMax
from Alg.Kmeans    import Kmeans



def main() :
  inName = input('Enter name: ')
  scan = IOFile(inName)
  atv = ATV(scan)
  atv.execution()
  print("MinMax")
  mm = MinMax(scan)
  res = mm.execution()
  print(res)
  kmeans = Kmeans(scan, res[0])
  print('Kmeans')
  res1 = kmeans.execution()
  print(res1)

if __name__ == '__main__' :
  main()