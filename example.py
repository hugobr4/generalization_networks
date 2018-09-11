'''
Employing NetworkX to model stimuli response networks.
'''
import random
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

stimulus = random.random()
conditioning = 0.2

G.add_node(1, name="stimulus", weight=stimulus)
G.add_node(2, name="detection")
G.add_node(3, name="brain state")
G.add_node(4, name="redund check", weight = stimulus + stimulus * conditioning)
#G.add_node(7, name="unlikely", weight=0.33)
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

if stimulus > 0.66:
    G.add_node(5, name="yes", weight=1)
    G.add_node(10, name="behaviour")
    G.add_edges_from([(4, 5), (5, 10)])
elif 0.33 < stimulus <= 0.66:
    G.add_node(6, name="probably", weight=0.66)
    G.add_node(9, name="valence computing")
    G.add_node(10, name="behaviour")
    G.add_edges_from([(4, 6), (6, 9), (9, 10)])
else:
    G.add_node(8, name="no")
    G.add_edges_from([(4, 8)])


pos = nx.spring_layout(G)

labels = nx.get_node_attributes(G, name="name")

nx.draw_networkx_nodes(G, pos,
                       node_color='b',
                       alpha=0.6)

nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, labels)

print(nx.info(G))

plt.show()



'''
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                  (5, 10), (6, 9), (7, 9), (9, 10)])
'''
