from scipy import sparse
import numpy as np
from snorkel.learning import GenerativeModel
import ast
import os
import json

dataset_type = 'prostrate'
path_prefix = 'data/prostrate_panther/'
filepath = path_prefix + dataset_type + '_NDS_labels_50.txt'
#filepath = 'data/' + dataset_type + '/' + dataset_type + '_NDS_labels_50.txt'
weightpath = path_prefix + dataset_type + '_weight_list.txt'
ppitext = '_withPPI'
filename = os.path.splitext(os.path.basename(filepath))[0]

#inp_data = pd.read_csv('input.txt', delimiter = '\t', header = None)
#ppi_score = pd.read_csv('PPI.csv')

w = open(weightpath, 'r')
f = open(filepath, 'r')

with open(path_prefix + 'panther_labels_bp.txt') as json_file:
    bio_labels1 = json.load(json_file)

with open(path_prefix + 'panther_labels_mf.txt') as json_file:
    bio_labels2 = json.load(json_file)

with open(path_prefix + 'panther_labels_cc.txt') as json_file:
    bio_labels3 = json.load(json_file)

x = f.readlines()
weights = w.read()

lis_0 = x[-1]
lis_0 = lis_0[7:]

lis_0 = ast.literal_eval(lis_0)
weights = ast.literal_eval(weights)
#print(weights[:8])

lis_1 = []

for row in lis_0:
    row = [x+1 for x in row]
    lis_1.append(row)


lis_1.append(bio_labels1)
lis_1.append(bio_labels2)
lis_1.append(bio_labels3)


#weights = [2, 2, 4, 2, 2, 4, 2, 2, 4]
labels = np.array(lis_1)
sparse_labels = sparse.csr_matrix(np.transpose(labels))

final_labels = []
#print(sparse_labels)

gen_model = GenerativeModel()

#gen_model.train(sparse_labels)
gen_model.train(sparse_labels, LF_acc_prior_weights = weights)


train_marginals = gen_model.marginals(sparse_labels)


with open(path_prefix + 'Panther_Marginals_' + filename + ppitext + '.txt', 'w') as f:
    for item in train_marginals:
        f.write("%s\n" % item)


for row in train_marginals:
	final_labels.append(row.tolist().index(max(row)))


with open(path_prefix + 'Panther_gen_' + filename + ppitext + '.txt', 'w') as f:
    for item in final_labels:
        f.write("%s\n" % item)
 

