import copy
import math
from collections import defaultdict

import networkx as nx
import numpy as np
import os
import matplotlib.pyplot as plt
import  sklearn.preprocessing as pre

from sklearn.preprocessing import QuantileTransformer,StandardScaler
from parameter import param

# yan = 0.71
# patel = 0.5
# polle = 0.9
# treutlein = 0.6
# klein = 0.6
threshold_value = param.map_threshold


class loaddata:
    def __init__(self,name):
        self.name = name
        # self.threshold_value = tv
        print('loaddata__'+ self.name)
        # print(self.threshold_value)

    def get_gc_matrix(self):
        path = os.getcwd()
        file = open(path+'\data\\'+self.name+ '_gene_feature.txt')
        lines = file.readlines()
        raw = 0
        list1 = []

        for line in lines:
            raw += 1
            if raw == 1:
                list = line.strip('\n').split('\t')
                col = len(list)
                cell_label = list[1:col - 1]
                # print(y)
            if raw != 1:
                list = line.strip('\n').split('\t')
                col = len(list)
                # dict[list[0]] = raw - 2
                temp = np.array(list[1:col - 1], dtype=float)
                list1.append(temp)

        gc = np.array(list1,dtype=float)

        # print(gc.shape)
        return gc, cell_label

    def deal_gc_matrix(self):
        gc, cell_label = self.get_gc_matrix()
        threshold = []
        # print(gc.shape)

        # scaler = StandardScaler()
        # gc = scaler.fit_transform(gc)
        for g in gc:
            g = sorted(g)
            threshold.append(g[int(len(g) *threshold_value)])

        for i in range(0, len(gc)):
            for j in range(0, len(gc[i])):
                if (gc[i][j] <  threshold[i]):
                    gc[i][j] = 0
                else:
                    gc[i][j] = 1

        return gc, cell_label,threshold

    def get_edgelist(self):
        path = os.getcwd()
        file = open(path + '\data\\' + self.name + '_gene_ppigraph.txt')
        lines = file.readlines()
        edgelist = []
        for line in lines:
            temp = line.strip('\n').split('\t')
            edgelist.append(temp)

        return edgelist

    def generate_graph(self):

        listedge = self.get_edgelist()
        G = nx.Graph()
        for e in listedge:
            G.add_edge(e[0],e[1],edge_label = float(e[2]))
            G.add_node(e[0],node_label = str(e[0]))
            G.add_node(e[1],node_label = str(e[1]))

        print(G.number_of_edges())
        print(G.degree())
        print(G.number_of_nodes())
        print('generate_graph')
        return G

    def cellvec_to_graph(self):

        graph = self.generate_graph()
        gc,cell_label = self.get_gc_matrix()
        _,_,threshold= self.deal_gc_matrix()

        cell_sample = np.transpose(gc)
        graph_list = []

        list1 =[]
        for sc in cell_sample:
            gra = self.map(sc,threshold,graph)
            graph_list.append(gra)
            list1.append(gra.number_of_nodes())
        for g in graph_list:
            print(g.number_of_nodes())
            for node in g.nodes:
                g.add_node(node,node_label = str(node))

        print('cellvec_to_graph')
        return graph_list,cell_label

    def map(self,scell,threshold,graph):
        # G = nx.Graph()
        G = copy.deepcopy(graph)
        for i in range(0,len(scell)):
            if(scell[i]>threshold[i]):
                G.add_node(str(i),node_weight =scell[i])
            else:
                G.add_node(str(i))
                G.remove_node(str(i))
        return G

    def get_graph_nodelist(self):
        gc, cell_label, threshold = self.deal_gc_matrix()
        nodelist = []
        for sc in  np.transpose(gc):
            nodes = []
            for i in range(0,len(sc)):
                if sc[i] == 1:
                    nodes.append(str(i))
            nodelist.append(nodes)

        return nodelist,cell_label

    def load_gcndata(self):
        feat_data, labels, threshold = self.deal_gc_matrix()
        graph = self.generate_graph()

        node_map = {}
        for i in range(0, len(feat_data)):
            node_map[str(i)] = i

        adj_lists = defaultdict(set)
        for e in graph.edges:
            n1 = node_map[e[0]]
            n2 = node_map[e[1]]
            adj_lists[n1].add(n2)
            adj_lists[n2].add(n1)

        return feat_data, adj_lists, node_map,labels,graph

if __name__ == '__main__':
    data = loaddata('yan')
    data.cellvec_to_graph()