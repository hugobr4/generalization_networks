'''
Employing NetworkX to model stimuli response networks.
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1, name="stimulus")
G.add_node(2, name="detection")
G.add_node(3, name="brain state")
G.add_node(4, name="redund check")
G.add_node(5, name="yes", weight=1)
G.add_node(6, name="probably", weight=0.66)
G.add_node(7, name="unlikely", weight=0.33)
G.add_node(8, name="no")
G.add_node(9, name="valence computing")
G.add_node(10, name="behaviour")
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                  (5, 10), (6, 9), (7, 9), (9, 10)])


pos = nx.spring_layout(G)

labels = nx.get_node_attributes(G, name="name")

nx.draw_networkx_nodes(G, pos,
                       nodelist=[i for i in range(1,11)],
                       node_color='b',
                       alpha=0.6)

nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, labels)

print(nx.info(G))

plt.show()





# e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
# G.add_weighted_edges_from(e)
#
# print(nx.dijkstra_path(G, 'a', 'd'))
# ['a', 'c', 'd']
#
# G = nx.cubical_graph()
#
# plt.subplot(121)
# nx.draw(G)
#
# plt.subplot(122)
# nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
#
# plt.show()
