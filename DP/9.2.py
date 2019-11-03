from collections import namedtuple, defaultdict


def dynamic_programming(items, steps):
    """
    :param items: item list
    :param steps: weight steps
    :returns: max value combo
    """
    value_table = defaultdict(dict)
    for i, item in enumerate(items):
        for weight_limit in steps:
            weight_limit += 1
            combo = []
            if weight_limit < item.weight:
                value = 0
            else:
                value = item.value
                combo.append(item)
            try:
                max_value = value + value_table[i-1][weight_limit - item.weight][0]
                combo.extend(value_table[i-1][weight_limit - item.weight][1])
            except KeyError:
                max_value = value
            try:
                old_max_value = value_table[i-1][weight_limit][0]
                old_combo = value_table[i-1][weight_limit][1]
            except KeyError:
                old_max_value = 0
                old_combo = []
            if max_value >= old_max_value:
                value_table[i][weight_limit] = (max_value, combo)
            else:
                value_table[i][weight_limit] = (old_max_value, old_combo)
    return value_table[len(items)-1][len(steps)]


if __name__ == '__main__':
    Item = namedtuple('Item', 'name weight value')
    items = [
        Item('water', 3, 10),
        Item('book', 1, 3),
        Item('food', 2, 9),
        Item('jacket', 2, 5),
        Item('camera', 1, 6)
    ]
    steps = range(6)
    print(dynamic_programming(items, steps))
