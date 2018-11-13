
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# options = {
#      'node_color': 'White',
#      'node_size': 500,
#      'width': 3,
# }
#
# G=nx.Graph()
# # G.add_node('Berea')
# # G.add_edge(5,100)
#
# i="MyNode"
# G.add_node(i,pos=(1,1))
# G.add_node(2,pos=(2,2))
# G.add_node(3,pos=(1,0))
# G.add_edge(i,2,weight=0.5)
# G.add_edge(i,3,weight="has")
# G.add_edge(i,3,weight="has")
# G.add_edge(i,i,weight="has")
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G,pos,with_labels=True, font_weight='bold', **options)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,with_labels=True, edge_labels=labels)
# plt.savefig("Plot.png")
#
#
# img = mpimg.imread('Plot.png')
# plt.imshow(img)
# plt.show()

G=nx.Graph()
G.add_node("College") # add node in random place
G.add_nodes_from(range(1,10)) # add 10 nodes with labels from list
G.add_edge(5,100) # connect node with label 5 with node with label 100 (create if not exists)
G.add_weighted_edges_from([(0,55,0.2),(1,4,7.5)]) # ([from, to , distance]), ([from, to ,dist])
G.add_path([1,2,3,440]) # connect 1,2,3 create if not exists with order
nx.draw(G, with_labels=True)
plt.draw()
plt.show()