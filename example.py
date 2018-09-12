'''
Employing NetworkX to model stimuli response networks.
'''
import random
import networkx as nx
import matplotlib.pyplot as plt



# This is our draw() function for later



def initial_variables():
    # 430-770 is the human vision spectrum in THz
    color = random.randrange(430, 771)

    # We want a variable for the intensity of the stimulus
    intensity = random.uniform(0.0, 1.5)

    # This is the color for which our subject is conditioned
    conditioning = 430

    # This is the degree of "proximity" from the stimulus to the conditioned color
    proximity = 1 - (abs(conditioning - color) / 340) ** 2

    return color, intensity, conditioning, proximity

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
        print(nx.info(G))
        print("\nColor: {} THz\n".format(color),
              "Intensity: {}\n".format(intensity),
              "Conditioning: {}\n".format(conditioning),
              "Proximity: {}\n".format(proximity))
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
            G.add_node(4, name="redundance test", weight=intensity + proximity*intensity)
            G.add_edge(3, 4)
            redundance = nx.get_node_attributes(G, 'weight')[4]
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
                    G.add_edge(4, 8)
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
