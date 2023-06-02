#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:37:50 2023

@author: karin
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time

data_file1 = 'Spruce_fingerprint_2017-03-10_16.48.olp.m4'
data_file2 = 'translated_data.txt'
data_file3 = 'sample_data_1_000_000.txt'

# Create an empty graph
graph = nx.Graph()
def read_data(graph):
    start_time = time.time()
    
    with open(data_file3, 'r') as file:
        print("Reading data...")
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
        end_time = time.time()
        print("Data read in, graph complete", end_time-start_time, "seconds")


# Count the number of components with at least three vertices
def three_vertices(graph):
    start_time = time.time()
    components = nx.connected_components(graph)
    count = 0
    for component in components:
        if len(component) >= 3:
            count += 1
    end_time = time.time()
    print("3 vertices", end_time-start_time, "seconds")
    return count

def component_density(graph):
    
    start_time = time.time()
        
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
    end_time = time.time()
    print("Component density: ", end_time-start_time, "seconds")
    return density_distribution
        

def node_density(graph):
    start_time = time.time()
    node_degrees = graph.degree()
    
    # Compute the node degree distribution
    degree_distribution = {}
    for node, degree in node_degrees:
        if degree in degree_distribution:
            degree_distribution[degree] += 1
        else:
            degree_distribution[degree] = 1
    end_time = time.time()
    print("Node density: ", end_time-start_time, "seconds")
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

plt.hist(degrees, bins=10, edgecolor ='black')
plt.xlabel("Degree")
plt.ylabel("Count")
plt.title("Node Degree Distribution")
  # Set logarithmic scale for the y-axis
plt.show()

