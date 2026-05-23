from vertex import Vertex
from weighted_graph import WeightedGraph


def format_distance(distance: float) -> str:
    return "unreachable" if distance == float("inf") else str(int(distance))


def format_path(path: list[int]) -> str:
    return "no path" if not path else " -> ".join(f"V{vertex_id}" for vertex_id in path)


def build_sample_graph() -> WeightedGraph:
    graph = WeightedGraph(directed=False)
    for vertex_id in range(6):
        graph.add_vertex(Vertex(vertex_id))

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 8)
    graph.add_edge(2, 4, 10)
    graph.add_edge(3, 4, 2)
    graph.add_edge(3, 5, 6)
    graph.add_edge(4, 5, 3)

    return graph


def main() -> None:
    start_id = 0
    graph = build_sample_graph()
    distances, previous = graph.dijkstra(start_id)

    print("Bonus Task: Dijkstra's Algorithm")
    print("=" * 39)
    print()

    print("Weighted Graph")
    print(graph.print_graph())
    print()

    print(f"Shortest paths from V{start_id}")
    print("Vertex | Distance | Path")
    print("-------|----------|----------------")
    for vertex_id in sorted(graph.vertices):
        path = graph.shortest_path(start_id, vertex_id, previous)
        print(
            f"V{vertex_id:<5} | {format_distance(distances[vertex_id]):<8} | "
            f"{format_path(path)}"
        )


if __name__ == "__main__":
    main()
