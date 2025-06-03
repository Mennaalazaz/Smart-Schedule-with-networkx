import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid_coloring(graph,coloring):
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            return False
    return True

def greedy_coloring(graph):
    coloring={}
    for node in graph.nodes():
        adjacent_colors = {coloring.get(neighbor) for neighbor in graph.neighbors(node) }
        coloring[node] = next(color for color in itertools.count() if color not in adjacent_colors)
    return coloring

# itertools.count() generates colors starting from 0, 1, 2, ... infinitely.
# next(...) gives the first color not used by neighbors.
# So if neighbors use 0 and 2, it will return 1.

n_nodes = 5
G= nx.Graph()
G.add_nodes_from(range(n_nodes))

# Randomly add edges to the graph
for i in range(n_nodes):
    for j in range(i+1, n_nodes):
        if random.random() < 0.3:  # 30% chance of an edge
            G.add_edge(i, j)

coloring_result = greedy_coloring(G)
print("Coloring result:", coloring_result)
print("Is valid coloring:", is_valid_coloring(G, coloring_result))
print("Number of colors used:", len(set(coloring_result.values())))

# Visualize the graph with the coloring
coloring_map= [coloring_result[node] for node in G.nodes()] # Create a list of colors for each node
nx.draw(G, node_color=coloring_map, with_labels=True, font_weight='bold')
plt.show()

