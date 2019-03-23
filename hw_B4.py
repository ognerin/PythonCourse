import random
a = random.randint(0,100)
n = int(input())
t = 0
while n != a:
    if t == 3 and a != 100:
        x = a // 10
        print("даю подсказку, ваше число находится в этом десятке " + str(x))
    elif t == 3:
        print("а вы думали, будет просто?") 
    
    if t == 7:
        print("терпение лопнуло, вы в " + str(abs(n - a)) + " шагах от верного ответа")  
        break 
    
    if n > a:
        print("ваше число слишком большое")
        n = int(input())
        t += 1
    elif n < a:
        print("ваше число слишком маленькое")
        n = int(input())
        t += 1
n = int(input())
while n != a:
    if n > a:
        print("нет")
        n = int(input())
    elif n < a:
        print("нет")
        n = int(input())
print("да, вы угадали, число " + str(n) + ", мое увожение")
