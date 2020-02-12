# Alex Bello
# 2/11/2020
# The list of methods used for the Operation project.


def sums(lists):
    sum = 0
    for i in lists:
        sum += i
    return sum


def product(lists):
    total = 0
    for i in lists:
        total *= i
    return total


def mean(lists):
    avg = sums(lists)
    return avg / len(lists)


def median(lists):
    mid = (len(lists) - 1) // 2
    if mid % 2 == 1:
        mid = lists[mid] + lists[mid + 1] / 2
    else:
        mid = lists[mid]
    return mid


def mode(lists):
    mode = []
    count = 0
    for i in range(len(lists)):
        temp_count = 1
        for j in range(1, len(lists)):
            if lists[i] == lists[j]:
                temp_count += 1
        if temp_count > count:
            mode.clear()
            count = temp_count
        if temp_count >= count:
            mode.append(lists[i])
    return set(mode)


def big_boi(lists):
    large = lists[0]
    for i in lists:
        if large < i:
            large = i
    return large


def small_boi(lists):
    little = lists[0]
    for i in lists:
        if little > i:
            little = i
    return little


def removal(lists):
    return list(set(lists))


def odd_times(lists):
    return [odd for odd in lists if odd % 2 == 1]


def even_times(lists):
    return [even for even in lists if even % 2 == 0]


def tell_me(lists):
    new_num = int(input("Give me a number boyo! "))
    for i in lists:
        if i == new_num:
            return True
    return False


def bonus(lists):
    return lists[-2]
