import heapq
from typing import Dict, List, Tuple, Any


def dijkstra(
        graph: Dict[Any, List[Tuple[Any, float]]],
        start: Any
) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """
    Finds the shortest paths from the start vertex to all other vertices in a weighted graph using Dijkstra's algorithm with a binary heap.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
               Keys are vertices, values are lists of tuples (neighbor, weight).
        start: The starting vertex.

    Returns:
        shortest_distances: A dictionary mapping each vertex to the shortest distance from the start vertex.
        previous_nodes: A dictionary mapping each vertex to its predecessor in the shortest path.
    """
    shortest_distances: Dict[Any, float] = {
        vertex: float('inf') for vertex in graph}
    previous_nodes: Dict[Any, Any] = {vertex: None for vertex in graph}
    shortest_distances[start] = 0

    heap: List[Tuple[float, Any]] = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Skip if we found a better path already
        if current_distance > shortest_distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # If a shorter path to neighbor is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return shortest_distances, previous_nodes


# Example usage:
if __name__ == "__main__":
    example_graph: Dict[str, List[Tuple[str, float]]] = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_vertex: str = 'A'
    distances, previous = dijkstra(example_graph, start_vertex)
    print("Shortest distances:", distances)
    print("Previous vertices:", previous)
