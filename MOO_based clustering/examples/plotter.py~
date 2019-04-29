import os
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import style
from validity import f3

style.use("seaborn-darkgrid")

if not os.path.exists("fitness_function"):
    	os.makedirs("fitness_function")


write_file_objective1 = open('fitness_function/prostrate_NDS_fitness.txt', 'w')

class Plotter():
    def __init__(self, problem, individual_list):
        self.directory = 'plots'
        self.problem = problem
        self.individual_list= individual_list

    def plot_population_best_front(self, population, generation_number):
        if generation_number % 5 == 0:
            test = "fitness_function/prostrate_NDS_labels_"+str(generation_number)+".txt"
            write_file_objective = open(test, 'w')
            write_file_objective.write("\n\nGeneration Number:- %s \n" % generation_number)
            write_file_objective1.write("\n\nGeneration Number:- %s \n" % generation_number)
            filename = "{}/generation_prostrate{}.png".format(self.directory, str(generation_number))
            self.__create_directory_if_not_exists()
            computed_pareto_front = population.fronts[0]
            self.__plot_front(computed_pareto_front, filename,write_file_objective)

    def plot_x_y(self, x, y, x_label, y_label, title, filename):
        filename = "{}/{}.png".format(self.directory, filename)
        self.__create_directory_if_not_exists()
        figure = pyplot.figure()
        axes = figure.add_subplot(111)
        axes.plot(x, y, 'r')
        axes.set_xlabel(x_label)
        axes.set_ylabel(y_label)
        axes.set_title(title)
        pyplot.savefig(filename)
        pyplot.close(figure)

    def __create_directory_if_not_exists(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def __plot_front(self, front, filename,write_file_objective):
        figure = pyplot.figure(figsize=[16, 9], dpi=100)
        axes = figure.add_subplot(111)
        No_of_cluster = map(lambda individual: individual.no_of_Cluster, front)
        labels = map(lambda individual: individual.labels,front)
        computed_score = map(lambda individual: f3(individual, self.individual_list),front)
        write_file_objective.write("No of Cluster %s \n" % No_of_cluster)
        write_file_objective.write("labels %s \n" % labels)
        write_file_objective.close
        
        computed_f1 = map(lambda individual: individual.objectives[0], front)
        computed_f2 = map(lambda individual: individual.objectives[1], front)
        computed_f3 = map(lambda individual: individual.objectives[2], front)
        
        write_file_objective1.write("FPC %s \n" % computed_f1)
        write_file_objective1.write("PBM Index %s \n" % computed_f2)
        write_file_objective1.write("DB Index %s \n" % computed_f3)
        write_file_objective1.write("Silhoutte Score %s \n" % computed_score)
        
        axes = figure.add_subplot(221)
        pyplot.plot(computed_f1, computed_f2, 'g.')
        axes.set_xlabel('FPC')
        axes.set_ylabel('PBM Index')

        axes = figure.add_subplot(222)
        pyplot.plot(computed_f1, computed_f3,  'b.')
        axes.set_xlabel('FPC')
        axes.set_ylabel('DB Index')
        
        axes = figure.add_subplot(223)
        pyplot.plot(computed_f2, computed_f3, 'y.')
        axes.set_xlabel('PBM Index')
        axes.set_ylabel('DB Index')
        
        axes = figure.add_subplot(224, projection='3d')
        pyplot.plot(computed_f1, computed_f2, computed_f3, 'r.')
        axes.set_xlabel('FPC')
        axes.set_ylabel('PBM Index')
        axes.set_zlabel('DB Index')
        pyplot.tight_layout()
        pyplot.savefig(filename)
        #pyplot.show()
        pyplot.close(figure)
        

