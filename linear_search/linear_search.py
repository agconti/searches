# https://youtu.be/wNVCJj642n4?list=PLAB1DA9F452D9466C


def linear_search(items, target):
    for position, item in enumerate(items):
        if item == target:
            return position

    raise ValueError("{} was not found in the list".format(target))
