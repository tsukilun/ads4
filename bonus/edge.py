from vertex import Vertex


class Edge:
    """Represents a weighted edge between two vertices."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int):
        if weight < 0:
            raise ValueError("Dijkstra's algorithm does not support negative weights.")

        self._source = source
        self._destination = destination
        self._weight = weight

    @property
    def source(self) -> Vertex:
        return self._source

    @property
    def destination(self) -> Vertex:
        return self._destination

    @property
    def weight(self) -> int:
        return self._weight

    def __str__(self) -> str:
        return f"{self._source} -> {self._destination} (weight: {self._weight})"
