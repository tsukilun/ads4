from edge import Edge
from vertex import Vertex


class WeightedGraph:
    """Weighted graph stored as an adjacency list."""

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.vertices: dict[int, Vertex] = {}
        self.adjacency_list: dict[int, list[tuple[int, int]]] = {}
        self.edges: list[Edge] = []

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.id] = vertex
        self.adjacency_list.setdefault(vertex.id, [])

    def add_edge(self, from_id: int, to_id: int, weight: int) -> None:
        if from_id not in self.vertices or to_id not in self.vertices:
            raise ValueError("Both vertices must exist before adding an edge.")

        self.adjacency_list[from_id].append((to_id, weight))
        self.edges.append(Edge(self.vertices[from_id], self.vertices[to_id], weight))

        if not self.directed:
            self.adjacency_list[to_id].append((from_id, weight))
            self.edges.append(Edge(self.vertices[to_id], self.vertices[from_id], weight))

    def print_graph(self) -> str:
        lines = []
        for vertex_id in sorted(self.adjacency_list):
            neighbors = ", ".join(
                f"{self.vertices[neighbor]}({weight})"
                for neighbor, weight in self.adjacency_list[vertex_id]
            )
            lines.append(f"{self.vertices[vertex_id]}: [{neighbors}]")
        return "\n".join(lines)

    def dijkstra(self, start_id: int) -> tuple[dict[int, float], dict[int, int | None]]:
        if start_id not in self.vertices:
            raise ValueError("Start vertex does not exist.")

        distances = {vertex_id: float("inf") for vertex_id in self.vertices}
        previous = {vertex_id: None for vertex_id in self.vertices}
        visited: set[int] = set()
        distances[start_id] = 0

        # Simple Dijkstra: repeatedly choose the unvisited vertex
        # with the smallest known distance.
        while len(visited) < len(self.vertices):
            current = self._closest_unvisited_vertex(distances, visited)
            if current is None:
                break

            visited.add(current)

            for neighbor, weight in self.adjacency_list[current]:
                if neighbor in visited:
                    continue

                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current

        return distances, previous

    def _closest_unvisited_vertex(
        self,
        distances: dict[int, float],
        visited: set[int],
    ) -> int | None:
        closest = None
        closest_distance = float("inf")

        for vertex_id, distance in distances.items():
            if vertex_id not in visited and distance < closest_distance:
                closest = vertex_id
                closest_distance = distance

        return closest

    def shortest_path(self, start_id: int, end_id: int, previous: dict[int, int | None]) -> list[int]:
        path = []
        current = end_id

        while current is not None:
            path.append(current)
            if current == start_id:
                break
            current = previous[current]

        path.reverse()
        return path if path and path[0] == start_id else []
