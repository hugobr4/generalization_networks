'''
Employing NetworkX to model stimuli response networks.
'''
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def initial_variables():
    # 430-770 is the human vision spectrum in THz
    #color = 500
    color = random.randrange(430, 771)

    # We want a variable for the intensity of the conditioning
    c_intensity = random.uniform(1.0, 1.5)

    # This is the color for which our subject is conditioned
    c_color = random.randrange(color-40, color+40)

    # This is the degree of "proximity" from the stimulus to the conditioned color
    if abs(c_color - color) < 40:
        proximity = 1.0 - ((abs(c_color - color) / 40)) ** 2
    else:
        proximity = 0.0

    return color, c_intensity, c_color, proximity


def main():
    G = nx.DiGraph()

    def draw():
        pos = nx.circular_layout(G)
        labels = nx.get_node_attributes(G, name="name")
        nx.draw_networkx_nodes(G, pos,
                               node_color='b',
                               alpha=0.6)

        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
        nx.draw_networkx_labels(G, pos, labels)
        print(
              "Summary \n",
              "Color: {} THz\n".format(color),
              "Condition Intensity: {}\n".format(c_intensity),
              "Sensibility: {}\n".format(sensi),
              "Valence: {}\n".format(valence),
              "Conditioning Color: {} THz\n".format(c_color),
              "Proximity: {}\n".format(proximity),
              "Response: {}".format(response)
              )

        #plt.show()

    # Firing our stimulus
    G.add_node(1, name="stimulus", weight=c_intensity)

    # Detection test
    G.add_node(2, name="detection")
    G.add_edge(1, 2)
    G.add_node(3, name="brain state")
    G.add_edge(2, 3)
    # MOTHERFUCKER redundance test
    if proximity == 1.0:
        G.add_node(4, name="redundance test", response=proximity*c_intensity)
    else:
        G.add_node(4, name="redundance test", response=proximity*c_intensity)
    G.add_edge(3, 4)
    response = nx.get_node_attributes(G, 'response')[4]
    draw()


    # I thought about 'brain state' meaning 'caring' about the stimulus
    # after it has been detected. Does it have anything to do with the
    # conditioning, though?


    # Ok, he detected the stimulus and processed it. Time for the redundance test.


    #redundance = nx.get_node_attributes(G, 'weight')[4]

if __name__ == "__main__":
    color, c_intensity, sensi, valence, c_color, proximity = initial_variables()
    main()
