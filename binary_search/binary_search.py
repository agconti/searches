# https://youtu.be/wNVCJj642n4?list=PLAB1DA9F452D9466C


def binary_search(items, target):
    low = 0
    high = len(items)

    while (low + 1 < high):
        middle = (low + high) // 2

        if target < items[middle]:
            high = middle
        else:
            low = middle

    if items[low] == target:
        return low
    raise ValueError("{} was not found in the list".format(target))
