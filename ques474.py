t = eval(input())
m = int(input())
n = int(input())
l = len(t)
a = [t[i].count('0') for i in range(l)]
b = [t[i].count('1') for i in range(l)]
res = []
def c(o,p,q):
    if o < 0 or p < 0 or q < 0:
        return res
    elif p < a[o] or q < b[o]:
        return c(o-1,p,q)
    elif p >= a[o] and q >= b[o] and o >= 0:
        res.append(t[o])
        return c(o-1,p-a[o],q-b[o])
print(len(c(l-1,m,n)))
