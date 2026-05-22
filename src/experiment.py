from time import perf_counter_ns

from graph import Graph
from vertex import Vertex


class Experiment:
    """Builds test graphs, runs traversals, and stores timing results."""

    def __init__(self):
        self.results: list[dict[str, int | list[int]]] = []

    def create_graph(self, size: int) -> Graph:
        graph = Graph(directed=False)
        for vertex_id in range(size):
            graph.add_vertex(Vertex(vertex_id))

        for vertex_id in range(size - 1):
            graph.add_edge(vertex_id, vertex_id + 1)

        for vertex_id in range(0, size - 3, 3):
            graph.add_edge(vertex_id, vertex_id + 3)

        for vertex_id in range(0, size - 5, 5):
            graph.add_edge(vertex_id, vertex_id + 5)

        return graph

    def run_traversals(self, graph: Graph, start_id: int = 0) -> dict[str, int | list[int]]:
        start = perf_counter_ns()
        bfs_order = graph.bfs(start_id)
        bfs_time = perf_counter_ns() - start

        start = perf_counter_ns()
        dfs_order = graph.dfs(start_id)
        dfs_time = perf_counter_ns() - start

        return {
            "vertices": len(graph.vertices),
            "edges": len(graph.edges),
            "bfs_time_ns": bfs_time,
            "dfs_time_ns": dfs_time,
            "bfs_order": bfs_order,
            "dfs_order": dfs_order,
        }

    def run_multiple_tests(self) -> None:
        self.results = []
        for size in (10, 30, 100):
            graph = self.create_graph(size)
            self.results.append(self.run_traversals(graph))

    def print_results(self) -> str:
        lines = [
            "Performance Results",
            "Size | Edges | BFS Time (ns) | DFS Time (ns)",
            "-----|-------|---------------|--------------",
        ]

        for result in self.results:
            lines.append(
                f"{result['vertices']:>4} | {result['edges']:>5} | "
                f"{result['bfs_time_ns']:>13} | {result['dfs_time_ns']:>12}"
            )

        return "\n".join(lines)
