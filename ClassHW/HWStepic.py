n = int(input())
i = 1
while i < n:
    if i ** 2 > n:
        print(i)
        break
    else:
        i += 1
