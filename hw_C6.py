s = int(input())
t = int(input())
loc = []
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        loc.append(i + 1)
for i in loc:
    print (i, end = " ")
