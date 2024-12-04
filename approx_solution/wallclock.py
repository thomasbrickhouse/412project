import time
import json
import os
from multiprocessing import Process, Queue
from cs412_tsp_exact import tsp_exact, parse_input
from cs412_tsp_approx import tsp_approx


def load_test_graph(file_name):
    """Load a graph from a file."""
    with open(file_name, "r") as f:
        return parse_input(f.read())


def run_function(func, args, result_queue):
    """Wrapper function to run in a separate process."""
    result_queue.put(func(*args))


def run_with_timeout(func, args=(), timeout=10):
    """Runs a function with a timeout."""
    result_queue = Queue()
    process = Process(target=run_function, args=(func, args, result_queue))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError("Function exceeded timeout limit.")

    return result_queue.get()


def benchmark(test_case_path, timeout=10.0):
    """Run benchmarks for both exact and approx solutions."""
    graph = load_test_graph(test_case_path)

    # Try exact solution with a timeout
    exact_cost = None
    exact_runtime = None
    try:
        start_time = time.time()
        exact_path, exact_cost = run_with_timeout(
            tsp_exact, args=(graph,), timeout=timeout
        )
        exact_runtime = time.time() - start_time
    except TimeoutError:
        exact_runtime = "Timeout"

    # Measure approximation solution
    start_time = time.time()
    approx_path, approx_cost = tsp_approx(
        graph, timeout=100.0, single_iteration=True
    )  # 1-second timeout for approx
    approx_runtime = time.time() - start_time

    return {
        "test_case": os.path.basename(test_case_path),
        "exact_cost": exact_cost,
        "approx_cost": approx_cost,
        "exact_runtime": exact_runtime,
        "approx_runtime": approx_runtime,
    }


if __name__ == "__main__":
    results = []
    test_cases_folder = "test_cases"
    test_cases = [
        os.path.join(test_cases_folder, f"test_graph{i}") for i in range(1, 11)
    ]
    timeout_limit = 1  # Set a timeout limit for the exact solution

    for test_case in test_cases:
        print(f"Running benchmarks for {test_case}...")
        result = benchmark(test_case, timeout=timeout_limit)
        results.append(result)

    # Save results to a JSON file
    output_file = "benchmark_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")
