# Day 1:

Made a test file for the first 100.000 rows from data
head -n <num_lines> <input_file> > <output_file>

Will be converting strings to integers line by line, unix or java?

Node distribution:
1. Traverse graph (BFS or DFS?)
2. count the number of edges incident to each node
3. Store the counts in a data structure (dict or array?)
4. Generate a histogram or a table summarizing the distribution of node degrees

Number of Components with at least Three Vertices:
1. Traversal to identify connected components
2. Count #components that has +3 

Component density:
1. For each connected component, compute the fraction of edges over the number of possible edges
2. Store the component densities in hashmap
3. Generate a histogram or a table summarizing the distribution of component densities


# Day 2:
Changes to using the networkx library instead of numpy, implemented translation of data file using Unix commands

Running sample with 10^6 lines ok, but slow when going bigger, run tests to see which algorithm is slow
![image](https://github.com/supergurkan/Project_DA3018/assets/133381081/c1d4a6aa-f4aa-4376-a441-ff90bc5615a5)
![image](https://github.com/supergurkan/Project_DA3018/assets/133381081/b956738f-7c24-4f43-b55f-f903ef363627)

# Day 3 
removed function that transalates and checks for >=1000 in java program in favor of Unix commands
Data file is now down from 7 GB to 2,75GB

Started to translate the code from Python3 to Java;
Chosen to use HashMap datastructure for storing the graph with Integers for vertices and Set for components. 

Implemented a method to add edge to graph using the built in function putIfAbsent() and get()
input: graph (HashMap), vertex1 (int), vertex2 (int)
output: no output

Implemented a method for reading the file using a buffered reader that adds edges using the method addEdge
input: graph
output: no outout except for string verifying graph has been built

Implemented the DFS-algorthm using recursion
input: graph (HashMap), vertex (int), component (Set), visited (Set)
output: no output

Implemented the method to count number of components with at least 3 vertices. Used a for loop to identify connected components and the the dfs method to count number of components with >3 vertices.
input: graph (HashMap)
output: number of components with >3 vertices (int)

# Day 4 
Implemented the method for computing node degree distribution. Used a for loop to iterate over the component and calculated the degree
input: graph (HashMap)
output: degreeDistribution (HashMap)

Tried implementing the method to calculate the component density but yielded unrealistic data with result well outside the interval [0,1] and a great amount of the data had density 0.

Wrote python-program to "transalte" the data from the Java program to plot histograms. That is making 2 lists, one with keys and one with values using replace("{",""), split() etc. and converting the strings that java program outputs in txt-file to int/float.

Debugging method "computeComponentDensity"; at line 100 the calculation of the density was badly implemented has been split up to numerator, denominator seperately. Also added if statement to check for zero division. Still the result is not probable with values outside the interval but more probable result, only a lot of components with density 0.

# Day 5





