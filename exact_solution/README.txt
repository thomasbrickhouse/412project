# Traveling Salesman Problem (TSP) Exact Solution

## Overview
This project implements an **exact** solution for the Traveling Salesman Problem (TSP) using a brute-force approach. The solution finds the shortest Hamiltonian cycle in a complete graph by exploring all possible paths.

## Requirements
* **Python**: Version 3.8 or later

## Usage

### 1. Run Test Cases
To run the predefined test cases:
./run_test_cases.sh


### 2. Run With Your Own Graph
Create a graph input file in the following format:
<number_of_vertices> <number_of_edges> <node1> <node2> <weight> <node1> <node3> <weight> ...


#### Example Input File:
4 6 a b 10.0 a c 15.0 a d 20.0 b c 35.0 b d 25.0 c d 30.0

Run the Code:

python tsp_exact.py <your_file_here>


### 3. Output Format
The output consists of:
1. The total cost of the shortest path (rounded to 4 decimal places).
2. The list of nodes representing the shortest Hamiltonian cycle.

#### Example Output:
80.0000 a b d c a
