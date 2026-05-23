# Bonus Task: Dijkstra's Algorithm

This folder contains a separate Python implementation of the bonus task.

## What It Does

The program extends the graph idea to weighted edges and implements Dijkstra's algorithm to find the shortest distance from one starting vertex to all other vertices.

The implementation uses:

- Weighted adjacency list
- `Vertex` class
- `Edge` class with a `weight` field
- `WeightedGraph` class
- Simple-loop Dijkstra implementation without a priority queue

## How to Run

```bash
python bonus/main.py
```

## Example Output

```text
Bonus Task: Dijkstra's Algorithm
=======================================

Weighted Graph
V0: [V1(4), V2(2)]
V1: [V0(4), V2(1), V3(5)]
V2: [V0(2), V1(1), V3(8), V4(10)]
V3: [V1(5), V2(8), V4(2), V5(6)]
V4: [V2(10), V3(2), V5(3)]
V5: [V3(6), V4(3)]

Shortest paths from V0
Vertex | Distance | Path
-------|----------|----------------
V0     | 0        | V0
V1     | 3        | V0 -> V2 -> V1
V2     | 2        | V0 -> V2
V3     | 8        | V0 -> V2 -> V1 -> V3
V4     | 10       | V0 -> V2 -> V1 -> V3 -> V4
V5     | 13       | V0 -> V2 -> V1 -> V3 -> V4 -> V5
```
