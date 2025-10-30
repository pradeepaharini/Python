#Code Author: Pradeepa Harini B

from itertools import zip_longest
def centroid(*points):
  return [sum(x)/len(points) for x in zip_longest(*points, fillvalue=0)]
centroid([1],[2,3],[4,5,6])
