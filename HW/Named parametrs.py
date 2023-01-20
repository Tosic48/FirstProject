# def get_v(a,b,c, verbose=True): #verbos формальный параметр
#     if verbose:
#         print(f'a = {a}, b = {b}, c = {c}')
#     return a*b*c
#
#
# v = get_v(1,c=2,b=3) #named in end!!!
# print(v)

def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    return s1 == s2


print(cmp_str('Python ', ' Python', trim=False))
