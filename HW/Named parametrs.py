# def get_v(a,b,c, verbose=True): #verbos формальный параметр
#     if verbose:
#         print(f'a = {a}, b = {b}, c = {c}')
#     return a*b*c
#
#
# v = get_v(1,c=2,b=3) #named in end!!!
# print(v)
# ------------------------------------------
# def cmp_str(s1, s2, reg=False, trim=True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s2.strip()
#     return s1 == s2
#
#
# print(cmp_str('Python ', ' Python', trim=False))
#________________________________________________
# def add_value(value, lst=[]) #списолк изменяемый потому там 1 ца остается
#     lst.append(value)
#     return lst
#
# l = add_value(1)
# l = add_value(2)
# print(l)
def check_password(passw, chars = "$%!?@#"):
    if len(passw) >= 8:
        for i in passw:
            if i in chars:
                return True
            else:
                False
    else:
        return False

