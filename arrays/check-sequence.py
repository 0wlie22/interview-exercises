in_orders: list = [2, 4, 6]
out_orders: list = [1, 3, 5]
served_orders: list = [1, 2, 4, 6, 3, 5]


def if_first_come_first_served(out_orders: list, in_orders: list, servings: list) -> bool:
    in_index: int = 0
    out_index: int = 0
    for order in servings:
        if in_index < len(in_orders) - 1:
            if order == in_orders[in_index]:
                in_index += 1
        else:
            in_index += 1

        if out_index < len(out_orders) - 1:
            if order == out_orders[out_index]:
                out_index += 1
        else:
            out_index += 1
    print(in_index, out_index)
    if in_index == len(in_orders) and out_index == len(out_orders):
        return True
    return False


if __name__ == '__main__':
    if if_first_come_first_served(out_orders, in_orders, served_orders):
        print("true")
    else:
        print("false")
