import heapq
import requests

# Dijkstra's algorithm implementation
def dijkstra(start_node, end_node, graph):
    # graph is assumed to be a dictionary with node connections and their weights
    # example: graph = {'A': {'B': 4, 'C': 2}, 'B': {'A': 4, 'C': 5}, ...}
    
    # Shortest path dictionary and the priority queue
    shortest_paths = {start_node: (None, 0)}  # {node: (previous_node, distance)}
    priority_queue = [(0, start_node)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end_node:
            break

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, distance)
                heapq.heappush(priority_queue, (distance, neighbor))

    # Backtrack to find the shortest path
    path = []
    current_node = end_node
    while current_node != start_node:
        path.append(current_node)
        current_node = shortest_paths[current_node][0]
    path.append(start_node)
    path.reverse()

    return path, shortest_paths[end_node][1]  # path and total distance
