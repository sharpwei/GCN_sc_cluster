import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np


def save_result( name,method,matrix, result_label, cell_label, ARI,NMI,parameter):
    path = os.getcwd()
    file = open('result\\'+method +'_'+name +'_'+ parameter+'_result.txt', 'w+')

    file.write('method: ' + method + '\n')
    file.write('result_matrix: ' + '\n')
    for vec in matrix:
        file.write('\t'.join(str(i) for i in vec) + '\n')
    file.write('result_label: ' + '\n')
    file.write('\t'.join(str(i) for i in result_label) + '\n')
    file.write('cell_label: ' + '\n')
    file.write('\t'.join(str(i) for i in cell_label) + '\n')
    file.write('ARI: ' + '\n')
    file.write(str(ARI) + '\n')
    file.write('NMI: ' + '\n')
    file.write(str(NMI) + '\n')

    file.close()
    print(path)

def draw( name,method,data,labels,parameter):

    data_train =data
    tsne = TSNE(n_components=2, init='pca', random_state=501)
    reduced_data = tsne.fit_transform(data_train)

    reduced_data = np.transpose(reduced_data)

    plt.scatter(reduced_data[0], reduced_data[1],  c=labels, alpha=0.5)
    plt.savefig('result\\'+method +'_'+name +'_'+ parameter+'_result.jpg')
    plt.show()

