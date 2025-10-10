from collections import defaultdict

def solution(edges):
    nodes = defaultdict(lambda: {"in": 0, "out": 0})   
    for a, b in edges:
        nodes[a]["out"] += 1
        nodes[b]["in"] += 1
    g =  next(v for v, d in nodes.items() if d["in"] == 0 and d["out"] >= 2)
    
    stick = sum(1 for d in nodes.values() if d["out"] == 0)
    eight = sum(1 for d in nodes.values() if d["in"] >= 2 and d["out"] == 2)
    donut = nodes[g]["out"] - stick - eight
    return [g, donut, stick, eight]