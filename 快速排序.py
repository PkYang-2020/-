num = [[1,4],[0,2],[3,5]]
def quick_sort(num):
    if len(num) < 2:
        return
    p = num[0][0]
    L = []
    M = []
    R = []
    while len(num) > 0:
        if p > num[-1][0]:
            L.append(num.pop())
        elif p == num[-1][0]:
            M.append(num.pop())
        else:
            R.append(num.pop())
    quick_sort(L)
    quick_sort(R)
    num.extend(L)
    num.extend(M)
    num.extend(R)
    return num
quick_sort(num)#分治法

