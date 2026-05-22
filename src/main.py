from experiment import Experiment


def format_order(order: list[int]) -> str:
    return " -> ".join(f"V{vertex_id}" for vertex_id in order)


def main() -> None:
    experiment = Experiment()

    small_graph = experiment.create_graph(10)
    small_result = experiment.run_traversals(small_graph)

    print("Graph Traversal and Representation System")
    print("=" * 49)
    print()

    print("Graph Structure Output (Small Graph)")
    print(small_graph.print_graph())
    print()

    print("BFS Traversal Output")
    print(format_order(small_result["bfs_order"]))
    print()

    print("DFS Traversal Output")
    print(format_order(small_result["dfs_order"]))
    print()

    experiment.run_multiple_tests()
    print(experiment.print_results())


if __name__ == "__main__":
    main()
