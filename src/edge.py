from vertex import Vertex


class Edge:
    """Represents a directed edge between two vertices."""

    def __init__(self, source: Vertex, destination: Vertex):
        self._source = source
        self._destination = destination

    @property
    def source(self) -> Vertex:
        return self._source

    @property
    def destination(self) -> Vertex:
        return self._destination

    def __str__(self) -> str:
        return f"{self._source} -> {self._destination}"
