from data import loaddata
from clustering import Clustering
import save
from  util import label_to_class,Estimatedk
from cluster_metrics import Metrics
import numpy as np
from emb_model.GraphEmb import gcnemb
from parameter import param
import matplotlib.pyplot as plt



data_name = param.data_name
k_clu= param.k

class main:
    def __init__(self):
        print('main')

    def run_gcn(self):
        data = loaddata(data_name)

        feat_data, adj_lists, node_map, cell_labels, graph = data.load_gcndata()
        graph_nodelist,_= data.get_graph_nodelist()

        cell_labels = label_to_class(cell_labels,data_name)

        graemb = gcnemb()
        datar = graemb.gcn_emb(feat_data=feat_data,adj_lists =adj_lists,node_map=node_map,labels = cell_labels,graph = graph,graph_nodelist =graph_nodelist)

        cluster = Clustering(k_clu)
        # datar =feat_data
        # gc = np.transpose(gc)
        result_label, sim = cluster.graphemb_cluster(datar)

        M = Metrics(result_label, cell_labels)
        ARI = M.ARI_metric()
        print('ARI: '+str(ARI))
        NMI = M.NMI_metric()
        print('NMI: '+str(NMI))
        ek = Estimatedk(sim)
        print('Estimatedk :'+str(ek))

        parameter = 'K'
        method = 'gcnemb'
        save.draw(name=data_name, method=method, data=sim, labels=cell_labels, parameter=parameter)
        save.save_result(name=data_name, method=method, matrix=sim, result_label=result_label, cell_label=cell_labels,
                         ARI=ARI, NMI=NMI, parameter=parameter)
        return ARI



    def run_gcn_sum(self):

        data = loaddata( data_name )
        feat_data, adj_lists, node_map, cell_labels, graph = data.load_gcndata()

        # feat_data,l =data.get_gc_matrix()
        # gralist, cell_labels = data.cellvec_to_graph()
        graph_nodelist,_= data.get_graph_nodelist()

        cell_labels = label_to_class(cell_labels,data_name)

        graemb = gcnemb()
        datar = graemb.gcn_emb_sum(feat_data=feat_data,adj_lists =adj_lists,node_map=node_map,labels = cell_labels,graph = graph,graph_nodelist =graph_nodelist)

        cluster = Clustering(k_clu)
        result_label, sim = cluster.graphemb_cluster(datar)

        M = Metrics(result_label, cell_labels)
        ARI = M.ARI_metric()
        print('ARI: '+str(ARI))
        NMI = M.NMI_metric()
        print('NMI: '+str(NMI))

        parameter = 'sum'
        method = 'gcnemb'
        save.draw(name=data_name, method=method, data=sim, labels=cell_labels, parameter=parameter)
        save.save_result(name=data_name, method=method, matrix=sim, result_label=result_label, cell_label=cell_labels,
                         ARI=ARI, NMI=NMI, parameter=parameter)
        return ARI

    def run_gcn_threshold(self):

        ARIs = []
        for i in range(0, 101):
            tv = i/100
            data = loaddata(data_name,tv)
            feat_data, adj_lists, node_map, cell_labels, graph = data.load_gcndata()

            graph_nodelist,_= data.get_graph_nodelist()
            cell_labels = label_to_class(cell_labels,data_name)
            graemb = gcnemb()
            datar = graemb.gcn_emb(feat_data=feat_data,adj_lists =adj_lists,node_map=node_map,labels = cell_labels,graph = graph,graph_nodelist =graph_nodelist)

            cluster = Clustering(k_clu)
            result_label, sim = cluster.graphemb_cluster(datar)
            print(result_label)
            print(cell_labels)
            M = Metrics(result_label, cell_labels)
            ARI = M.ARI_metric()
            print('ARI: '+str(ARI))
            ARIs.append(ARI*100)
            NMI = M.NMI_metric()
            print('NMI: '+str(NMI))
        K = range(0, 101)
        plt.plot(K, ARIs, 'bx-')
        plt.xlabel('Expression level threshold')
        plt.ylabel('ARI(%)')
        plt.savefig('image\\' + ' ' +data_name+ ''+ 'Expression level threshold_result.jpg')
        plt.show()
        file = open('result\\' + data_name+ ''+ 'Expression level threshold_result.txt', 'w+')
        file.write('ARIs' + '\n')
        file.write('\t'.join(str(i) for i in ARIs) + '\n')
        file.write('k ' + '\n')
        file.write('\t'.join(str(i) for i in K) + '\n')

if __name__ == '__main__':
    Main= main()
    Main.run_gcn()

