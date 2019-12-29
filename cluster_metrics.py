from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import normalized_mutual_info_score


class Metrics:
    def __init__(self,label1,label2):
        self.label1 = label1
        self.label2 = label2

    def ARI_metric(self):
        ARI = adjusted_rand_score(self.label1,self.label2)
        return ARI

    def NMI_metric(self):
        NMI = normalized_mutual_info_score(self.label1,self.label2)
        return NMI


if __name__ == '__main__':
    str1 = ' 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10  5  5  7  7  5  7  5  5  5  5  5 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11  7  5  5  7  5  5  5  7 11  7  5  7  7  5  7  5  7  5  5  5  5  5  7  5  5  5  5  7  7  7  5  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  7  7  7  7  7  7  7  7  7  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  6  9  1  1  6  6  6  6  6  6  6  6  6  6  1  6  6  6  6  9  9  6  6  9  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  1  1  1  9  1  9  6  1  9  1  9  1  9  1  9  9  9  9  1  9  1  9  1  1  9  1 '
    label1 = str1.split()
    label1 =[int(i)-1 for i in label1 ]
    print(type(label1[1]))
    print(len(label1))
    str2 = '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	8	8	8	8	8	8	8	8	8	8	8	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	8	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	7	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	9	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	4	4	4	4	4	4	4	4	10	10	10	10	10	10	10	10	10	10	10	10	10	10	10	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3'
    label2 = str2.split('\t')
    print(len(label2))
    # label2 = np.array(label2,dtype=int)
    label2 =[int(i) for i in label2 ]
    print('result')
    print('\t'.join(str(i) for i in label1))
    print('real')
    print('\t'.join(str(i) for i in label2))
    print('ARI')
    # label1 = [0,0,0,1,1,1,2,2,2,2,3,3,3]
    # label2 = [1,1,1,2,2,2,1,3,0,0,3,3,3]
    # print(type(label2[1]))
    metric = Metrics(label1,label2)
    ARI =  metric.NMI_metric()
    print(ARI)

