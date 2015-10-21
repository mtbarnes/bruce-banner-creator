import utils
from functools import wraps
from nose.tools import assert_equals
import colorvecs
from colorvecs import Colorvec

def multi(fn):
    @wraps(fn)
    def wrapper():
        for n in range(100):
            fn()
    return wrapper

test_points = [(1, 1, 1), (0, 0, 0), (1.1, 1.1, 1.1), (0.2, 0.2, 0.2),
               (0.1, 0.1, 0.2), (1.1, 1.0, 1.0), (0, 0, 0.3)]
# test_points = [Colorvec(vec) for vec in test_points]
test_clusters = [(1, 1, 1), (0, 0, 0)]
# test_clusters = [Colorvec(vec) for vec in test_clusters]
test_cluster_count = len(test_clusters)
testKmeans = utils.KMeans(test_points, test_cluster_count, test_clusters)


def test_rgb_to_hex():

    color1 = Colorvec((0, 0, 0))
    color2 = Colorvec((1, 0, 0))
    color3 = Colorvec((0, 255, 0))
    color4 = Colorvec((255, 255, 255))
    assert str(color1) == "#000000"
    assert str(color2) == "#010000"
    assert str(color3) == "#00ff00"
    assert str(color4) == "#ffffff"

def test_calc_resp_vec():
    kmeans = utils.KMeans([(1,1,1)], 2)
    test_point = Colorvec((1, 1, 1))
    test_clusters = [Colorvec((1.5, 1.5, 1.5)),
                     Colorvec((-2, -2, -2)), Colorvec((3, 0, 3))]
    assert kmeans.calc_resp_vec(test_point,
                                test_clusters) == Colorvec((1, 0, 0))
    test_clusters.append(Colorvec((50,50,50)))
    assert kmeans.calc_resp_vec(test_point,
                                test_clusters) == Colorvec((1, 0, 0, 0))


@multi
def test_random_means():
    vecs = [(1, 0), (2, 0), (0, 3), (27, 27), (27, 25), (2, 2)]
    init_means = [(0, 0), (22, 22), (3, 3), (50, 50)]
    randKmeans = utils.KMeans(vecs, 3, init_means)
    random_means = randKmeans.random_means(4)
    print str(random_means[0])
    assert random_means.__class__ == list
    assert random_means[0].__class__ == randKmeans.vector_list[0].__class__
    assert random_means[3].__class__ == randKmeans.vector_list[0].__class__
    # randmeans2 = testKmeans.random_means(1)
    # assert randmeans[0] != randmeans[1]


def test_initialization():
    test_points = [(1, 1, 1), (0, 0, 0), (1.1, 1.1, 1.1), (0.2, 0.2, 0.2),
                   (0.1, 0.1, 0.2), (1.1, 1.0, 1.0), (0, 0, 0.3)]
    test_clusters = [(1, 1, 1), (0, 0, 0)]
    test_cluster_count = 2
    expected_resp = [(1, 0), (0, 1), (1, 0), (0, 1), (0, 1), (1, 0),
                     (0, 1)]
    testObj = utils.KMeans(test_points, test_cluster_count, test_clusters)
    assert testObj.vector_list == [Colorvec(tup) for tup in test_points]
    assert testObj.cluster_count == test_cluster_count
    assert testObj.means == [Colorvec(tup) for tup in test_clusters]
    assert testObj.resp_vectors == [Colorvec(tup) for tup in expected_resp]
    assert_equals(testObj.updated, True)
