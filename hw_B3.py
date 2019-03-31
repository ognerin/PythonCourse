s = int(input())
t = int(input())
d = 0
for nucl in range(len(s)):
    if s[nucl] != t[nucl]:
        d += 1
print(d)







