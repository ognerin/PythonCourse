n = int(input())
if n == 1 or n == 2:
    print("1")
    quit()
k = 3
a = 1
b = 1
for i in range(n - 2):
    a, b = b, a * 3 + b
print(b)
