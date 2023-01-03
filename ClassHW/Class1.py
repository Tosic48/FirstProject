#Fibanachi
n = 8
lst = [1, 1]
i = 0
t = 1
if n > 0:
    while len(lst) < n:
        g = lst[i] + lst[t]
        lst.append(g)
        i = i + 1
        t = t + 1
    print(*lst)
else:
    print('Вводится натуральное положительное число')