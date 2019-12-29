
from sklearn.cluster import KMeans,SpectralClustering
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from util import Estimatedk

class Clustering:
    def __init__(self,k):
        self.k = k
        print('Clustering')

    def pca_cluster(self,data):
        # sim_matrix =self.Calculated_sim(data)
        sim_matrix = data
        print('kkk')
        print(self.k)
        km = KMeans(n_clusters=self.k, random_state=47)
        label = km.fit_predict(data)
        # print(label)
        # print('aaa')

        # sc = SpectralClustering(self.k, affinity='precomputed', n_init=100, assign_labels='discretize',random_state=47)
        # label = sc.fit_predict(sim_matrix)
        # ek = Estimatedk(sim_matrix)
        # print('Estimated')

        # print(ek)

        # X = data
        # K = range(1, 10)
        # meandistortions = []
        # for k in K:
        #     kmeans = KMeans(n_clusters=k)
        #     kmeans.fit(X)
        #     meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
        #
        # plt.plot(K, meandistortions, 'bx-')
        # plt.xlabel('k')
        # plt.ylabel(u'平均畸变程度')
        # plt.title(u'用肘部法则来确定最佳的K值');
        # plt.show()


        # sim_matrix = data
        return label,sim_matrix

    def graphkel_cluster(self,data):
        sim_matrix =self.Calculated_sim(data)
        sc = SpectralClustering(self.k, affinity='precomputed', n_init=100, assign_labels='discretize',random_state=100)
        label = sc.fit_predict(sim_matrix)

        # sim_matrix = data
        # sc = SpectralClustering(self.k, affinity='precomputed', n_init=100, assign_labels='discretize',random_state=47)
        # label = sc.fit_predict(sim_matrix)
        return label,sim_matrix


    def graphemb_cluster(self,data):
        # sim_matrix =self.Calculated_sim(data)
        sim_matrix = data
        #
        # sc = SpectralClustering(self.k, affinity='precomputed', n_init=100, assign_labels='discretize')
        #
        # label = sc.fit_predict(sim_matrix)
        km = KMeans(n_clusters=self.k,random_state=47)
        print('1111')
        print(data)
        label = km.fit_predict(data)

        return label,sim_matrix



    def Calculated_sim(self,data):
        sim_matrix = np.zeros((len(data), len(data)), dtype=float)
        for i in range(0, len(data)):
            for j in range(i, len(data)):
                x= data[i]
                y = data[j]
                odist = np.linalg.norm(x - y)
                sim = 1.0 / (1.0 + odist)
                sim_matrix[i][j], sim_matrix[j][i] = sim, sim

        return sim_matrix

    def calLaplacianMatrix(self,adjacentMatrix):

        # compute the Degree Matrix: D=sum(A)
        degreeMatrix = np.sum(adjacentMatrix, axis=1)
        print(degreeMatrix)
        # compute the Laplacian Matrix: L=D-A
        laplacianMatrix = np.diag(degreeMatrix) - adjacentMatrix

        # normailze
        # D^(-1/2) L D^(-1/2)
        # sqrtDegreeMatrix = np.diag(1.0 / (degreeMatrix ** (0.5)))
        # Laplacian = np.dot(np.dot(sqrtDegreeMatrix, laplacianMatrix), sqrtDegreeMatrix)
        lam, H = np.linalg.eig(laplacianMatrix)
        print(H.shape)
        return  laplacianMatrix


if __name__ == '__main__':
    clu = Clustering('polle')
