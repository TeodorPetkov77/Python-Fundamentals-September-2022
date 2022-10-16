# REMOVES IMBEDDED LISTS:


def remove_list(a_list):
    for index, item in enumerate(a_list):
        if isinstance(item, list):
            removed_item = a_list.pop(index)
            for index1 in range(len(removed_item), 0, -1):
                item_to_add = removed_item[index1 - 1]
                a_list.insert(index, item_to_add)
    return a_list
