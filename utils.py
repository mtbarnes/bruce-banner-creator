from random import randint
import colorvecs
from colorvecs import Colorvec

class KMeans():
    '''Module for predicting centroids of vector clusters'''

    def __init__(self, vector_list, cluster_count, means=[], cutoff_iter=20):
        self.vector_list = [Colorvec(item) for item in vector_list]
        self.cluster_count = cluster_count
        if means == []:
            self.means = self.random_means(self.cluster_count)
        else:
            self.means = [Colorvec(item) for item in means]
        self.resp_vectors = [self.calc_resp_vec(vec, self.means)
                             for vec in self.vector_list]
        self.updated = True
        self.cutoff_iter= cutoff_iter

    def smart_seed(self, cluster_count):
        '''return a list of <cluster_count> means selected from
        self.vector_list such that each mean is far from the others'''
        means = []
        return means

    def random_means(self, cluster_count):
        '''return a list of <cluster_count> random means selected from
        self.vector_list.'''
        means = []
        print(self.vector_list)
        for k in range(0, cluster_count):
            randvec = self.vector_list[randint(0, len(self.vector_list) - 1)]
            means.append(randvec)
        return means

    def calc_resp_vec(self, point, cluster_means):
        '''return a responsibility vector (tuple) with a single entry set to
        1 (corresponding to the nearest cluster mean) and all other
        entries set to 0.

        '''
        responsibilities = []
        closest = 0
        dist = colorvecs.distance(point, cluster_means[0])
        for i, mean in enumerate(cluster_means):
            responsibilities.append(0)
            if colorvecs.distance(point, cluster_means[i]) < dist:
                closest = i

        responsibilities[closest] = 1
        return Colorvec(responsibilities)

    def assignment_step(self):
        for n, vector in enumerate(self.vector_list):
            self.resp_vectors[n] = self.calc_resp_vec(vector, self.means)
        return

    def update_means(self):
        summed_vecs = [Colorvec((0, 0, 0)) for m in self.means]
            #  summed_vecs is now a list of zeroed vecs
        for n, vec in enumerate(self.vector_list):
            for k, weight in enumerate(self.resp_vectors[n]):
                # weighted = colorvecs.scalar_vec_mult(vec, weight)
                summed_vecs[k] = summed_vecs[k] * weight

        total_resp = reduce(lambda x, y: x+y, self.resp_vectors)
        # summed_vecs holds a list of vectors that are the
        # componentwise sums of each vector assigned to each cluster.
        # total_resp is a vector that holds the total number of data
        # points assigned to each cluster.
        self.updated = False
        for mean, total_vec, resp in zip(self.means,
                                      summed_vecs, total_resp):
            if resp == 0:
                continue
            else:
                self.updated = True
                mean = total_vec * (1.0/resp)
        return

    def run(self):
        counter = 0
        while(self.updated and counter < self.cutoff_iter):
            self.assignment_step()
            self.update_means()
            counter = counter + 1
        return self.means
