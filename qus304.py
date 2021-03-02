matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

n1 = (2,1)
n2 = (4,3)
res = 0
for i in range(n1[0],n2[0]+1):
    l = matrix[i]
    for j in range(n1[1],n2[1]+1):
        res += l[j]
print(res)
print(1)
