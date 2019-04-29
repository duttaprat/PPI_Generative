import numpy as np
from sklearn.metrics import *
from scipy.spatial import distance


def f3(individual, individual_list):
        all_data_columnmatrix = np.vstack(individual_list)
        silhouette_avg = silhouette_score(all_data_columnmatrix, individual.labels)
        print "##", silhouette_avg
        return silhouette_avg
