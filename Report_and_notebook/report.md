
# Report
### Karin Nordin
### 2023-06-01

## Introduction
In this project an analysis of a genome assembly graph has been made. The graph consists of vertices representing DNA segments and edges representing similarities between two vertices. The assignment provided was to report the three following results;

1. The node degree distribution 
2. The number of components of the graph G with at least three vertices 
3. A histogram of the component density distribution

## Methods
I have chosen to use HashMap to represent the graph, component densities and node degrees. The built in library for HashMap in java is efficient for lookup and direct access to data in the table. Further, I have chosen to use Set<Integer> to store vertices and neighbors to avoid duplicate elements. The choice to use depht-first search instead of breadth-first search was made due to DFS using less memory than BFS. 

#### Building the graph

I started by translaring the data in columns 1 and 2 via hashing the identifier for the first and second vertex for an edge to integers. This is done using unix commands and generates a txt-file that is significantly smaller than the original file. The data is then read using buffered reader. Depth first search (DFS) has been chosen for traversing the graph.

#### Node degree distribution

The node degree distribution is stored in a HashMap and a for loop is used to iterate over the components in the graph. The node density is then the size of each component. The method takes the graph (HashMap) as input and returns the node density (HashMap).

#### Component density

The component density is stored using a hashmap with density as keys and number of components with that specific density as values. The formula $\frac{2|E|}{|V|(|V|-1)}$ is used to calculate the density. The method takes the graph as a hashmap as input and returns the component density map.

#### At least 3 vertices

The method takes the graph in form of a map as input and returns a hashmap with degrees as keys and and the corresponding number of nodes with that specfic degree as value. 

### Time and space complexity

#### Reading the data

The method reads the file line by line so the time complexity is $O(n)$, the method then calls addEdge(graph, identifier1, identifier2) that is constant, that is $O(1)$. In conlcustion the method takes $O(E)$. In the data structure for the graph, each vertex is a key assoicated with the adjacent vertices, the values. The memory required is proportional to the sum of vertices ($V$) and edges ($E$). Therefore the spacecomplexity is $O(E+V)$ 


#### Count compoonents

Iterating over the vertices in the graph is $O(V)$, the time complexity for dfs is $O(V+E)$. So in total the time complexity is $O(V(V+E))$. In most cases the number of vertices is dominant over the number of edges, so the time complexity can be approximated by $O(V^2)$. Analysing the space complexity we see that the set "visited" is $O(V)$, "component" set is $O(V)$ and 

#### Component density

The first iteration is over all components in the graph, so the time complexity is $O(V)$ for the worst case scenario, the iteration over each vertex in every component is $O(V)$, so in total the time complexity is $O(V^2)$. For space complexity, the variables "numEdges", "numNodes", "denominator" and numerator all require constants space. In the worst case, where HashMap "densityDistribution" stores all vertices forms a single components and all vertices has uniqe density, the space complexity is $O(V)$. 

#### Node density

Both retrieving and updating the size of "degreeDistribution" is constant. The loop iterates over all components, which yields a time complexity of $O(V)$. The space complexity is, with the same argument as for the component density, $O(V)$.

## Results 

For sample of $10^6$ lines from the full data file, the number of components with at least 3 vertices are 11969. 

![Figure_1](https://github.com/supergurkan/Project_DA3018/assets/133381081/4c3479bf-a620-488a-b5a7-80a365e58955)

![Figure_2](https://github.com/supergurkan/Project_DA3018/assets/133381081/2fcd0685-0194-4652-854a-c0a3e28530ec)
In Fig.1 a histogram over the node degree distribution with degree on the x-axis and number of components with that degre on the y-axis. 
In Fig.2 a histogram over the component density distribution with density on the x-axis and number of components on the y-axis. 

## Conclusions

Based on my analysis for the time and space complexity of the diffrent methods, i suspect that the methods countComponents and computeComponentDensity are the issues when trying to run the program on the full data set. 
