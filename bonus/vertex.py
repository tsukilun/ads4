class Vertex:
    """Represents a graph vertex with a unique integer id."""

    def __init__(self, vertex_id: int):
        self._id = vertex_id

    @property
    def id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"V{self._id}"

    def __repr__(self) -> str:
        return str(self)
