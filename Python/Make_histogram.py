#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:17:40 2023

@author: karin
"""

import matplotlib.pyplot as plt
import math

node_degrees_data = "/Users/karin/DA3018/Projekt/Project_DA3018/node_densities_million.txt"
component_densities_data = "/Users/karin/DA3018/Projekt/Project_DA3018/Componenent_densities.txt"

def plot_component_densities():
    
    with open(node_degrees_data, 'r') as file:
        
        array_component = file.read()
        clean_array_component = array_component.replace("{", "").replace("}","").replace(",", "").replace("=", " ")
        cleaner_array_component = clean_array_component.split(" ")
        array_list = [int(x) for x in cleaner_array_component]
        
        keys = []
        values = []
        
        end_index = math.floor(len(array_list)/2)
        
        for i in range(end_index):
            
            keys.append(array_list[2*i])
            values.append(array_list[2*i +1])
            
        plt.bar(keys, values)
        plt.xlabel('degrees')
        plt.ylabel('Values')
        plt.yscale("log")
        plt.title('Component Densities Histogram')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
    
plot_component_densities()

def plot_node_degree():
    
    with open(component_densities_data, 'r') as file:
        
        array_component = file.read()
        clean_array_component = array_component.replace("{", "").replace("}","").replace(",", "").replace("=", " ")
        cleaner_array_component = clean_array_component.split(" ")
        array_list = [float(x) for x in cleaner_array_component]
        
        keys = []
        values = []
        
        end_index = math.floor(len(array_list)/2)
        
        for i in range(end_index):
            
            keys.append(array_list[2*i])
            values.append(array_list[2*i +1])
            
        plt.bar(keys, values, color="m")
        plt.xlabel('Keys')
        plt.ylabel('Values')
        plt.yscale("log")
        plt.title('Component Densities Histogram')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust spacing to prevent label cutoff
        plt.show()
    return

plot_node_degree()
