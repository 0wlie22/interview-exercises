# INPUT - two sorted lists
# OUTPUT - merged sorted list

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


def check_if_sorted(numbers: list) -> bool:
    if len(numbers) == 1 or len(numbers) == 0:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True


def merge_lists(list_a: list[int], list_b: list[int]):
    merged_list = [0] * (len(list_a) + len(list_b))

    index_a = len(list_a) - 1
    index_b = len(list_b) - 1
    end_list_a = False
    end_list_b = False
    index_merged_list = index_a + index_b + 1

    while index_merged_list >= 0:
        if not end_list_a and not end_list_b:
            if index_a >= 0 and list_a[index_a] >= list_b[index_b]:
                merged_list[index_merged_list] = list_a[index_a]
                index_a -= 1
                if index_a < 0:
                    end_list_a = True
            elif index_b >= 0 and list_a[index_a] <= list_b[index_b]:
                merged_list[index_merged_list] = list_b[index_b]
                index_b -= 1
                if index_b < 0:
                    end_list_b = True
        elif end_list_a:
            merged_list[index_merged_list] = list_b[index_b]
            index_b -= 1
        elif end_list_b:
            merged_list[index_merged_list] = list_a[index_a]
            index_a -= 1
        index_merged_list -= 1

    return merged_list


if __name__ == '__main__':
    if check_if_sorted(my_list) and check_if_sorted(alices_list):
        print(merge_lists(my_list, alices_list))
    else:
        print("Arrays are not sorted")
