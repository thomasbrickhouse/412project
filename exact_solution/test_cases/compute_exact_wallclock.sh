#!/bin/bash

echo "Running exact TSP wallclock benchmark..."

# Path to the Python wallclock script
PYTHON_SCRIPT="/Users/tannerkarol/cs374/ChefsProject/412project/exact_solution/wallclock.py"

# Output file
OUTPUT_FILE="benchmark_results_exact.json"

# Run the Python script
python3 "$PYTHON_SCRIPT"

# Check if the output file was created
if [ -f "$OUTPUT_FILE" ]; then
    echo "Results saved to $OUTPUT_FILE"
else
    echo "Benchmarking failed"
    exit 1
fi
