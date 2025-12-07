import random
import os

def instance_generator(
    n_nodes=8,
    filename="instances/fully_connected_instance.txt",
    min_cost=1.0,
    max_cost=20.0,
    n_triggers=None,
    seed=None
):

    rng = random.Random(seed)
    if n_triggers is None:
        n_triggers = max(1, n_nodes // 2)

    arcs = []
    arc_by_uv = {}
    arc_idx = 0

    for u in range(n_nodes):
        for v in range(n_nodes):
            if u == v: continue
            c = round(rng.uniform(min_cost, max_cost), 2)
            arcs.append((arc_idx, u, v, c))
            arc_by_uv[(u, v)] = arc_idx
            arc_idx += 1

    relations = []
    arc_indices = list(range(arc_idx))
    for rel_idx in range(n_triggers):
        trig, targ = rng.sample(arc_indices, 2)
        trig_u, trig_v = arcs[trig][1], arcs[trig][2]
        targ_u, targ_v = arcs[targ][1], arcs[targ][2]
        new_cost = round(rng.uniform(min_cost, max_cost), 2)
        relations.append((rel_idx, trig, trig_u, trig_v, targ, targ_u, targ_v, new_cost))

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{n_nodes} {len(arcs)} {len(relations)}\n")
        for a, u, v, c in arcs:
            f.write(f"{a} {u} {v} {c}\n")
        for rel in relations:
            f.write(" ".join(str(x) for x in rel) + "\n")

    print(f"Generated instance '{filename}' with {n_nodes} nodes, {len(arcs)} arcs, {len(relations)} relations.")

if __name__ == "__main__":
    instance_generator()
