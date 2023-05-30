

from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# data_file = '/Users/karin/DA3018/Projekt/Project_DA3018/sample100000.txt'
data_file = '/Users/karin/DA3018/Projekt/Project_DA3018/Spruce_fingerprint_2017-03-10_16.48.olp.m4'

# Create a mapping from string identifiers to integer identifiers
id_mapping = {}
next_id = 0

# Create the adjacency list using a defaultdict
graph = defaultdict(list)

# Read the file line by line
with open(data_file, 'r') as file:
    for line in file:
        row = line.strip().split()
        v1, v2, _, _, _, _, start1, end1, _, _, start2, end2 = row
        if v1 not in id_mapping:
            id_mapping[v1] = next_id
            next_id += 1
        if v2 not in id_mapping:
            id_mapping[v2] = next_id
            next_id += 1
        v1_id = id_mapping[v1]
        v2_id = id_mapping[v2]
        graph[v1_id].append((v2_id, start1, end1, start2, end2))
        graph[v2_id].append((v1_id, start2, end2, start1, end1))

node_degrees = [len(edges) for edges in graph.values()]
degree_counts = np.bincount(node_degrees)
degrees = np.nonzero(degree_counts)[0]
degree_distribution = degree_counts[degrees] / len(node_degrees)

# Reset variables for counting components
visited = [False] * len(graph)
component_count = 0

def explore_component(node, component):
    visited[node] = True
    component.add(node)
    for neighbor in graph[node]:
        if not visited[neighbor[0]]:
            explore_component(neighbor[0], component)

# Compute the number of components with at least three vertices
for node in graph:
    if not visited[node]:
        component = set()
        explore_component(node, component)
        if len(component) >= 3:
            component_count += 1

# Compute component density distribution
component_densities = []
for component in graph.values():
    num_edges = len(component)
    num_vertices = len(set([v for v, _, _, _, _ in component]))
    if num_vertices < 2:
        density = 0
    else:
        density = num_edges / (num_vertices * (num_vertices - 1) / 2)  # Number of possible edges in a complete graph
    component_densities.append(density)

# Plot the node degree distribution
plt.figure()
plt.bar(degrees, degree_distribution, width=1, edgecolor='black')
plt.xlabel('Node Degree')
plt.ylabel('Fraction of Nodes')
plt.title('Node Degree Distribution')
plt.show()

# Print the number of components with at least three vertices
print("Number of Components with at least three vertices:", component_count)

# Plot the component density distribution
plt.figure()
plt.hist(component_densities, bins=20, edgecolor='black')
plt


