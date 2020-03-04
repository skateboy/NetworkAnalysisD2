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
#### Reading the data
flName = 'moreno_lesmis\out.moreno_lesmis_lesmis'
f = open(flName, 'r')
lines = f.readlines()
# Each edge has three numbers:
# num1: start of the vertex,
# num2: end of the vertex,
# num3: weight of the edge.

####################################################################################
# Note: Part D was not available for the undirected graphs
####################################################################################

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


cc = sorted(nx.connected_components(ug), key=len, reverse=True)
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

# Part C: Histogram representing the lengths of all paths between 2 nodes
paths = nx.all_simple_paths(separate1, 1, 13, 9)
hold = []
hold = list(paths)
pathlen = []
for x in hold:
    pathlen.append(len(x))
plt.figure(11)
plt.title('Probability Distribution of lengths of all paths between 2 arbitrary nodes: Undirected Graph')
plt.hist(pathlen, bins=50)

# Part G: Compare copies of the network and then compare again after adding 10 edges
n1 = separate1.copy()
n2 = separate1.copy()
print("N1 and N2 copy: ")
if n1.number_of_edges() == n2.number_of_edges():
    print("They are equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N2 num of edges: ", n2.number_of_edges())
else:
    print("They are not equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N2 num of edges: ", n2.number_of_edges())

n3 = n2.copy()
n3.add_edge(5, 6, weight=1)
n3.add_edge(5, 7, weight=1)
n3.add_edge(25, 8, weight=1)
n3.add_edge(26, 8, weight=1)
n3.add_edge(5, 11, weight=1)
n3.add_edge(36, 7, weight=1)
n3.add_edge(1, 5, weight=1)
n3.add_edge(1, 61, weight=1)
n3.add_edge(9, 16, weight=1)
n3.add_edge(19, 10, weight=1)

print("Added 10 edges to N3: ")
if n1.number_of_edges() == n3.number_of_edges():
    print("They are equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N3 num of edges: ", n3.number_of_edges())
else:
    print("They are not equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N3 num of edges: ", n3.number_of_edges())

## Part F: Image of weight
um = nx.to_numpy_matrix(ug)
um2 = um[:100, :100]
plt.figure(2)
plt.imshow(um2, interpolation='nearest')
plt.grid(True)


# Part I: Image of Lengths Through Dijkstra's Algorithm
####################################################
#to_numpy_matrix only works with directed graphs
####################################################

# Part B: Standard Deviation and Mean with a Histogram representing the Probability Distribution of the Node Degree
mean = np.mean(ug.degree)
standardDeviation = np.std(ug.degree)
print("Mean of Node Degree: {0:.2}".format(mean))
print("Standard Deviation of Node Degree: {0:.2}".format(standardDeviation))
###Displaying probability distribution of Node Degree
plt.figure(4)
plt.title('Node Degree Histogram of Undirected Graph')
plt.hist(ug.degree, bins=100)


# Part A: Analysis of Connected Components
print("The Amount of Connected Components: ", nx.number_connected_components(ug))
ccs = [len(c) for c in sorted(nx.connected_components(ug), key=len, reverse=True)]
print("Largest Connected Component: ", ccs[0])
print("Smallest Connected Component: ", ccs[-1])
# Part E: Euler Network
print("Is subnetwork 1 Eularian? ", nx.is_eulerian(separate1))
print("Is subnetwork 2 Eularian? ", nx.is_eulerian(separate2))
# Part H: Minimum Spanning tree of network (ug) and largest CC (separate1)
a = nx.minimum_spanning_tree(ug)
print("Is tree?", nx.is_tree(a))
print("Is forest?", nx.is_forest(a))
separate1.remove_edge(3, 11)
b = nx.minimum_spanning_tree(separate1)
print("Removed edge from largest CC")
print("Is tree?", nx.is_tree(b))
print("Is forest?", nx.is_forest(b))


flName = 'moreno_highschool\README.moreno_highschool'
f = open(flName, 'r')
lines = f.readlines()

print('###################################################################')
print('############### Directed weighted network: README #################')
print('###################################################################')
## Reading the data
flName = 'moreno_highschool\out.moreno_highschool_highschool'
f = open(flName, 'r')
lines = f.readlines()
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

dg.add_edge(99, 98, weight=1)
dg.add_edge(98, 100, weight=1)
pos = nx.spring_layout(dg)

z = dg.copy()
z1 = nx.to_undirected(z)

###Displaying directed graph
plt.figure(5)
plt.title('Directed graph')
# nodes
nx.draw_networkx_nodes(dg, pos, node_size=50)
# edges
nx.draw_networkx_edges(dg, pos, width=.1, arrow=True)


# Part B: Standard Deviation and Mean with a Histogram representing the Probability Distribution of the Node Degree
###Displaying probability distribution of node degree
plt.figure(6)
plt.title('Node Degree Histogram of Directed Graph')
plt.hist(dg.degree, bins=100)
mean = np.mean(dg.degree)
standardDeviation = np.std(dg.degree)
print("Mean of Node Degree: {0:.2}".format(mean))
print("Standard Deviation of Node Degree: {0:.2}".format(standardDeviation))

# Part G: Compare copies of the network and then compare again after adding 10 edges
n1 = dg.copy()
n2 = dg.copy()
print("N1 and N2 copy:")
if n1.number_of_edges() == n2.number_of_edges():
    print("They are equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N2 num of edges: ", n2.number_of_edges())
else:
    print("They are not equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N2 num of edges: ", n2.number_of_edges())
n3 = n2.copy()
n2.add_edge(1, 5, weight=1)
n3.add_edge(1, 6, weight=1)
n3.add_edge(1, 7, weight=1)
n3.add_edge(1, 8, weight=1)
n3.add_edge(1, 9, weight=1)
n3.add_edge(1, 10, weight=1)
n3.add_edge(3, 5, weight=1)
n3.add_edge(4, 5, weight=1)
n3.add_edge(7, 5, weight=1)
n3.add_edge(8, 5, weight=1)
print("Added 10 edges to N3:")
if n1.number_of_edges() == n3.number_of_edges():
    print("They are equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N3 num of edges: ", n3.number_of_edges())
else:
    print("They are not equal")
    print("N1 num of edges: ", n1.number_of_edges())
    print("N3 num of edges: ", n3.number_of_edges())

## Part F: Image of weight
dm = nx.to_numpy_matrix(dg)
dm2 = dm[:100, :100]
plt.figure(7)
plt.imshow(dm2, interpolation='nearest')
plt.grid(True)

# Part D: Histogram representing all simple circuits of a node
#It works but the computation time is too much for my computer
#circuit = nx.simple_cycles(dg)
#circuitnode = []
#for i in circuit:
#    if i[0] == 1:
#        circuitnode.append(len(i))
#plt.figure(10)
#plt.title('Histogram of length of all simple cycles of a node')
#plt.hist(circuitnode, bins=100)

## Part I: Image of Lengths Through Dijkstra's Algorithm
########################################################################################################
# Issues feeding lengths of paths with direction into nx.to_numpy_matrix because it only accepts directed graphs
########################################################################################################
#dsp = nx.dijkstra_path(dg, 1, 13)
#dsp2 = nx.to_numpy_matrix(dsp)
#spmean = np.mean(dsp2)
#spstd = np.std(dsp2)

allp = nx.all_pairs_dijkstra_path_length(dg)
allp2 = list(allp)
totalweight = []
for x in allp2:
    y = 1
    for y in x[1]:
        totalweight.append(x[1][y])

mean = np.mean(totalweight)
standardDeviation = np.std(totalweight)
# Histogram representing the Probability Distribution of lengths of shortest paths between 2 nodes using Dijkstra's Algorithm
plt.figure(8)
plt.title('Shortest path between all nodes probability distribution: Directed Graph: Mean: {0:.2}'.format(
    mean) + ' STD: {0:.2}'.format(standardDeviation))
plt.hist(totalweight, bins=100)

###creating the separate graphs for the connected components
###separate1 = Largest CC
###separate2 = Second Largest CC
separate1 = nx.Graph()
for ln in lines[2:-1]:
    if int(ln.split(' ')[0]) in cc[0]:
        if int(ln.split(' ')[1]) in cc[0]:
            vSt = int(ln.split(' ')[0])
            vEd = int(ln.split(' ')[1])
            eLn = float(ln.split(' ')[2])
            separate1.add_edge(vSt, vEd, weight=eLn)
separate2 = nx.Graph()
separate2.add_edge(99, 98, weight=1)
separate2.add_edge(98, 100, weight=1)

# Part C: Histogram representing the lengths of all paths between 2 nodes
paths = nx.all_simple_paths(separate1, 1, 5, 8)
hold = []
hold = list(paths)
pathlen = []
for x in hold:
    pathlen.append(len(x))
plt.figure(9)
plt.title('Probability Distribution of lengths of all paths between 2 arbitrary nodes: Directed Graph')
plt.hist(pathlen, bins=50)

# Part A: Analysis of Connected Components
cc = sorted(nx.connected_components(z1), key=len, reverse=True)
print("The number of Connected Components: ", len(ccs))
print("The size of the largest Connected Component: ", len(cc[0]))
print("The size of the smallest Connected Component: ", len(cc[-1]))

# Part H: Minimum Spanning tree of network (ug) and largest CC (separate1)
g = nx.to_undirected(dg)
a = nx.minimum_spanning_tree(g)
print("Is forest?: ", nx.is_forest(a))
print("Is tree?: ", nx.is_tree(a))
separate1.remove_edge(1, 3)
b = nx.minimum_spanning_tree(separate1)
print("Removed edge from largest cc")
print("Is forest? ", nx.is_forest(b))
print("Is tree? ", nx.is_tree(b))
# Part E: Euler Network
print("Is subnetwork 1 Eularian? ", nx.is_eulerian(separate1))
print("Is subnetwork 2 Eularian? ", nx.is_eulerian(separate2))
plt.show()
