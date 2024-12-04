import random
import sys


def generate_complete_graph(num_vertices, weight_range=(1.0, 100.0)):
    file_name = "test_graph5"
    vertices = [chr(97 + i) if i < 26 else f"v{i}" for i in range(num_vertices)]

    with open(file_name, "w") as file:
        num_edges = num_vertices * (num_vertices - 1) // 2
        file.write(f"{num_vertices} {num_edges}\n")

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                u, v = vertices[i], vertices[j]
                weight = round(random.uniform(*weight_range), 1)
                file.write(f"{u} {v} {weight}\n")


def parse_input(input_string):
    lines = input_string.strip().split("\n")
    num_nodes, num_edges = map(int, lines[0].split())
    graph = {}

    for line in lines[1:]:
        node1, node2, weight = line.split()
        weight = float(weight)
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    num_vertices = int(sys.argv[1])
    weight_range = (1.0, 100.0)

    if len(sys.argv) == 4:
        weight_range = (float(sys.argv[2]), float(sys.argv[3]))

    generate_complete_graph(num_vertices, weight_range)
