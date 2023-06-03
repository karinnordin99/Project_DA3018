#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:17:40 2023

@author: karin
"""

import matplotlib.pyplot as plt
import math

node_degrees_data_million = "/Users/karin/DA3018/Projekt/Run/node_density_million.txt"
component_densities_data_million = "/Users/karin/DA3018/Projekt/Run/component_density_million.txt"
def plot_component_densities():
    
    with open(component_densities_data_million, 'r') as file:
        
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

            
        plt.bar(keys,values, width = 0.025)
        plt.ylim(0,1000)
        plt.xlabel('Density')
        plt.ylabel('Component')
        plt.title('Component Densities Histogram')
        #plt.yscale("log")
        plt.show()
    
plot_component_densities()

def plot_node_degree():
    
    with open(node_degrees_data_million, 'r') as file:
        
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
        plt.xlabel('Degree')
        plt.ylabel('Component')
        plt.yscale("log")
        plt.title('Node degree Histogram')
        plt.show()
    return

plot_node_degree()
