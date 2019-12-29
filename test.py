import os

import grakel
import numpy as np
import matplotlib.pyplot as plt
from data import loaddata
import networkx as nx

from util import label_to_class

data_name = 'kolodziejczyk'

data = loaddata(data_name)
gc,cell_labels = data.get_gc_matrix()
new_labels = label_to_class(cell_labels,data_name)

file = open(data_name+'_type.txt','w+')
file.write('cell'+'\t'+'cell_type'+'\n')
for i in range(0,len(cell_labels)):
    file.write(str(cell_labels[i])+'\t'+str(new_labels[i])+'\n')
