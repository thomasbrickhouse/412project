def exact_tsp_solution(input_data):
    # Parse the input
    lines = input_data.strip().split("\n")
    n, m = map(int, lines[0].split())
    edges = lines[1:]
    
    # Map letters to indices for internal processing
    vertex_map = {}
    reverse_map = {}
    counter = 0
    
    for edge in edges:
        u, v, w = edge.split()
        if u not in vertex_map:
            vertex_map[u] = counter
            reverse_map[counter] = u
            counter += 1
        if v not in vertex_map:
            vertex_map[v] = counter
            reverse_map[counter] = v
            counter += 1
    
    # Create adjacency matrix for the graph
    graph = {i: {} for i in range(n)}
    for edge in edges:
        u, v, w = edge.split()
        u_idx = vertex_map[u]
        v_idx = vertex_map[v]
        weight = float(w)
        graph[u_idx][v_idx] = weight
        graph[v_idx][u_idx] = weight

    # Solve TSP using brute force
    min_weight, optimal_path_indices = tsp_brute_force(graph, list(range(n)))
    
    # Convert the optimal path back to letters
    optimal_path = [reverse_map[idx] for idx in optimal_path_indices]
    
    # Return the result
    return f"{min_weight:.4f}\n{' '.join(optimal_path)}"

def tsp_brute_force(graph, list):
    

def main():
    example_input = """3 3
    a b 3.0
    b c 4.2
    a c 5.4"""

    solution = exact_tsp_solution(example_input)


if __name__ == "__main__":
    main()