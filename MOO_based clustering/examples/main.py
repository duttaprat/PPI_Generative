import os, sys


from preprocessing.preprocessing import preprocess, preprocess_fcm_datamatrix,AnnotatedClustering , Confidence_Score_Matrix
sys.path.append('../')
from nsga2.evolution import Evolution
from nsga2.problems.zdt import ZDT
from nsga2.problems.zdt.zdt3_definitions import ZDT3Definitions
from plotter import Plotter


def print_generation(population, generation_num):
    print("Generation:- {}".format(generation_num))


"""
    #individual_list = list that contains all gene(individual) expression values
    #individual_id_list = contains all UNIQUE GENE ID that is used for calculating BHI
    #individual_ref_id_list = contains all GENE reference id that is used for calculating PPI Interaction Score
    #all_datamatrix, all_normalized_data_matrix = preprocessed the gene expression values that is fed to FCM
    #unique_protein_ref: Contains unique Gene refernce ID
"""
individual_list = []

individual_length, individual_list , individual_id_list , individual_ref_id_list = preprocess('Input_data/preprocessed_prostrate.txt')
all_data_matrix , all_normalized_data_matrix = preprocess_fcm_datamatrix( individual_length,individual_list)


"""
Input from user
"""
chromosome_number = int(sys.argv[1])       # Enter the number of chromosome(individual) you want to generate
generation_number = int(sys.argv[2])       # Enter the maximum number of generation  


zdt_definitions = ZDT3Definitions(individual_list,individual_id_list,individual_ref_id_list)
plotter = Plotter(zdt_definitions,individual_list)
problem = ZDT(zdt_definitions, all_normalized_data_matrix,chromosome_number )
evolution = Evolution(problem, generation_number, chromosome_number, individual_list, individual_length)
evolution.register_on_new_generation(plotter.plot_population_best_front)
evolution.register_on_new_generation(print_generation)
pareto_front = evolution.evolve()
