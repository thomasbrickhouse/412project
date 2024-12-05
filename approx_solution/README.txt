# Traveling Salesman Problem (TSP) Approximation Solution

## Overview
This project implements an **approximate**  solution for the Traveling Salesman Problem (TSP). The solution uses a greedy algorithm with repeated iterations

## Requierments
*Python:* Version 3.8 or later
matplotlib
```
pip install matplotlib
```

## Usage

1. Run Test Cases
```
./run_test_cases.sh
```

2. Run With Your Own Graph

Create a graph using this format:
```
<number_of_vertices> <number_of_edges>
<node1> <node2> <weight>
<node1> <node3> <weight>
...
```

Example:
```
3 3
a b 3.0
b c 4.2
a c 5.4
```

Run the Code:
```
python tsp_approx.py <your_file_here>
```




