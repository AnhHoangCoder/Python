#BFS tra ve khoach cach ngan nhat

from collections import deque

def bfs_distance(graph, start):
    distance = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance

g = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

print(bfs_distance(g, 1))
print(bfs_distance(g, 4))
