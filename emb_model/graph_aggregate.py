
import  numpy as np
from sklearn.cluster import KMeans

class BOF:
    def __init__(self,k ,data):
        self.data = data
        self.k = k
        self.node_map = self.fit(self.data)

    def fit(self,data):
        km = KMeans(n_clusters=self.k,random_state=1)
        cluster =  km .fit_predict(data)
        print(cluster)
        node_map ={}
        for i in range(0,len(cluster)):
            node_map[i] = cluster[i]
            # print(type(cluster[i]))
            # print(cluster[i])
        return node_map

    def graphhistogram (self,nodes):
        gvec = np.zeros((self.k),dtype=float)
        for n in nodes:

            gvec[self.node_map[int(n)]] +=1
        return gvec

class Sum:
    def __init__(self,data):
        self.data = data
        print('sum')

    def geaphlevel_vec(self,nodelist):
        gvec = np.zeros(len(self.data[0]),dtype=float)
        for node in nodelist:
            gvec+=self.data[int(node)]

        gvec/=len(nodelist)
        return gvec
