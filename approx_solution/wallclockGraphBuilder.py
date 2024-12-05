import json
import matplotlib.pyplot as plt

# Load benchmark results
with open("benchmark_results.json", "r") as f:
    results = json.load(f)

# Extract data for plotting
test_cases = [r["test_case"] for r in results]  # Use test case names for the x-axis
exact_runtimes = [r["exact_runtime"] for r in results]
approx_runtimes = [r["approx_runtime"] for r in results]
exact_costs = [r["exact_cost"] for r in results]
approx_costs = [r["approx_cost"] for r in results]

# Runtime Comparison Plot
plt.figure(figsize=(8, 6))
plt.plot(test_cases, exact_runtimes, label="Exact Runtime", marker="o", linestyle="--")
plt.plot(test_cases, approx_runtimes, label="Approx Runtime", marker="o")
plt.xlabel("Graph")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Solution Value Comparison Plot
plt.figure(figsize=(8, 6))
plt.plot(test_cases, exact_costs, label="Exact Cost", marker="o", linestyle="--")
plt.plot(test_cases, approx_costs, label="Approx Cost", marker="o")
plt.xlabel("Graph")
plt.ylabel("Solution Cost")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
