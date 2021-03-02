rains = eval(input())
res = []
full_lake = []
def test(rains):
    for i in range(len(rains)):
        if rains[i] != 0:
            if rains[i] in full_lake:
                return []
            full_lake.append(rains[i])
            res.append(-1)
        else:
            if full_lake == []:
                res.append(1)
            else:
                if i != len(rains)-1:
                    if len(full_lake) != 0:
                        if full_lake.count(rains[i+1]) == 1:
                            t = full_lake.index(rains[i+1])
                            full_lake.pop(t)
                            res.append(rains[i+1])
                        else:
                            full_lake.pop(0)
                            res.append(rains[0])
    return res
print(test(rains))