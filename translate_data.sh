#!/bin/sh

# Author : Karin Nordin
# Make sure the datafile Spruce_fingerprint_2017-03-10_16.48.olp.m4, projekt.java, histo_plot.py is in the same directory
# and change the path_to_file to your directory you are working in, this path to file has to be changed in both the shell script,
# in the java file projekt.java and in the python file histo_plot.py. 

# chmod -x translade_data.sh
# sh translate_data.sh


echo "This project has been applied to a smaller dataset, beginning by extracting a sample from the given data with 1.000.000 lines"
echo

touch samplemillion.txt
touch translated_data_1_000_000.txt

head -n 1000000 /PATH_TO_FILE/Spruce_fingerprint_2017-03-10_16.48.olp.m4 > samplemillion.txt

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
' samplemillion.txt > translated_data_1_000_000.txt
echo "The sample has been translated, strings has been mapped to integers and only the contigs fulfilling the criterea n>=1000 are included"
echo
echo "Now running the java project"

touch result_million.txt

java projekt.java > result_million.txt

touch component_density_million.txt
touch node_density_million.txt

head -n 4 result_million.txt | tail -1 > component_density_million.txt
head -n 5 result_million.txt | tail -1 > node_density_million.txt

Python3 histo_plot.py 
