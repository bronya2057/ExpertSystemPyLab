import networkx as nx
import matplotlib.pyplot as plt

node_name = ['Candy']
in_objects = ["Lion", "Man", "Caramel"]
in_interactions = ["dont like", "eats", "ingridient of"]

G = nx.DiGraph()
G.add_edges_from( [('A', 'B'), ('A', 'C'), ('D', 'B'), ('AA','BB')], weight=1)
G.add_edges_from([('E', 'C'), ('E', 'F'),('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')], weight=2)
G.add_edge('Candy', 'Lion', weight="dont like")
G.add_edge('Candy', 'Man', weight="eats")
G.add_edge('Candy', 'ingridient of', weight="Caramel")
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]
print (values)
# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)

edge_labels=dict([((u,v,),d['weight'])for u,v,d in G.edges(data=True)])
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.xticks([])
plt.yticks([])
# plt.gca().axes.get_yaxis().set_visible(False)
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.show()