import sys
from utils.helpers import *
import networkx as nx


def sol1(edges):
    triples = set()

    for e1 in edges:
        v1, v2 = e1
        for e2 in edges:
            v3, v4 = e2
            if v1 == v3:
                if {v2, v4} in edges:
                    triples.add(tuple(sorted([v1, v2, v4])))
            elif v1 == v4:
                if {v2, v3} in edges:
                    triples.add(tuple(sorted([v1, v2, v3])))

            if v2 == v3:
                if {v1, v4} in edges:
                    triples.add(tuple(sorted([v1, v2, v4])))
            elif v2 == v4:
                if {v1, v3} in edges:
                    triples.add(tuple(sorted([v1, v2, v3])))

    print("Number of all triples:", len(triples))

    total = 0
    for t in triples:
        if "t" in "".join([v[0] for v in t]):
            total += 1

    return total


def sol2(edges):
    G = nx.Graph()

    G.add_edges_from(edges)

    cliques = list(nx.find_cliques(G))
    largest_clique = max(cliques, key=len)

    print("Largest clique:", largest_clique)

    return ",".join(sorted(largest_clique))


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    edges = [set(r.split("-")) for r in file]
    edges_tuples = [tuple(r.split("-")) for r in file]

    # part1 - by hand
    s1 = sol1(edges)

    # part2 - with networkX
    s2 = sol2(edges_tuples)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
