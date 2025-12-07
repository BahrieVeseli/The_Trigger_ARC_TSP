import math
import matplotlib.pyplot as plt
from cost_eval import compute_tour_cost

def plot_tour(tour_nodes, arcs, arc_by_uv, trigger_map_by_trigger, title="Trigger Arc TSP Tour"):
    n = max(tour_nodes) + 1
    radius = 5
    coords = {
        node: (
            radius * math.cos(2 * math.pi * node / n),
            radius * math.sin(2 * math.pi * node / n)
        )
        for node in range(n)
    }

    total_cost, arc_costs = compute_tour_cost(tour_nodes, arcs, arc_by_uv, trigger_map_by_trigger)

    plt.figure(figsize=(8, 6))
    for node, (x, y) in coords.items():
        plt.plot(x, y, "ko")
        plt.text(x + 0.15, y + 0.15, str(node), fontsize=10)
    for (aidx, cost) in arc_costs:
        u, v, _ = arcs[aidx]
        color = 'red' if aidx in trigger_map_by_trigger else 'blue'
        plt.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color=color, linewidth=1.5)
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
