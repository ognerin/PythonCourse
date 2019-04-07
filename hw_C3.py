n = str(input())
a = n.split()
k = 0
for i in range(len(a)):
    if i == 0:
        k = len(a[i])
    elif len(a[i]) < k:
        k = len(a[i])
print(k)
