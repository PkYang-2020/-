w = [2,3,4,5]
v = [3,4,5,6]
def c(m,n):
    if m < 0 or n < 0:
        return 0
    if n < w[m]:
        return c(m-1,n)
    elif n >= w[m] and m >= 0:
        return  max(v[m] + c(m-1,n-w[m]),c(m-1,n))
print(c(3,9))