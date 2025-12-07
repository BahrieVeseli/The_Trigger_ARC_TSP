INF = 1e15

def tour_arcs_from_nodes(tour_nodes, arc_by_uv):
    arc_seq = []
    for i in range(len(tour_nodes) - 1):
        u, v = tour_nodes[i], tour_nodes[i + 1]
        a = arc_by_uv.get((u, v))
        if a is None:
            return None
        arc_seq.append(a)
    return arc_seq

def compute_tour_cost_from_arcseq(arc_seq, arcs, trigger_map_by_trigger):
    
    last_activation = {}
    total = 0.0
    arc_costs = []  

    for a in arc_seq:
        applied = last_activation.get(a, arcs[a][2])
        total += applied
        arc_costs.append((a, applied))
     
        for (targ, newc) in trigger_map_by_trigger.get(a, []):
           
            last_activation[targ] = newc

    return total, arc_costs

def compute_tour_cost(tour_nodes, arcs, arc_by_uv, trigger_map_by_trigger):
    arc_seq = tour_arcs_from_nodes(tour_nodes, arc_by_uv)
    if arc_seq is None:
        return INF, []
    return compute_tour_cost_from_arcseq(arc_seq, arcs, trigger_map_by_trigger)
