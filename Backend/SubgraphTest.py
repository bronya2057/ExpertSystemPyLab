from graphviz import Digraph

g = Digraph('G', filename='cluster.gv')
g.attr(compound='true')
# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
#       so that Graphviz recognizes it as a special cluster subgraph

with g.subgraph(name='cluster_0') as c:
    c.node("GEw")
    c.node("GEw2")
    c.attr(style='filled')
    c.attr(color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    # c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
    c.attr(label='process #1')

with g.subgraph(name='cluster_1') as c:
    c.node_attr.update(style='filled')
    c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
    c.attr(label='process #2')
    c.attr(color='blue')

g.edge('GEw', 'b0', ltail='cluster_0', lhead='cluster_1') # cluster to cluster
g.edge('GEw', 'b0', lhead='cluster_1') # node to cluster
g.edge('start', 'b0')
g.edge('a1', 'b3')
g.edge('b2', 'a3')
g.edge('a3', 'a0')
g.edge('a3', 'end')
g.edge('b3', 'end')

g.node('start', shape='Mdiamond')
g.node('end', shape='Msquare')

g.view()


# cluster_edge.py - http://www.graphviz.org/pdf/dotguide.pdf Figure 20

# from graphviz import Digraph
#
# g = Digraph('G', filename='cluster_edge.gv')
# g.attr(compound='true')
#
# with g.subgraph(name='cluster0') as c:
#     c.edges(['ab', 'ac', 'bd', 'cd'])
#
# with g.subgraph(name='cluster1') as c:
#     c.edges(['eg', 'ef'])
#
# g.edge('b', 'f', lhead='cluster1')
# g.edge('d', 'e')
# g.edge('c', 'g', ltail='cluster0', lhead='cluster1')
# g.edge('c', 'e', ltail='cluster0')
# g.edge('d', 'h')

g.view()
