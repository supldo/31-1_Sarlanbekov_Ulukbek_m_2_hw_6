def bubble_sort(num):
    l = len(num) - 1
    for i in range(0, l):
        for j in range(0, l - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num