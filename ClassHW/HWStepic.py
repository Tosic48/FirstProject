n = int(input())
i = 1
while i < n:
    if n < 100:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=' ')
            i += 1
        else:
            i += 1
    else:
        print("слишком большое значение n")
        break

else:
    pass
