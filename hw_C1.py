n = [2,5,7,7,0,3,3,9,0]
a = 0
for i in range(len(n)):
    if i == 0:
        a = n[i]
    elif n[i] > a:
        print(n[i], end = " ")
        a = n[i]
    else:
        a = n[i]
