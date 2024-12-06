#!/bin/bash

# Path to your exact TSP solution script
SCRIPT_PATH="/Users/tannerkarol/cs374/ChefsProject/412project/exact_solution/cs412_tsp_exact.py"

# List of test case files
test_cases=("testCase1" "testCase2" "testCase3" "testCase4" "testCase5" "testCase6" "testCase7" "testCase8" "testCase9" "testCase10")
# Test case descriptions:
# 1 : 3 Vertex Graph
# 2 : 4 Vertex Graph
# 3 : 5 Vertex Graph
# 4 : 10 Vertex Graph
# 5 : 15 Vertex Graph
# 6 : 25 Vertex Graph
# 7 : 50 Vertex Graph
# 8 : 100 Vertex Graph
# 9 : 500 Vertex Graph
# 10 : 1000 Vertex Graph

# Iterate through each test case and run the Python script
for test_case in "${test_cases[@]}"; do
    echo "Running test case: $test_case"
    python3 "$SCRIPT_PATH" < "$test_case"
    echo "-----------------------"
done
