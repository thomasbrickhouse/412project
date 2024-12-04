import random


def generate_complete_graph(num_vertices, weight_range=(1.0, 100.0)):
    file_name = "graph"  # Always use the same file name
    vertices = [chr(97 + i) if i < 26 else f"v{i}" for i in range(num_vertices)]

    with open(file_name, "w") as file:
        num_edges = num_vertices * (num_vertices - 1) // 2
        file.write(f"{num_vertices} {num_edges}\n")

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                u, v = vertices[i], vertices[j]
                weight = round(random.uniform(*weight_range), 1)
                file.write(f"{u} {v} {weight}\n")
