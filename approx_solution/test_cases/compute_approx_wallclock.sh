echo "Running script..."
python3 "/Users/thomasbrickhouse/Desktop/cs/cs412/412project/approx_solution/wallclock.py"

OUTPUT_FILE="benchmark_results.json"

if [ -f "$OUTPUT_FILE" ]; then
    echo "Results saved to $OUTPUT_FILE"
else
    echo "Failed"
    exit 1
fi
