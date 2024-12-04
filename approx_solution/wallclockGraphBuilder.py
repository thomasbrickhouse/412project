import json
import matplotlib.pyplot as plt

# Load benchmark results
with open("benchmark_results.json", "r") as f:
    results = json.load(f)


# Extract the number of vertices from test case filenames (e.g., test_graph1 -> 1)
def extract_num_vertices(test_case_name):
    # Extract the number at the end of 'test_graphX'
    return int(test_case_name.replace("test_graph", ""))


# Parse results
vertex_sizes = [extract_num_vertices(r["test_case"]) for r in results]
exact_runtimes = [
    r["exact_runtime"] if r["exact_runtime"] != "Timeout" else None for r in results
]
approx_runtimes = [r["approx_runtime"] for r in results]
exact_costs = [
    r["exact_cost"] if r["exact_cost"] is not None else None for r in results
]
approx_costs = [r["approx_cost"] for r in results]

# Runtime Comparison Plot
plt.figure(figsize=(8, 6))
plt.plot(
    vertex_sizes,
    exact_runtimes,
    label="Exact Runtime",
    marker="o",
    linestyle="--",
    alpha=0.7,
)
plt.plot(vertex_sizes, approx_runtimes, label="Approx Runtime", marker="o")
plt.xlabel("Number of Test Cases (by test_graphX)")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Comparison: Exact vs Approximation")
plt.legend()
plt.grid(True)
plt.show()

# Solution Value Comparison Plot
plt.figure(figsize=(8, 6))
plt.plot(
    vertex_sizes, exact_costs, label="Exact Cost", marker="o", linestyle="--", alpha=0.7
)
plt.plot(vertex_sizes, approx_costs, label="Approx Cost", marker="o")
plt.xlabel("Number of Test Cases (by test_graphX)")
plt.ylabel("Solution Cost")
plt.title("Solution Value Comparison: Exact vs Approximation")
plt.legend()
plt.grid(True)
plt.show()
