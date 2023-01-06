b = 'Сергей Балакирев'
str_in = b.lower().strip()
print(str_in)
str_out = ''
for i in str_in:
    print(i)
    str_out = str_out + d[i] + ' '
print(str_out.strip())