import numpy as np
import pandas as pd
import json

class_type = 'bp'
path_prefix = 'data/BCLL_panther/'
path = path_prefix + 'panther_' + class_type + '/pantherGeneList '
inp_data = pd.read_csv(path_prefix + 'preprocessed_BCLL.txt', delimiter = '\t', header = None)
chart_df = pd.read_csv(path_prefix + '/panther_' + class_type + '/pantherChart.txt', delimiter = '\t', header = None).sort_values(by = 1, ascending = True)
go_df = pd.read_csv('data/Go_term_info_without_header.txt', index_col = 0)
read_order = []

cluster_ids = chart_df.loc[:, 1].tolist()

for i in range(len(cluster_ids)):
    cluster_ids[i] = cluster_ids[i][-11:-1]

print(cluster_ids)

priority_df = go_df.loc[cluster_ids, ['Depth', 'IC']].sort_values(by = ['Depth', 'IC'], ascending = [True, True])
print(priority_df.head(9))


for elem in priority_df.index.values:
    read_order.append(cluster_ids.index(elem))

print(read_order)


labels = np.zeros(inp_data.shape[0], dtype = int)
#common = 0


for count in read_order:
    df = pd.read_csv(path + '(' + str(count) + ')' + '.txt', delimiter = '\t', header = None)
    temp = df[1].tolist()
    for geneName in temp:
        if inp_data[1].str.contains(geneName).any():
            """
            if labels[inp_data[inp_data[1] == geneName].index.values.astype(int)[0]] != 0:
                common += 1
            """
            labels[inp_data[inp_data[1] == geneName].index.values.astype(int)[0]] = int(count + 1)

#print("Number of common genes:")
#print(common)

with open(path_prefix + 'panther_labels_' + class_type + '.txt', 'w') as f:
    json.dump(labels.tolist(), f)

