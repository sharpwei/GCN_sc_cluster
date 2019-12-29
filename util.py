import math
import os

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import numpy as np
from sklearn.metrics import silhouette_score


def label_to_class(labels,name):
    if name =='polle':
        dictlabel = {}
        dictlabel['2338'] = 0
        dictlabel['2339'] = 1
        dictlabel['BJ'] = 2
        dictlabel['GW16'] = 3
        dictlabel['GW21_'] = 4
        dictlabel['GW21+2'] =5
        dictlabel['iPS'] = 6
        dictlabel['HL60'] = 7
        dictlabel['K562'] = 8
        dictlabel['Kera'] = 9
        dictlabel['NPC'] = 10
        new_label = []
        for label in labels:
            if ('2338' in label):
                new_label.append(dictlabel['2338'])
            if ('2339' in label):
                new_label.append(dictlabel['2339'])
            if ('BJ' in label):
                new_label.append(dictlabel['BJ'])
            if ('GW16' in label):
                new_label.append(dictlabel['GW16'])
            if ('GW21_' in label):
                new_label.append(dictlabel['GW21_'])
            if ('GW21+2' in label):
                new_label.append(dictlabel['GW21+2'])
            if ('iPS' in label):
                new_label.append(dictlabel['iPS'])
            if ('HL60' in label):
                new_label.append(dictlabel['HL60'])
            if ('Kera' in label):
                new_label.append(dictlabel['Kera'])
            if ('NPC' in label):
                new_label.append(dictlabel['NPC'])
            if ('K562' in label):
                new_label.append(dictlabel['K562'])

    if name == 'klein':
        dictlabel = {}
        dictlabel['d0'] = 0
        dictlabel['d2'] = 1
        dictlabel['d4'] = 2
        dictlabel['d7'] = 3
        new_label = []
        for label in labels:
            if ('d0' in label):
                new_label.append(dictlabel['d0'])
            if ('d2' in label):
                new_label.append(dictlabel['d2'])
            if ('d4' in label):
                new_label.append(dictlabel['d4'])
            if ('d7' in label):
                new_label.append(dictlabel['d7'])

    if name == 'goolam':
        dictlabel = {}
        dictlabel['2cell'] = 0
        dictlabel['4cell'] = 1
        dictlabel['8cell'] = 2
        dictlabel['16cell'] = 3
        dictlabel['32cell'] = 3
        new_label = []

        # print(len(labels))
        # print('lll')
        for label in labels:
            # print(label)
            if ('2cell' in label):
                if ('32cell' in label):
                    new_label.append(dictlabel['32cell'])
                else:
                    new_label.append(dictlabel['2cell'])
            if ('4cell' in label):
                new_label.append(dictlabel['4cell'])
            if ('8cell' in label):
                new_label.append(dictlabel['8cell'])
            if ('16cell' in label):
                new_label.append(dictlabel['16cell'])

    if name =='treutlein':
        dictlabel = {}
        dictlabel['AT1'] = 0
        dictlabel['AT2'] = 1
        dictlabel['BP'] = 2
        dictlabel['Clara'] = 3
        dictlabel['ciliated'] = 4

        new_label = []
        for label in labels:
            if ('AT1' in label):
                new_label.append(dictlabel['AT1'])
            if ('AT2' in label):
                new_label.append(dictlabel['AT2'])
            if ('BP' in label):
                new_label.append(dictlabel['BP'])
            if ('Clara' in label):
                new_label.append(dictlabel['Clara'])
            if ('ciliated' in label):
                new_label.append(dictlabel['ciliated'])

    if name =='kolodziejczyk':

        # dictlabel = {}
        # dictlabel['2i'] = 0
        # dictlabel['a2i'] = 1
        # dictlabel['lif'] = 2
        # new_label = []
        # for label in labels:
        #     if ('2i' in label):
        #         if ('a2i' in label):
        #             new_label.append(dictlabel['a2i'])
        #         else:
        #             new_label.append(dictlabel['2i'])
        #     if ('lif' in label):
        #         new_label.append(dictlabel['lif'])

        dictlabel = {}
        dictlabel['2i_2'] = 0
        dictlabel['2i_3'] = 1
        dictlabel['2i_4'] = 2
        dictlabel['2i_5'] = 3
        dictlabel['a2i_2'] = 4
        dictlabel['a2i_3'] = 5
        dictlabel['lif_1'] = 6
        dictlabel['lif_2'] = 7
        dictlabel['lif_3'] = 8
        new_label = []
        for label in labels:
            # print(label)
            if ('2i_2' in label):
                # print('11')
                if ('a2i_2' in label):
                    new_label.append(dictlabel['a2i_2'])
                else:
                    new_label.append(dictlabel['2i_2'])

            if ('2i_3' in label):
                # print('11')
                if ('a2i_3' in label):
                    new_label.append(dictlabel['a2i_3'])
                else:
                    new_label.append(dictlabel['2i_3'])

            if ('2i_4' in label):
                # print('11')
                new_label.append(dictlabel['2i_4'])

            if ('2i_5' in label):
                # print('11')
                new_label.append(dictlabel['2i_5'])

            if ('lif_1' in label):
                # print('22')
                new_label.append(dictlabel['lif_1'])
            if ('lif_2' in label):
                # print('22')
                new_label.append(dictlabel['lif_2'])
            if ('lif_3' in label):
                # print('22')
                new_label.append(dictlabel['lif_3'])


    if name =='yan':
        dictlabel = {}
        dictlabel['Oocyte'] = 0
        dictlabel['Zygote'] = 1
        dictlabel['2-cell'] = 2
        dictlabel['4-cell'] = 3
        dictlabel['8-cell'] = 4
        dictlabel['Morulae'] =5
        dictlabel['Late'] = 6

        new_label = []
        for label in labels:
            if ('Oocyte' in label):
                new_label.append(dictlabel['Oocyte'])
            if ('Zygote' in label):
                new_label.append(dictlabel['Zygote'])
            if ('2-cell' in label):
                new_label.append(dictlabel['2-cell'])
            if ('4-cell' in label):
                new_label.append(dictlabel['4-cell'])
            if ('8-cell' in label):
                new_label.append(dictlabel['8-cell'])
            if ('Morulae' in label):
                new_label.append(dictlabel['Morulae'])
            if ('Late' in label):
                new_label.append(dictlabel['Late'])
    if name =='patel':
        dictlabel = {}
        dictlabel['MGH26'] = 0
        dictlabel['MGH28'] = 1
        dictlabel['MGH29'] = 2
        dictlabel['MGH30'] = 3
        dictlabel['MGH31'] = 4

        new_label = []
        for label in labels:
            if ('MGH31' in label):
                new_label.append(dictlabel['MGH31'])
            if ('MGH30' in label):
                new_label.append(dictlabel['MGH30'])
            if ('MGH29' in label):
                new_label.append(dictlabel['MGH29'])
            if ('MGH28' in label):
                new_label.append(dictlabel['MGH28'])
            if ('MGH26' in label):
                new_label.append(dictlabel['MGH26'])


    if name =='biase':
        path = os.getcwd()
        file = open(path + '\data\\biase_cell_types.txt')
        lines = file.readlines()
        dict1 ={}
        for line in lines:
            list1 = line.strip('\n').split('\t')
            dict1[list1[0]] = list1[2]

        tran_label = []
        for i in range(0, len(labels)):
            labels[i] = dict1[labels[i]]


        dictlabel = {}
        dictlabel['zygote'] = 0
        dictlabel['2cell'] = 1
        dictlabel['4cell'] = 2
        dictlabel['blast'] = 3

        new_label = []
        for label in labels:
            if ('zygote' in label):
                new_label.append(dictlabel['zygote'])
            if ('2cell' in label):
                new_label.append(dictlabel['2cell'])
            if ('blast' in label):
                new_label.append(dictlabel['blast'])
            if ('4cell' in label):
                new_label.append(dictlabel['4cell'])

    print(labels)
    print(new_label)

    return new_label

def Estimatedk(X):

    silhouette_list =[]
    for k in range(2,31):
        kmeans_model = KMeans(n_clusters=k, random_state=1).fit(X)
        labels = kmeans_model.labels_
        # print(X.shape)
        silhouette = silhouette_score(X, labels)
        silhouette_list.append(silhouette)

    max = -100000
    estimk = 0
    for i in range(0,29):
        print(silhouette_list[i])
        if( silhouette_list[i] > max ):
            max = silhouette_list[i]
            estimk = i+2

    return estimk


def cosVector(x,y):
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return;
    result1=0.0;
    result2=0.0;
    result3=0.0;
    for i in range(len(x)):
        result1+=x[i]*y[i]   #sum(X*Y)
        result2+=x[i]**2     #sum(X*X)
        result3+=y[i]**2     #sum(Y*Y)

    return result1/((result2*result3)**0.5)