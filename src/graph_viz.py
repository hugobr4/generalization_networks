'''
Employing NetworkX to model stimuli response networks.
'''
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))

x = np.arange(-40, 40, 0.01)
n = np.array([np.mean(xrange)])
sig = np.array([np.std(xrange)])
mu = 0.0

gauss = make_gauss(n, sig, mu)(x)

def initial_variables():
    # 430-770 is the human vision spectrum in THz
    color = random.randrange(430, 771)

    # We want a variable for the intensity of the conditioning
    c_intensity = random.uniform(0.0, 1.5)

    # This is the color for which our subject is conditioned
    conditioning = random.randrange(430,771)

    # This is the degree of "proximity" from the stimulus to the conditioned color
    if abs(conditioning - color) < 40:
        proximity = 1.0 - ((abs(conditioning - color) / 40))
    else:
        proximity = 0.0

    return color, c_intensity, conditioning, proximity

def main():
    G = nx.DiGraph()

    def draw():
        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, name="name")
        nx.draw_networkx_nodes(G, pos,
                               node_color='b',
                               alpha=0.6)

        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
        nx.draw_networkx_labels(G, pos, labels)
        if 10 in G.nodes:
            print("Summary \n",
                  "Color: {} THz\n".format(color),
                  "Intensity: {}\n".format(c_intensity),
                  "Conditioning: {} THz\n".format(conditioning),
                  "Proximity: {}\n".format(proximity),
                  "Behaviour: Yes\n",
                  "Redundance: {}".format(redundance)
                  )
        elif 4 in G.nodes:
            print("Summary \n",
                  "Color: {} THz\n".format(color),
                  "Intensity: {}\n".format(c_intensity),
                  "Conditioning: {} THz\n".format(conditioning),
                  "Proximity: {}\n".format(proximity),
                  "Behaviour: No\n",
                  "Redundance: {}".format(redundance)
                  )
        else:
            print("Summary \n",
                  "Color: {} THz\n".format(color),
                  "Intensity: {}\n".format(c_intensity),
                  "Conditioning: {} THz\n".format(conditioning),
                  "Proximity: {}\n".format(proximity),
                  "Behaviour: No\n")

        plt.show()

    # Firing our stimulus
    G.add_node(1, name="stimulus", weight=intensity)

    # Detection test
    if 430 <= color <= 770 and intensity > 0.25:
        G.add_node(2, name="detection")
        G.add_edge(1, 2)
        G.add_node(3, name="brain state")  # If our little guy is too distracted
        G.add_edge(2, 3)
        if intensity > 0.4:
            # MOTHERFUCKER redundance test
            G.add_node(4, name="redundance test", redundance=proximity*intensity)
            G.add_edge(3, 4)
            redundance = nx.get_node_attributes(G, 'redundance')[4]
            if redundance >= 1:
                G.add_node(5, name="yes")
                G.add_node(10, name="behaviour")
                G.add_edges_from([(4, 5), (5, 10)])
                draw()
            elif 0.66 <= redundance < 1:
                G.add_node(6, name="probably", weight=0.66)
                G.add_node(9, name="valence computing")
                G.add_edges_from([(4, 6), (6, 9)])
                redundance = redundance * 1/proximity
                if redundance >= 1:
                    G.add_node(5, name="yes")
                    G.add_node(10, name="behaviour")
                    G.add_edges_from([(9, 5), (5, 10)])
                    draw()
                else:
                    G.add_node(8, name="no")
                    G.add_edge(9, 8)
                    draw()
            else:
                G.add_node(8, name="no")
                G.add_edge(4, 8)
                draw()
        else:
            draw()
    else:
        draw()

    # I thought about 'brain state' meaning 'caring' about the stimulus
    # after it has been detected. Does it have anything to do with the
    # conditioning, though?


    # Ok, he detected the stimulus and processed it. Time for the redundance test.


    #redundance = nx.get_node_attributes(G, 'weight')[4]

if __name__ == "__main__":
    color, intensity, conditioning, proximity = initial_variables()
    main()
