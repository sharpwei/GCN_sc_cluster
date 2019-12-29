
# from emb_model.graph2vec import
import networkx as nx
from sklearn.preprocessing import QuantileTransformer

# from emb_model.node2vec import Node2Vec
# from emb_model import graph2vec
import numpy as np
from emb_model.graph_aggregate import BOF,Sum
from emb_model.GCN import GCN
from emb_model.config import cfg



class gcnemb:
    def __init__(self):
        print('gcn')


    def gcn_emb(self,feat_data=None, adj_lists=None, node_map=None,labels=None,graph=None,graph_nodelist=None):

        cfg.update_config('features', feat_data)
        cfg.update_config('adj_lists', adj_lists)
        cfg.update_config('node_map', node_map)
        cfg.update_config('labels',labels)
        cfg.update_config('graph',graph)
        cfg.update_config('num_nodes',graph.number_of_nodes())
        cfg.update_config('num_features',len(feat_data))

        gcn = GCN()
        feat = gcn.exec()
        print(feat_data)
        bag = BOF(512, feat)
        gvlist = []
        for nodelist in graph_nodelist:
            gv = bag.graphhistogram(nodelist)
            gvlist.append(gv)

        gvlist = np.array(gvlist, dtype=float)
        return gvlist

    def gcn_emb_sum(self,feat_data=None, adj_lists=None, node_map=None,labels=None,graph=None,graph_nodelist=None):

        cfg.update_config('features', feat_data)
        cfg.update_config('adj_lists', adj_lists)
        cfg.update_config('node_map', node_map)
        cfg.update_config('labels',labels)
        cfg.update_config('graph',graph)
        cfg.update_config('num_nodes',graph.number_of_nodes())
        cfg.update_config('num_features',len(feat_data))

        gcn = GCN()
        feat = gcn.exec()
        print(feat_data)
        sum = Sum(feat)
        gvlist = []
        for nodelist in graph_nodelist:
            gv = sum.geaphlevel_vec(nodelist)
            gvlist.append(gv)

        gvlist = np.array(gvlist, dtype=float)
        return gvlist


if __name__ == '__main__':
    print('11')