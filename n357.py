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

_max = 0
_m = 0
s1 = 0
s2 = 0
for i in range(len(_l)):
    for j in range(len(_l[i])):
        _m = _l[i][j]
        if _m > _max:
            _max = _m
            s1 = i
            s2 = j

print(_max)
print(f"{s1} {s2}")