#!/bin/bash

SCRIPT_PATH="/Users/thomasbrickhouse/Desktop/cs/cs412/412project/approx_solution/cs412_tsp_approx.py"

test_cases=("test_graph1" "test_graph2" "test_graph3" "test_graph4" "test_graph5" "test_graph6" "test_graph7" "test_graph8" "test_graph9" "test_graph10")
# 1 : 3 Vertex Graph
# 2 : 8 Vertex Graph
# 3 : 10 Vertex Graph
# 4 : 12 Vertex Graph
# 5 : 15 Vertex Graph
# 6 : 18 Vertex Graph
# 7 : 20 Vertex Graph
# 8 : 100 Vertex Graph
# 9 : 500 Vertex Graph
# 10 : 1000 Vertex Graph

for test_case in "${test_cases[@]}"; do
    echo "Running test case: $test_case"
    python3 "$SCRIPT_PATH" < "$test_case"
    echo "-----------------------"
done
