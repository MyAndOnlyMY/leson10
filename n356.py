n_m = list(map(int, input().split()))
n = int(n_m[0])
m = int(n_m[1])

_l = [0]*n
for i in range(n):
    _str = input()
    k = _str.split()
    _l[i] = [0]*m
    for j in range(m):
        _l[i][j] = int(k[j])

_sum = 0
_max = 0
s = 0
for i in range(len(_l)):
    for j in range(len(_l[i])):
        _sum += _l[i][j]
    if _sum > _max:
        _max = _sum
        s = i
    _sum = 0

print(_max)
print(s)