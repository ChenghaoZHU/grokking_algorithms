from collections import defaultdict


def longest_common_substring(word_a, word_b):
    """
    :param word_a: word A
    :param word_b: word B
    :returns: longest common substring of A and B
    """
    value_table = defaultdict(dict)
    best = None  # corodinates of last character of longest substring
    best_v = -1  # length of longest substring
    for i, a in enumerate(word_a):
        for j, b in enumerate(word_b):
            v = 1 if a == b else 0
            try:
                if v:
                    v = v + value_table[i-1][j-1]  # their last character is the same if no keyerror
            except KeyError:
                pass
            value_table[i][j] = v
            if v > best_v:  # record current best result
                best_v = v
                best = (i, j)

    longest_common_str = ''
    x, y = best
    while x >= 0 and y >= 0:  # loop to find the subtring
        v = value_table[x][y]
        if v:
            longest_common_str += word_a[x]
        else:
            break
        x -= 1
        y -= 1
    return longest_common_str[::-1]


if __name__ == '__main__':
    print(longest_common_substring('fish', 'hish'))
    print(longest_common_substring('fort', 'fosh'))
    print(longest_common_substring('fish', 'fort'))
    print(longest_common_substring('blue', 'clues'))
