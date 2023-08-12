# [1,2,3,5,4]

# lst = [1, 2, 1, 2]

lst = [1, 3, 4, 5, 1, 10, 7]


def check_increasing_order(lst):
    count = 0
    res_list = []
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            if lst[i] not in res_list:
                res_list.append(lst[i])
            else:
                count += 1
        else:
            count += 1
    if count > 1:
        return False
    else:
        return True


print(check_increasing_order(lst))
