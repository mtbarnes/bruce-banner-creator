from math import sqrt, pow

class Kvec(object):
    def __init__(self, points):
        self.points = [point for point in points]

    def __iter__(self):
        return iter(self.points)

    def __add__(self, other):
        added = [x + y for x, y in zip(self.points, other.points)]
        return self.__class__(added)

    def __eq__(self, other):
        for x, y in zip(self.points, other.points):
            if x != y:
                return False
        return True

    def __mul__(self, other):
        result = [point*other for point in self.points]
        return self.__class__(result)

    def __rmul__(self, other):
        return self.__mul__(self, other)


class Colorvec(Kvec):
    def __init__(self, points, mode="RGB"):
        self.mode = mode
        super(Colorvec, self).__init__(points)

    def __str__(self):
        hex_string = '#'
        for val in self.points:
            hex_string += "{0:0{1}x}".format(val, 2)
        return hex_string

    
def distance(point1, point2):
    ''' return the euclidean distance between point1 and point2'''
    sum_sq_diff = 0
    for i, j in zip(point1, point2):
        sum_sq_diff += pow(i - j, 2)
    return sqrt(sum_sq_diff)

