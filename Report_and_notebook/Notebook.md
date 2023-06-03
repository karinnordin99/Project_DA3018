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

Log-representation of histogram node degree for better visibilty

Running sample with 10^6 lines ok, but slow when going bigger, run tests to see which algorithm is slow
![image](https://github.com/supergurkan/Project_DA3018/assets/133381081/c1d4a6aa-f4aa-4376-a441-ff90bc5615a5)
![image](https://github.com/supergurkan/Project_DA3018/assets/133381081/b956738f-7c24-4f43-b55f-f903ef363627)

# Day 3 
removed function that transalates and checks for >=1000 in java program in favor of Unix commands
Data file is now down from 7 GB to 2,75GB
Rewritten the code today to Java instead of Python3

# Day 4 
Wrote python-program to "transalte" the data from the Java program to plot histograms. That is making 2 lists, one with keys and one with values
and converting the strings that java program outputs in txt-file to int/float
Debugging method "computeComponentDensity" that was returning alarming amount of components with density 0, bug was at line 100 where
the calculation of the density was badly implemented




