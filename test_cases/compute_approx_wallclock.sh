#!/bin/bash

# Paths to solutions and test cases
TEST_CASES_DIR="test_cases"
EXACT_SOL="exact_solution/cs412_tsp_exact.py"
APPROX_SOL="approx_solution/cs412_tsp_approx.py"

# Output files for results
EXACT_RESULTS="$TEST_CASES_DIR/exact_results.txt"
APPROX_RESULTS="$TEST_CASES_DIR/approx_results.txt"

# Cleanup old results
rm -f $EXACT_RESULTS $APPROX_RESULTS

# Loop through each test case
for TEST_FILE in $TEST_CASES_DIR/*.txt; do
  echo "Processing $TEST_FILE..."
  
  # Run the exact solution and record its cost and runtime
  /usr/bin/time -p python3 $EXACT_SOL $TEST_FILE > temp_output.txt 2> temp_time.txt
  EXACT_COST=$(cat temp_output.txt)  # Assuming the script outputs the cost
  EXACT_TIME=$(grep real temp_time.txt | awk '{print $2}')
  echo "$TEST_FILE $EXACT_COST $EXACT_TIME" >> $EXACT_RESULTS
  
  # Run the approximate solution and record its cost and runtime
  /usr/bin/time -p python3 $APPROX_SOL $TEST_FILE > temp_output.txt 2> temp_time.txt
  APPROX_COST=$(cat temp_output.txt)  # Assuming the script outputs the cost
  APPROX_TIME=$(grep real temp_time.txt | awk '{print $2}')
  echo "$TEST_FILE $APPROX_COST $APPROX_TIME" >> $APPROX_RESULTS
done

# Cleanup temporary files
rm -f temp_time.txt temp_output.txt
