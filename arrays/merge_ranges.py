# INPUT - list of tuple of integers (start_time, finish_time),
# each of them represents the number of 30-min blocks past 9:00am.
# OUTPUT - list of condensed ranges

time_ranges: list[tuple] = [(1, 10), (2, 6), (3, 5), (7, 9)]


def merge_ranges(ranges: list) -> list[tuple]:
    """
    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    """

    ranges = sorted(ranges)
    result: list = [ranges[0]]

    for n in range(1, len(ranges)):
        if ranges[n][0] <= result[-1][1]:
            result.append((result[-1][0], max(ranges[n][1], result[-1][1])))
            result.pop(-2)
        else:
            result.append(ranges[n])

    return result


if __name__ == '__main__':
    print(merge_ranges(time_ranges))
