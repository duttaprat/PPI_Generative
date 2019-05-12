import numpy as np
import ast
import pandas as pd
import math


dataset_type = 'prostrate'
path = 'data/' + dataset_type + '/'

f = open(path + dataset_type + '_NDS_labels_50.txt','r')
x = f.readlines()

inp_data = pd.read_csv(path + 'preprocessed_' + dataset_type + '.txt', delimiter = '\t', header = None)

df = pd.read_csv('data/PPI_matrix/ppi_matrix.csv', header = 1, index_col = 0)
ppi_df = df.apply(pd.to_numeric, errors='coerce')

clus_list = x[-1]
clus_num = x[-2]

clus_num= clus_num[14:]
clus_num = ast.literal_eval(clus_num)

clus_list = clus_list[7:]
clus_list = ast.literal_eval(clus_list)

#matrix_list = []
#p = ppi_score[(ppi_score[['Gene A','Gene B']].values == ['RELA', 'YWHAE']).all(axis=1)].iloc[0, 2]
#for row in lis_0:
#    labels = np.array(row)


weight_list = [2, 3]
for i in range(len(clus_num)):
    answer=[]
    temp_arr=clus_list[i]
    for j in range(clus_num[i]):
        list=[]
        for x in range(len(temp_arr)):
              if temp_arr[x]==j:
                  list.append(x)
        answer.append(list)

    weight = 0
    for list0 in answer:
      ppi_sum = 0
      d = 0
      for m in list0:
        #print("m:")
        #print(m)
        for n in list0:
             if(list0.index(n)>=list0.index(m)):
                #print("n:")
                #print(n)
                geneA = inp_data.iloc[m, 1]
                geneB = inp_data.iloc[n, 1]
                if (geneA in ppi_df.index and geneB in ppi_df.columns):
                    ppi_value = ppi_df.loc[geneA, geneB]
                    if(not math.isnan(ppi_value)):
                        ppi_sum += float(ppi_value)
                        d += 1
                        #print(geneA)
                        #print(geneB)
                        #print(ppi_value)

                elif(geneB in ppi_df.index and geneA in ppi_df.columns):
                    ppi_value = ppi_df.loc[geneB, geneA]
                    if(not math.isnan(ppi_value)):
                        ppi_sum += float(ppi_value)
                        d += 1
                        #print(geneA)
                        #print(geneB)
                        #print(ppi_value)
        #print(ppi_sum)
      if (ppi_sum == 0 or math.isnan(ppi_sum)):
        ppi_avg = 0
      else:
        ppi_avg = ppi_sum / float(d)
      print("ppi_avg:")
      print(ppi_avg)
      weight += ppi_avg
    weight /= clus_num[i]
    print("weight:")
    print(weight)
    weight_list.append(weight)

print(weight_list)

with open(path + dataset_type + '_weight_list.txt', 'w') as f:
    f.write(str(weight_list))
