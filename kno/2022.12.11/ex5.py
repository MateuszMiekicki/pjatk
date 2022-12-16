from collections import defaultdict
import time


class Graph:
    def __init__(self):
        self.cities = defaultdict(list)
        self.distance = {}

    def add_city(self, from_node, to_node, km):
        self.cities[from_node].append(to_node)
        self.cities[to_node].append(from_node)
        self.distance[(from_node, to_node)] = km
        self.distance[(to_node, from_node)] = km


graph = Graph()

cities = [
    ('Elbląg', 'Gdańsk', 63),
    ('Elbląg', 'Tczew', 53),
    ('Tczew', 'Gdańsk', 33),
    ('Tczew', 'Elbląg', 53),
    ('Tczew', 'Kościerzyna', 59),
    ('Kościerzyna', 'Tczew', 59),
    ('Kościerzyna', 'Gdańsk', 58),
    ('Kościerzyna', 'Lębork', 58),
    ('Kościerzyna', 'Bytów', 40),
    ('Kościerzyna', 'Chojnice', 70),
    ('Chojnice', 'Kościerzyna', 70),
    ('Chojnice', 'Bytów', 65),
    ('Bytów', 'Kościerzyna', 40),
    ('Bytów', 'Chojnice', 65),
    ('Bytów', 'Słupsk', 70),
    ('Słupsk', 'Bytów', 70),
    ('Słupsk', 'Ustka', 21),
    ('Słupsk', 'Lębork', 55),
    ('Ustka', 'Słupsk', 21),
    ('Ustka', 'Łeba', 64),
    ('Łeba', 'Ustka', 64),
    ('Łeba', 'Lębork', 29),
    ('Łeba', 'Władysławowo', 66),
    ('Władysławowo', 'Łeba', 66),
    ('Władysławowo', 'Hel', 35),
    ('Władysławowo', 'Gdynia', 42),
    ('Lębork', 'Kościerzyna', 58),
    ('Lębork', 'Słupsk', 55),
    ('Lębork', 'Gdynia', 60),
    ('Lębork', 'Łeba', 29),
    ('Hel', 'Władysławowo', 35),
    ('Gdynia', 'Lębork', 60),
    ('Gdynia', 'Władysławowo', 42),
    ('Gdynia', 'Gdańsk', 24),
    ('Gdańsk', 'Gdynia', 24),
    ('Gdańsk', 'Kościerzyna', 58),
    ('Gdańsk', 'Elbląg', 63),
    ('Gdańsk', 'Tczew', 33),
]

for city in cities:
    graph.add_city(*city)


def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    distab = []
    while current_node != end:
        visited.add(current_node)
        destinations = graph.cities[current_node]
        dis_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            dis = graph.distance[(current_node, next_node)] + dis_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, dis)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > dis:
                    shortest_paths[next_node] = (current_node, dis)
                    if dis >= shortest_paths[current_node][1]:
                        distab.append(dis)
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

        if not next_destinations:
            return "Droga niemożliwa do znalezienia"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    print("Droga wynosi " + str(distab[-1]) + "km.")

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path


start = time.time()
print(dijsktra(graph, 'Gdańsk', 'Ustka'))
end = time.time()
print(str(end-start))
