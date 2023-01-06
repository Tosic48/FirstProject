
# считывание списка из входного потока
a = '3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана'
lst_in = list(a)
print(lst_in)
B = [i.split() for i in lst_in]
print(B)
F = [i.split()[0] for i in lst_in]
print(F)
d = dict.fromkeys(F)
# d_key = list(d)
# for i in range(len(d)):
#     C = []
#     for j in range(len(B)):
#         if d_key[i] == B[j][0]:
#             C.append(B[j][1])
#     d[d_key[i]] = C
# for key, value in d.items():
#     print(key, ", ".join(value), sep=': ')