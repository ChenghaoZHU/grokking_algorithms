def get_next_node(costs, processed_nodes):
    """
    :param costs: cost list of nodes
    :param processed_nodes: nodes proccessed
    :returns: node with lowest cost which has not been processed
    """
    node_num = len(costs)
    while len(processed_nodes) < node_num:
        min_cost = float('inf')
        min_node = None
        for node, cost in costs.items():
            if node in processed_nodes:
                continue
            if cost <= min_cost:
                min_cost = cost
                min_node = node
        yield min_node


def dijkstra_algorithm(graph, src, des):
    """
    :param graph: input graph
    :param src: source point
    :param des: destination
    :returns: shortest path and shortest distance
    """
    # initialization
    costs = {}
    parents = {}
    for node in graph.keys():
        if node == src:
            continue  # 不处理自己
        costs[node] = float('inf')
        parents[node] = None
    for node, cost in graph[src].items():
        costs[node] = cost
        parents[node] = src

    processed_node_list = []
    for node in get_next_node(costs, processed_node_list):
        for neighbor, cost in graph[node].items():
            new_cost = cost + costs[node]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed_node_list.append(node)

    shortest_path = []
    current_node = des  # point
    while current_node in parents:
        shortest_path.append(current_node)
        current_node = parents[current_node]
    shortest_path.append(src)

    return shortest_path[::-1], costs[des]


if __name__ == '__main__':
    # test A
    graph1 = {
        '1': {'2': 5, '3': 2},
        '2': {'5': 4, '4': 2},
        '3': {'2': 8, '4': 7},
        '4': {'6': 1},
        '5': {'4': 6, '6': 3},
        '6': {}
    }
    src1 = '1'
    des1 = '6'
    print(dijkstra_algorithm(graph1, src1, des1))

    # test B
    # happen to solve, dijkstra is not applied to cyclic gragh
    graph2 = {
        'a': {'b': 10},
        'b': {'d': 20},
        'c': {'b': 1},
        'd': {'e': 30, 'c': 1},
        'e': {},
    }
    src2 = 'a'
    des2 = 'e'
    print(dijkstra_algorithm(graph2, src2, des2))

    # test C
    # happen to solve, dijkstra cannot handle negative weighted graph
    graph3 = {
        'a': {'b': 2, 'c': 2},
        'b': {'c': 2},
        'c': {'e': 2, 'd': 2},
        'd': {'e': 2, 'b': -1},
        'e': {},
    }
    src3 = 'a'
    des3 = 'e'
    print(dijkstra_algorithm(graph3, src3, des3))
