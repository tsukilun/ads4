from collections import deque

from edge import Edge
from vertex import Vertex


class Graph:
    """Graph represented by an adjacency list."""

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.vertices: dict[int, Vertex] = {}
        self.adjacency_list: dict[int, list[int]] = {}
        self.edges: list[Edge] = []

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.id] = vertex
        self.adjacency_list.setdefault(vertex.id, [])

    def add_edge(self, from_id: int, to_id: int) -> None:
        if from_id not in self.vertices or to_id not in self.vertices:
            raise ValueError("Both vertices must exist before adding an edge.")

        self.adjacency_list[from_id].append(to_id)
        self.edges.append(Edge(self.vertices[from_id], self.vertices[to_id]))

        if not self.directed:
            self.adjacency_list[to_id].append(from_id)
            self.edges.append(Edge(self.vertices[to_id], self.vertices[from_id]))

    def print_graph(self, limit: int | None = None) -> str:
        lines = []
        vertex_ids = sorted(self.adjacency_list)
        if limit is not None:
            vertex_ids = vertex_ids[:limit]

        for vertex_id in vertex_ids:
            neighbors = ", ".join(str(self.vertices[n]) for n in self.adjacency_list[vertex_id])
            lines.append(f"{self.vertices[vertex_id]}: [{neighbors}]")

        if limit is not None and len(self.adjacency_list) > limit:
            lines.append(f"... {len(self.adjacency_list) - limit} more vertices")

        return "\n".join(lines)

    def bfs(self, start_id: int) -> list[int]:
        if start_id not in self.vertices:
            raise ValueError("Start vertex does not exist.")

        visited = {start_id}
        order = []
        queue = deque([start_id])

        # BFS explores vertices level by level using a queue.
        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start_id: int) -> list[int]:
        if start_id not in self.vertices:
            raise ValueError("Start vertex does not exist.")

        visited = set()
        order = []

        # DFS goes as deep as possible before backtracking.
        def visit(vertex_id: int) -> None:
            visited.add(vertex_id)
            order.append(vertex_id)

            for neighbor in self.adjacency_list[vertex_id]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start_id)
        return order
