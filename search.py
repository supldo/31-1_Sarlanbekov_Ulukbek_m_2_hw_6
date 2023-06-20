def binary_search(val, num):
    pos = 0
    n = len(num)
    result_ok = False
    first = 0
    last = n - 1

    while True:
        if first <= last:
            middle = (first + last) // 2
            if val == num[middle]:
                result_ok = True
                first = middle
                last = first - 1
                pos = middle
            else:
                if val > num[middle]:
                    first = middle + 1
                else:
                    last = middle - 1
        else:
            if result_ok == True:
                print(f'Элемент найден по индексу {pos}')
            else:
                print('Элемент не найден')
            break