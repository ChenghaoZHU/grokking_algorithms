def find_shortest_path(src, des):
    step = 0
    check_list = graph.get(src, [])
    while check_list:
        step += 1
        new_targets = []
        for node in check_list:
            if node == des:
                return step
            new_targets.extend(graph.get(node, []))
        check_list = new_targets
    return 0


if __name__ == '__main__':
    graph = {
        'cab': ['cat', 'car'],
        'cat': ['mat', 'bat'],
        'car': ['cat', 'bar'],
        'bar': ['bat'],
        'mat': ['bat']
    }
    print(find_shortest_path('cab', 'bat'))
    print(find_shortest_path('n', 'b'))
    print(find_shortest_path('cab', 'test'))
    print(find_shortest_path('cat', 'bat'))
    print(find_shortest_path('bat', 'cat'))
    print(find_shortest_path('cab', 'mat'))
    print(find_shortest_path('cat', 'car'))
