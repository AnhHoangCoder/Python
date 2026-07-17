#Collections.defaultdict: so do duoi dang danh sach Tuan

from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dict(graph)

print(build_graph([(1, 2), (1, 3), (2, 4)]))
print(build_graph([]))
