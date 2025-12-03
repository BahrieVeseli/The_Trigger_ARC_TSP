import random
import os

def generate_instance(n_nodes=8, n_arcs=None, n_triggers=None, filename="instances/example_instance.txt"):
    if n_arcs is None: n_arcs = n_nodes*(n_nodes-1)
    if n_triggers is None: n_triggers = n_nodes

    arcs = []
    arc_idx = 0
    arc_by_uv = {}
    for u in range(n_nodes):
        for v in range(n_nodes):
            if u==v: continue
            cost = round(random.uniform(1, 20),2)
            arcs.append((arc_idx,u,v,cost))
            arc_by_uv[(u,v)] = arc_idx
            arc_idx += 1

    relations=[]
    arc_indices = list(range(arc_idx))
    for _ in range(n_triggers):
        t,a=random.sample(arc_indices,2)
        new_cost = round(random.uniform(1,20),2)
        relations.append((t,a,new_cost))

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,"w") as f:
        f.write(f"{n_nodes} {len(arcs)} {len(relations)}\n")
        for a,u,v,c in arcs:
            f.write(f"{a} {u} {v} {c}\n")
        for t,a,c in relations:
            f.write(f"{t} {a} {c}\n")
    print(f"Generated instance '{filename}' with {n_nodes} nodes, {len(arcs)} arcs, {len(relations)} triggers.")

if __name__=="__main__":
    generate_instance()
