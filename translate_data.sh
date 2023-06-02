#!/bin/sh

# Author : Karin Nordin
echo "This project has been applies to a smaller dataset, beginning by extracting a sampla from the given data with 1.000.000 lines"
head -n 1000000 /Users/karin/DA3018/Projekt/Project_DA3018/Spruce_fingerprint_2017-03-10_16.48.olp.m4 > samplemillion.txt

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
echo "The sample has been translated, strings has been mapped to integers and only the contigs fulfilling the criterea n>=1000 are included"
echo "Now running the java project"
java projekt.java > translated_data_1_000_000.txt

touch component_density_million.txt
touch node_density_million.txt

head -4 component_density_million.txt
head -5 node_density_million.txt

Python3 histo_plot.py 
