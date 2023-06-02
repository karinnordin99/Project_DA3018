#!/bin/sh

# Author : Karin Nordin

awk '
BEGIN {
    idx = 1
}
$7 - $6 + 1 >= 1000 && $11 - $10 + 1 >= 1000 {
    if (!($1 in vertex_map)) {
        vertex_map[$1] = idx
        idx++
    }
    if (!($2 in vertex_map)) {
        vertex_map[$2] = idx
        idx++
    }
    print vertex_map[$1], vertex_map[$2], $6, $7, $8, $10, $11, $12
}
' samplemillion.txt > "$translated_data_1_000_000.txt"

java projekt.java > million.txt

# Dividing the output data into component_density_million.txt (first array) and node_density_million.txt

Python3 histo_plot.py 
