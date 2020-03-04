# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:29:50 2020

@author: Ryan Cardin, Sumedh Sohrab
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# This script shows how to import a dataset into Python that is downloaded from KONECT.

#########################################
### START: for an undirected network ####
#########################################

### access the README for the information associated with data
flName = 'moreno_lesmis\README.moreno_lesmis'
f = open(flName, 'r')
lines = f.readlines()

print('#####################################################################')
print('############### Undirected weighted network: README #################')
print('#####################################################################')
#for ln in lines:
#   print(ln)

#### Reading the data
flName = 'moreno_lesmis\out.moreno_lesmis_lesmis'
f = open(flName, 'r')
lines = f.readlines()
##print(lines)# The first two lines are not edges in this dataset.
## You have to print lines, print(lines), and check what lines represent edges.

# Each edge has three numbers:
# num1: start of the vertex,
# num2: end of the vertex,
# num3: weight of the edge.

ug = nx.Graph()

for ln in lines[2:-1]:
    vSt = int(ln.split(' ')[0])
    vEd = int(ln.split(' ')[1])
    eLn = float(ln.split(' ')[2])
    ug.add_edge(vSt, vEd, weight=eLn)


ug.add_edge(81, 99, weight=1)
ug.add_edge(99, 98, weight=1)

pos = nx.spring_layout(ug)
###Display Undirected Network
# nodes
plt.figure(1)
plt.title('Undirected graph')
nx.draw_networkx_nodes(ug, pos, node_size=50)
# edges
nx.draw_networkx_edges(ug, pos, width=1)
plt.show()

cc = sorted(nx.connected_components(ug), key = len, reverse=True)
###Separate1 = Largest Connected Component
###Separate2 = Second largest Connected Component
separate1 = nx.Graph()
separate2 = nx.Graph()
for ln in lines[2:-1]:
    if int(ln.split(' ')[0]) in cc[0]:
        if int(ln.split(' ')[1]) in cc[0]:
            vSt = int(ln.split(' ')[0])
            vEd = int(ln.split(' ')[1])
            eLn = float(ln.split(' ')[2])
            separate1.add_edge(vSt, vEd, weight=eLn)
separate2.add_edge(81, 99, weight=1)
separate2.add_edge(99, 98, weight=1)


## Part F: Image of weight
um = nx.to_numpy_matrix(ug)
um2 = um[:100,:100]
plt.figure(5)
plt.imshow(um2, interpolation='nearest')
plt.grid(True)

## Part I: Image of Lengths Through Dijkstra's Algorithm
usp = nx.dijkstra_path(ug)
spmean = np.mean(usp)
spstd = np.std(usp)
plt.figure(6)
plt.title('Shortest Path Histogram of Undirected Graph')
plt.hist(usp, bins=100)
plt.show()


#####Calculations
mean = np.mean(ug.degree)
standardDeviation = np.std(ug.degree)
###Displaying probability distribution of Node Degree
plt.figure(2)
plt.title('Node Degree Histogram of Undirected Graph')
plt.hist(ug.degree, bins=100)
plt.show()

print("The Amount of Connected Components: ", nx.number_connected_components(ug))
ccs = [len(c) for c in sorted(nx.connected_components(ug), key=len, reverse=True)]
print("Largest Connected Component: ", ccs[0])
print("Smallest Connected Component: ", ccs[-1])
print("Mean: {0:.2}".format(mean))
print("Standard Deviation: {0:.2}".format(standardDeviation))
print("Is subnetwork 1 Eularian? ", nx.is_eulerian(separate1))
print("Is subnetwork 2 Eularian? ", nx.is_eulerian(separate2))
a = nx.minimum_spanning_tree(ug)
print(sorted(a.edges(data=True)))
print("Is tree?", nx.is_tree(a))
print("Is forest?", nx.is_forest(a))
separate1.remove_edge(3, 11)
b = nx.minimum_spanning_tree(separate1)
print(sorted(b.edges(data=True)))
print("Removed edge from largest CC")
print("Is tree?", nx.is_tree(b))
print("Is forest?", nx.is_forest(b))



#######################################
#### START: for a directed network ####
#######################################

#### access the README for the information associated with data
flName = 'moreno_highschool\README.moreno_highschool'
f = open(flName, 'r')
lines = f.readlines()

print('###################################################################')
print('############### Directed weighted network: README #################')
print('###################################################################')
#for ln in lines:
#    print(ln)

## Reading the data
flName = 'moreno_highschool\out.moreno_highschool_highschool'
f = open(flName, 'r')
lines = f.readlines()
# print(lines)# The first two lines are not edges in this dataset.
# You have to print lines, print(lines), and check what lines represent edges.

# Each edge has three numbers:
# num1: start of the vertx,
# num2: end of the vertex,
# num3: weight of the edge.


dg = nx.DiGraph()

for ln in lines[2:-1]:
    vSt = int(ln.split(' ')[0])
    vEd = int(ln.split(' ')[1])
    eLn = float(ln.split(' ')[2])
    dg.add_edge(vSt, vEd, weight=eLn)


pos = nx.spring_layout(dg)

ccs = [list(cc) for cc in nx.strongly_connected_components(dg)]
mean = np.mean(dg.degree)
standardDeviation = np.std(dg.degree)

###Displaying directed graph
plt.figure(3)
plt.title('Directed graph')
# nodes
nx.draw_networkx_nodes(dg, pos, node_size=50)
# edges
nx.draw_networkx_edges(dg, pos, width=.1, arrow=True)
plt.show()

###Displaying probability distribution of node degree
plt.figure(4)
plt.title('Node Degree Histogram of Directed Graph')
plt.hist(dg.degree, bins=100)
plt.show()

## Part F: Image of weight
dm = nx.to_numpy_matrix(dg)
dm2 = dm[:100,:100]
plt.figure(5)
plt.imshow(dm2, interpolation='nearest')
plt.grid(True)

#Calculations
print("The number of Connected Components: ", len(ccs))
print("The size of the largest Connected Component: ", len(ccs[0]))
print("The size of the smallest Connected Component: ", len(ccs[-1]))
print("Mean of Node Degree: {0:.2}".format(mean))
print("Standard Deviation of Node Degree: {0:.2}".format(standardDeviation))

