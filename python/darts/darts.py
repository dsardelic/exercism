import bisect
import math


def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    thresholds = [1, 5, 10]
    points = [10, 5, 1, 0]
    return points[bisect.bisect_left(thresholds, distance)]
