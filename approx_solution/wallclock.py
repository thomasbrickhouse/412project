import time
import json
import os
from cs412_tsp_exact import tsp_exact, parse_input
from cs412_tsp_approx import tsp_approx


def load_graph(file_name):
    with open(file_name, "r") as f:
        line = f.readline()
        v = int(line.split()[0])
        graph = line + f.read()
    return parse_input(graph), v


def benchmark(test_case, max_vertices_for_exact=15):
    graph, num_vertices = load_graph(test_case)

    # Skip exact solution for graphs with too many vertices (more than 15 by default)
    if num_vertices >= max_vertices_for_exact:
        exact_runtime = None
        exact_cost = None
    else:
        start_time = time.time()
        path, exact_cost = tsp_exact(graph)
        exact_runtime = time.time() - start_time

    start_time = time.time()
    approx_path, approx_cost = tsp_approx(graph, timeout=100, single_iteration=True)
    approx_runtime = time.time() - start_time

    print(f"Test case complete: {test_case}")

    return {
        "test_case": os.path.basename(test_case),
        "num_vertices": num_vertices,
        "exact_cost": exact_cost,
        "approx_cost": approx_cost,
        "exact_runtime": exact_runtime,
        "approx_runtime": approx_runtime,
    }


if __name__ == "__main__":
    test_cases = [
        "test_graph1",
        "test_graph2",
        "test_graph3",
        "test_graph4",
        "test_graph5",
        "test_graph6",
        "test_graph7",
        "test_graph8",
        "test_graph9",
        "test_graph10",
    ]
    results = []

    for test_case in test_cases:
        result = benchmark(test_case)
        results.append(result)

    # json file for graoh building
    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=4)
