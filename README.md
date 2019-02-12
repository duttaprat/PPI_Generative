# PPI_Generative
 **This repository contains the code for the paper-** *Integration of Deep-learning and Multi-objective Optimization for Labeling Gene Expression Profiles*
 
In the field of biomedical informatics, for tasks such as medical diagnosis or disease gene classification, acquiring class labels is very much essential and costly. On the contrary, collecting a large number of unlabeled data is comparatively cheap. In this paper, we have combined a **Multi-Objective Optimization (MOO)** based genetic clustering technique with **Snorkel Generative Model** to predict class labels of unlabeled gene expression data. The key contribution of the proposed model is to generate class labels without using any prior information of labeled data. More precisely, a linkage graph is developed by ensembling the non-dominated solutions of the proposed MOO-based clustering technique. This linkage graph is used to label some part of the gene expression data on the basis of the distinct connected components. Finally, the trained deep neural models are used to predict the remaining unlabeled gene expression data.
- **Authors:**
- **Affiliation:**
- **Submitted:**
- **Accepted:**
 ## Motivation
One of the crucial problems in the field of functional genomics is to understand the biological functionalities of the genes. Analyzing the gene expression values leads to the discovery of some biologically significant genes and also to understand the gene functions. In the field of bioinformatics, gene function prediction is often formalized as a classification problem. To accomplish this type of biological research, i.e., for classifying the disease genes, identifying the pathway markers, understanding the specificity of protein bindings, labeled biological data is more essential than unlabeled data. But collecting labeled data is very much expensive as that requires a lot of human effort and expertise. Moreover, collection of a huge amount of unlabeled data is relatively easy. In this paper we explore semi-supervised learning techniques to predict the label for the unlabeled genes using machine learning clustering algorithms and deep learning architecture.
 ## Getting Started 
 These instructions will allow you to emulate the results obtained from the code for development and testing purposes.
 ### Prerequisites
* **[Python 2.7+](https://www.python.org/downloads/release/python-2713/)**{*MOO based Clustering done in Python older version.*}
* **[Python 3.6](https://www.python.org/downloads/)** {*Label Prediction done in Python newer version.*}
* **[sklearn](https://scikit-learn.org/stable/install.html)**
* **[matplotlib 2.0+](https://matplotlib.org/users/installing.html)**
* **[mpl_toolkits](https://matplotlib.org/2.0.2/mpl_toolkits/index.html)**
* **[numpy 1.10+](https://pypi.org/project/numpy/)**
* **[Snorkel](https://github.com/HazyResearch/snorkel)**

### Setup
All our code is implemented in Python. The installation instructions are as follows:                                                       
> git clone                                                                                                     
> python get-pip.py                                                                                                                  
> pip install numpy                                                                                                                     
> pip install matplotlib                                                                                                                 
> pip install numpy scipy scikit-learn                                                                                                   
> If the above doesn't work try upgrading the setup tools as follows -                                                                   
> pip install --upgrade setuptools

**NOTE:** To install Snorkel follow the given steps or refer **[here](https://github.com/HazyResearch/snorkel)** .
This section is meant to help setup Snorkel on your systems. For more detailed instructions see the **[Installation section](https://github.com/HazyResearch/snorkel#installation)**. These instructions assume that you already have conda installed.
First, download and extract a copy of the Snorkel directory from a **[GitHub release](https://github.com/HazyResearch/snorkel/releases)** (version 0.7.0 or greater). Then navigate to the root of the snorkel directory in a terminal and run the following:
> Install the environment                                                                                                               
> conda env create --file=environment.yml                                                                                               
> Activate the environment                                                                                                              
> source activate snorkel                                                                                                               
> Install snorkel in the environment                                                                                                     
> pip install .                                                                                                                         
## Description
### 1.
### 2.
### 3.
## Authors
- [Pratik Dutta](http://www.iitp.ac.in/~pratik.pcs16/) (Ph.D, Indian Institute Of Technology Patna)
- Sanket Pai (B.tech, Indian Institute Of Technology Patna)
- Aviral Kumar (B.tech Indian Institute Of Technology Patna)
## Acknowledgement
This research work was completed under the guidance of [Dr. Sriparna Saha](http://www.iitp.ac.in/~sriparna/) of Computer Science and Technology Department at Indian Institute Of Technology Patna.
## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


