# Given a list of cities and the distances between each pair of cities, 
# what is the shortest possible route that visits each city exactly once and returns to the origin city?"

# TSP can be modeled as an undirected weighted graph, such that cities are the graph's vertices, paths are the graph's edges, 
# and a path's distance is the edge's weight. It is a minimization problem starting and finishing at a specified vertex after 
# having visited each other vertex exactly once. Often, the model is a complete graph (i.e., each pair of vertices is connected by an edge). 
# If no path exists between two cities, then adding a sufficiently long edge will complete the graph without affecting the optimal tour.

# run minimum spanning tree on same inputs and compare for analysis
# MST = Lower bound helps to estimate final answer between approximate

# Heres what I need to present:
    # why MST is a good lower bound for TSP
    # convince Malloy that MST is polynomial time computable
    # showcase the lower bound, optimal, approximate exist --> test cases
    # run all of these on something the optimal cannot complete --> plot on graph

    # complete graph and generate random weights 
    # 10 different graphs
    # google mat.plot.lib

# Lab 10 MST code: # https://canvas.jmu.edu/courses/2035607/assignments/18443313

# TSP MST Implementation: 
    # add lightest edge thats not in the minimum spanning tree to the graph after 
        # you run the code to complete the tour
    # May need to change code to make it so that it doesnt backtrack
    
import random
import heapq
from collections import defaultdict

# New generate_complete_graph function with adjacency matrix as a dictionary
def generate_complete_graph(num_cities, weight_range=(1, 100)):
    graph = {}
    for i in range(1, num_cities + 1):
        city_i = f"City_{i}"
        graph[city_i] = {}
        for j in range(1, num_cities + 1):
            if i != j:  # No self-loops
                city_j = f"City_{j}"
                if city_j not in graph[city_i]:  # Avoid duplicating the edge
                    weight = random.randint(*weight_range)
                    graph[city_i][city_j] = weight
                    graph[city_j] = graph.get(city_j, {})
                    graph[city_j][city_i] = weight
    return graph

# Calculate the MST using Prim's Algorithm
def calculate_mst(graph, num_cities, start_city="City_1"):
    mst = defaultdict(list)
    visited = set()
    min_heap = [(0, start_city, None)]  # (weight, current_node, parent_node)
    total_weight = 0

    while len(visited) < num_cities:
        weight, current, parent = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if parent:
            mst[parent].append((current, weight))
            mst[current].append((parent, weight))
            total_weight += weight
        # Traverse through the neighbors from the adjacency matrix
        for neighbor, w in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, current))

    return mst, total_weight

# Calculate the lower bound for TSP
def calculate_lower_bound(graph, mst, mst_weight):
    # Convert MST edges into a set for easy lookup
    mst_edge_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges(mst))

    # Find the lightest edge not in the MST
    lightest_edge_weight = float('inf')
    for city, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edge = (min(city, neighbor), max(city, neighbor))
            if edge not in mst_edge_set and weight < lightest_edge_weight:
                lightest_edge_weight = weight

    return mst_weight + lightest_edge_weight

# Helper function to extract edges from the MST dictionary
def mst_edges(mst):
    mst_edges = []
    for city, connections in mst.items():
        for neighbor, weight in connections:
            if city < neighbor:  # To ensure each edge is printed once
                mst_edges.append((city, neighbor, weight))
    return mst_edges

# Main function
def main():
    # Readable Format

    # num_cities = 5
    # weight_range = (10, 50)

    # # Generate the graph using the new function
    # graph = generate_complete_graph(num_cities, weight_range)
    # print("Graph (Adjacency Matrix):")
    # for city, neighbors in graph.items():
    #     print(f"{city}: {neighbors}")

    # # Compute the MST
    # mst, mst_weight = calculate_mst(graph, num_cities)
    # print("\nMinimum Spanning Tree Edges:")
    # mst_edges_result = mst_edges(mst)
    # for edge in mst_edges_result:
    #     print(f"({edge[0]}, {edge[1]}, {edge[2]})")
    # print(f"Total Weight of MST: {mst_weight}")

    # # Compute the lower bound for TSP
    # lower_bound = calculate_lower_bound(graph, mst, mst_weight)
    # print(f"Lower Bound for TSP: MST ({mst_weight}) + Lightest Extra Edge ({lower_bound - mst_weight}) = {lower_bound}")

    # Just the Lower Bound Format
    
    num_cities = 5
    weight_range = (10, 50)

    # Generate the graph using the new function
    graph = generate_complete_graph(num_cities, weight_range)

    # Compute the MST
    mst, mst_weight = calculate_mst(graph, num_cities)

    # Compute the lower bound for TSP
    lower_bound = calculate_lower_bound(graph, mst, mst_weight)

if __name__ == "__main__":
    main()
