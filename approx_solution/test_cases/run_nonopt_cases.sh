SCRIPT_PATH="/Users/thomasbrickhouse/Desktop/cs/cs412/412project/approx_solution/cs412_tsp_approx.py"

test_cases=("test_graph10")
# 10 : 1000 Vertex Graph

# It is not possible to run one specific test case and guarantee that the result will be optimal 
# or not. My approximation method starts at a random vertex and then performs a greedy traversal.
# Because of this random start, that traversal may or may not be optimal. That is why I repeadetly
# run the algorithm on the same test case for a specified amount of time to see if the result can 
# be improved. Sometimes the result is optimal, sometimes it is not. Check presentation graphs for
# examples of this behavior.

for test_case in "${test_cases[@]}"; do
    echo "Running test case: $test_case"
    python3 "$SCRIPT_PATH" < "$test_case"
    echo "-----------------------"
done