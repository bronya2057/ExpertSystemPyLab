import networkx as nx

import matplotlib.pyplot as plt

# data= open("./data.txt", "r") # replace with the path to your edge file
G = nx.DiGraph()
edge_labels = dict()

objects = ["Candy", "Man"]

connectedObjects = [["Lion", "Man", "Caramel"], ["Lion", "Flesh"]]
inputs =[["dont like", "eats", "Ingredient of"], ["like", "Ingredient of"]]

for index, obj in enumerate(objects):
    node1 = obj
    for conObjInd, connectedObject in enumerate(connectedObjects[index]):
        node2 = connectedObject
        length = inputs[index][conObjInd]
        G.add_edge(node2,node1, label=str(length), length=length)
        edge_labels[(node1, node2)] = length # store the string version as a label



pos = nx.spring_layout(G) # set the positions of the nodes/edges/labels
nx.draw_networkx(G, pos=pos) # draw everything but the edge labels
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
plt.show()
