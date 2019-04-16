def simple_numbers(n):
    lst=[]
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
            yield i
for curr in simple_numbers(int(input())):
    print(curr, end = ' ')
