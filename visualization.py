import matplotlib.pyplot as plt
import random

def plot_tour(tour_nodes, arcs, trigger_map_by_trigger=None):
    coords={}
    for node in set(tour_nodes):
        coords[node]=(random.uniform(0,10), random.uniform(0,10))

    plt.figure(figsize=(8,6))
    for node,(x,y) in coords.items():
        plt.plot(x,y,'ko')
        plt.text(x+0.1,y+0.1,str(node),fontsize=10)

    for i in range(len(tour_nodes)-1):
        u=tour_nodes[i]; v=tour_nodes[i+1]
        x=[coords[u][0], coords[v][0]]; y=[coords[u][1], coords[v][1]]
        color='blue'
        if trigger_map_by_trigger and i in trigger_map_by_trigger: color='red'
        plt.plot(x,y,color=color,linewidth=1.5)

    plt.title("Trigger Arc TSP Tour")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
