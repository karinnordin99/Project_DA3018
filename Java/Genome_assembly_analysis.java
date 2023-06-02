package projekt;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.*;

public class projekt {
    public static void main(String[] args) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        System.out.println("Before readin");
        readData(graph);

        int numComponents = countComponents(graph);
        System.out.println("Number of components with at least three vertices: " + numComponents);

        Map<Double, Integer> componentDensities = computeComponentDensity(graph);
        System.out.println(componentDensities);
        

        Map<Integer, Integer> degreeDistribution = computeNodeDensity(graph);
        System.out.println(degreeDistribution);
    }

    private static void readData(Map<Integer, Set<Integer>> graph) {
        String dataFile1 = "/Users/karin/DA3018/Projekt/Project_DA3018/translated_data_sample.txt";
        String dataFile2 = "/Users/karin/DA3018/Projekt/Project_DA3018/sample_data_1_000_000.txt";
        String dataFile3 = "/Users/karin/DA3018/Projekt/Project_DA3018/translated_data.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(dataFile2))) {
            System.out.println("Reading data...");
            String line;
            while ((line = br.readLine()) != null) {
                String[] columns = line.trim().split("\\s+");

                int identifier1 = Integer.parseInt(columns[0]);
                int identifier2 = Integer.parseInt(columns[1]);

                // Add edge to the graph
                addEdge(graph, identifier1, identifier2);
            }
            System.out.println("Data read, graph complete");
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Data read and graph created.");
    }

    private static void addEdge(Map<Integer, Set<Integer>> graph, int vertex1, int vertex2) {
        // Add vertex1 and vertex2 to the graph if they don't exist
        graph.putIfAbsent(vertex1, new HashSet<>());
        graph.putIfAbsent(vertex2, new HashSet<>());

        // Add the edge between vertex1 and vertex2
        graph.get(vertex1).add(vertex2);
        graph.get(vertex2).add(vertex1);
        
        //HASHMAP FOR NODE, 
    }

    

    private static int countComponents(Map<Integer, Set<Integer>> graph) {
        int count = 0;
        Set<Integer> visited = new HashSet<>();

        for (int vertex : graph.keySet()) {
            if (!visited.contains(vertex)) {
                Set<Integer> component = new HashSet<>();
                dfs(graph, vertex, component, visited);
                if (component.size() >= 3) {
                    count++;
                }
            }
        }

        return count;
    }

    private static void dfs(Map<Integer, Set<Integer>> graph, int vertex, Set<Integer> component, Set<Integer> visited) {
        visited.add(vertex);
        component.add(vertex);

        for (int neighbor : graph.getOrDefault(vertex, Collections.emptySet())) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, component, visited);
            }
        }
    }

    private static Map<Double, Integer> computeComponentDensity(Map<Integer, Set<Integer>> graph) {
        Map<Double, Integer> densityDistribution = new HashMap<>();

        for (Set<Integer> component : graph.values()) {
            int numNodes = component.size();
            int numEdges = 0;

            for (int vertex : component) {
                numEdges += graph.getOrDefault(vertex, Collections.emptySet()).size();
            }

            double maxPossibleEdges = numNodes * (numNodes - 1) / 2.0;
            double density = maxPossibleEdges > 0 ? numEdges / maxPossibleEdges : 0.0;

            densityDistribution.put(density, densityDistribution.getOrDefault(density, 0) + 1);
        }

        return densityDistribution;
    }

    private static Map<Integer, Integer> computeNodeDensity(Map<Integer, Set<Integer>> graph) {
        Map<Integer, Integer> degreeDistribution = new HashMap<>();

        for (Set<Integer> component : graph.values()) {
            int degree = component.size();
            degreeDistribution.put(degree, degreeDistribution.getOrDefault(degree, 0) + 1);
        }

        return degreeDistribution;
    }

}


