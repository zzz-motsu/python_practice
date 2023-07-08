s = 'fdsfgdohjsdkfmisjgryhoiedrjhi'

d = {}
for c in s:
    if c not in d:
        print(c)
        d[c] = 0
    d[c] += 1

print(d)
print(c)