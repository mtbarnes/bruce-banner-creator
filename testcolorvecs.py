import math
from colorvecs import Colorvec
from colorvecs import distance
from nose.tools import assert_equals

def test_colorvec_add():
    test1 = Colorvec((1,1,1))
    test2 = Colorvec((1,1,1))
    result = test1+test2
    expected = Colorvec((2,2,2))
    assert(result == expected)

def test_distance():
    point000 = Colorvec((0, 0, 0))
    point100 = Colorvec((1, 0, 0))
    point001 = Colorvec((0, 0, 1))
    point002 = Colorvec((0, 0, 2))
    point111 = Colorvec((-1, -1, -1))
    assert distance(point000, point000) == 0
    assert distance(point000, point100) == 1
    assert distance(point100, point001) == math.sqrt(2)
    assert distance(point002, point100) == math.sqrt(5)
    assert distance(point000, point111) == math.sqrt(3)

