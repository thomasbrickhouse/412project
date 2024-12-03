#!/bin/bash

# Define colors for output
RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"

echo -e "${BOLD}Running Test Cases:${NC}"
echo -e "\t${BOLD}Test Case\tResult\t\tRuntime${NC}"

# Python program to test
PYTHON_SCRIPT="exact_tsp_solution.py"

# Iterate through test case folders
for TEST_CASE_DIR in test_cases/test_case_*; do
    cd "$TEST_CASE_DIR"

    # Measure runtime
    start=$(python3 -c 'import time; print(time.time())')
    python3 ../../$PYTHON_SCRIPT < input.txt > output.txt
    end=$(python3 -c 'import time; print(time.time())')
    runtime=$(echo "$end - $start" | bc -l)

    # Compare output and expected output
    if diff -q output.txt expectedoutput.txt > /dev/null; then
        echo -e "\t$(basename $TEST_CASE_DIR)\t${GREEN}PASSED${NC}\t\t${BLUE}${runtime}s${NC}"
    else
        echo -e "\t$(basename $TEST_CASE_DIR)\t${RED}FAILED${NC}\t\t${BLUE}${runtime}s${NC}"
    fi

    cd - > /dev/null
done
