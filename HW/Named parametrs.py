def get_v(a,b,c, verbose=True): #verbos формальный параметр
    if verbose:
        print(f'a = {a}, b = {b}, c = {c}')
    return a*b*c


v = get_v(1,c=2,b=3) #named in end!!!
print(v)