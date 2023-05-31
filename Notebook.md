Day 1:

Made a test file for the first 100.000 rows from data
head -n <num_lines> <input_file> > <output_file>

Will be converting strings to integers line by line (with open)

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
2. Store the component densities in ...
3. Generate a histogram or a table summarizing the distribution of component densities


Day 2:
Changes to using the networkx library instead of numpy, tried to translate data_file using unix command instead but will
continue with reading line for line and translate instead. 

Log-representation of histogram node degree for better visibilty

Running sample with 10^6 lines ok, but slow when going bigger, run tests to see which algorithm is slow


