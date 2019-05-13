This directory contains three files as described below-

### Panther.py
This file is used to generate additional labels from GO based solutions. The additional labels obtained from above is incorporated along with the labels obtained from MOO-clustering in order to increase the biological significance.

### PPI_in.py
This file is used to process the data obtained from the protein - protein Interaction database which is used to generate weights which represent the accuracy of the  weak supervision sources.

### Snorkel_test.py
This file is used to implement the generative model on the labels generated from both MOO-based clustering and GO - based solutions.
