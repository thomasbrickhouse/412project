import time
import json
import os
from cs412_tsp_exact import tsp_exact, parse_input


def load_graph(file_name):
    """
    Load a graph from a test case file.

    Args:
    file_name (str): Path to the test case file.

    Returns:
    tuple: A parsed graph (dict) and the number of vertices.
    """
    with open(file_name, "r") as f:
        line = f.readline()
        v = int(line.split()[0])
        graph = line + f.read()
    return parse_input(graph), v


def benchmark(test_case, max_vertices_for_exact=15):
    """
    Benchmark the exact TSP solution for a given test case.

    Args:
    test_case (str): Path to the test case file.
    max_vertices_for_exact (int): Maximum number of vertices for exact TSP.

    Returns:
    dict: Benchmark results.
    """
    graph, num_vertices = load_graph(test_case)

    # Skip exact solution for graphs with too many vertices
    if num_vertices > max_vertices_for_exact:
        exact_runtime = None
        exact_cost = None
    else:
        start_time = time.time()
        path, exact_cost = tsp_exact(graph)
        exact_runtime = time.time() - start_time

    print(f"Test case complete: {test_case}")

    return {
        "test_case": os.path.basename(test_case),
        "num_vertices": num_vertices,
        "exact_cost": exact_cost,
        "exact_runtime": exact_runtime,
    }


if __name__ == "__main__":
    # List of test case files
    test_cases = [
        "testCase1",
        "testCase2",
        "testCase3",
        "testCase4",
        "testCase5",
        "testCase6",
        "testCase7",
        "testCase8",
        "testCase9",
        "testCase10",
    ]

    results = []

    # Run the benchmark for each test case
    for test_case in test_cases:
        result = benchmark(test_case)
        results.append(result)

    # Save the results to a JSON file
    with open("benchmark_results_exact.json", "w") as f:
        json.dump(results, f, indent=4)
