SCRIPT_PATH="/Users/thomasbrickhouse/Desktop/cs/cs412/412project/approx_solution/cs412_tsp_approx.py"

test_cases=("test_graph10")
# 10 : 1000 Vertex Graph

for test_case in "${test_cases[@]}"; do
    echo "Running test case: $test_case"
    python3 "$SCRIPT_PATH" < "$test_case"
    echo "-----------------------"
done