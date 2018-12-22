def hash_quadratic(keys):
    MAX_ITERATIONS = 1000

    table = ['-'] * 19
    h = lambda k : (6*k + 3) % 19

    for k in keys:
        if not (type(k) is int):
            raise MyException("Non-integer value passed!")

        brk = False
        i = 0
        start = h(k)
        while not (table[(start + i**2) % 19] == '-'):
            i += 1
            if i > MAX_ITERATIONS:
                print("Unable to place {0} after {1} tries with quadratic probing.".format(k, MAX_ITERATIONS))
                brk = True
                break

        if not brk:
            table[(start+i**2)%19] = k

    return table

def hash_double(keys):
    MAX_ITERATIONS = 1000
    
    table = ['-'] * 19
    h_1 = lambda k : (6*k + 3) % 19
    h_2 = lambda k : 11 - (k % 11)

    for k in keys:
        if not (type(k) is int):
            raise MyException("Non-integer value passed!")
            
        brk = False
        i = 0
        start = h_1(k)
        inc = h_2(k)
        while not (table[(start + i*inc)%19] == '-'):
            i += 1
            if i > MAX_ITERATIONS:
                print("Unable to place {0} after {1} tries with quadratic probing.".format(k, MAX_ITERATIONS))
                brk = True
                break
            
        if not brk:
            table[(start + i*inc)%19] = k

    return table

class MyException(Exception):
    pass

#########################################################################################
#print(hash_quadratic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]))
print(hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]))