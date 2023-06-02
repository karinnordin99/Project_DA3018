

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()
def read_data(graph):
    
    with open(data_file2, 'r') as file:
        print("open")
        for line in file:
            # Split the line into columns
            columns = line.strip().split()
    
            # Extract relevant information from the columns
            identifier1 = int(columns[0])
            identifier2 = int(columns[1])
            # overlap_start1 = int(columns[2])
            # overlap_end1 = int(columns[3])
            # contig_length1 = int(columns[4])
            # overlap_start2 = int(columns[5])
            # overlap_end2 = int(columns[6])
            # contig_length2 = int(columns[7])

            graph.add_edge(identifier1, identifier2)
        print("graphed")


# Count the number of components with at least three vertices
def three_vertices(graph):
    components = nx.connected_components(graph)
    count = 0
    for component in components:
        if len(component) >= 3:
            count += 1
    return count

def component_density(graph):
        
    components = nx.connected_components(graph)
    densities = []
    for component in components:
        subgraph = graph.subgraph(component)
        num_nodes = subgraph.number_of_nodes()
        num_edges = subgraph.number_of_edges()
        density = 0.0
        if num_nodes > 1:
            max_possible_edges = (num_nodes * (num_nodes - 1)) / 2  # Complete graph
            density = num_edges / max_possible_edges
        densities.append(density)

    # Compute the component density distribution
    density_distribution = {}
    for density in densities:
        if density in density_distribution:
            density_distribution[density] += 1
        else:
            density_distribution[density] = 1
    return density_distribution
        

def node_density(graph):
    node_degrees = graph.degree()
    
    # Compute the node degree distribution
    degree_distribution = {}
    for node, degree in node_degrees:
        if degree in degree_distribution:
            degree_distribution[degree] += 1
        else:
            degree_distribution[degree] = 1
    return degree_distribution

# Driver code
read_data(graph)

# Compute the number of components with at least three vertices
num_components = three_vertices(graph)
print("Number of components with at least three vertices:", num_components)

# Compute the component density distribution
component_densities = component_density(graph)

# Plot the histogram of component densities
plt.hist(component_densities, bins=10, edgecolor='black')
plt.xlabel("Density")
plt.ylabel("Count")
plt.title("Component Density Distribution")
plt.show()

# Compute the node degree distribution
degree_distribution = node_density(graph)

# Plot the histogram of node degrees
degrees = list(degree_distribution.keys())
counts = list(degree_distribution.values())

plt.bar(degrees, counts)
plt.xlabel("Degree")
plt.ylabel("Count")
plt.title("Node Degree Distribution")
plt.yscale('log')  # Set logarithmic scale for the y-axis
plt.show()



