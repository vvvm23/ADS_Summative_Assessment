def count_ephemeral(n_1, n_2, k):
    candidates = list(range(n_1, n_2))
    count = 0
    good = []
    bad = []
    while len(candidates) > 0:
        c = candidates[0]
        path = [c]
        brk = False
        next = c
        while not brk:
            next = get_child(next, k)
            if next in good or next in bad or next == 1 or next in path: # THIS LINE IS FUCKED
                remove, remove_count = get_similar(path, n_2)
                candidates = [n for n in candidates if not n in remove]
                brk = True
                if next in good or next == 1:
                    print(c,"is ephemeral.")
                    count += remove_count
                    good = good + remove
                else:
                    print(c,"is eternal")
                    bad = bad + remove
            else:
                path.append(next)
    return count

def get_child(n, k):
    sum = 0
    for base in range(7, 0, -1):
        sum += (n // (10**base)) ** k
        n = n % (10**base)
    return sum + n**k

def get_similar(path, max):
    path = list(map(str, path))
    for p in path:
        _p = permutate(p, 0, len(p) - 1)
        _p = [n for n in _p if type(n) == int]

    lists = list(map(lambda n : [n * 10**x for x in range(7) if n * 10**x < max], _p))
    out = [i for _ in lists for i in _]
    return out, len(out)

def permutate(string, left, right, p=[]):
    if type(string) == str:
        string = list(string)
    if right == 0:
        p.append(int(''.join(string)))
    elif left == right:
        return int(''.join(string))
    else:
        for _ in range(left, right + 1):
            string[left], string[_] = string[_], string[left]
            p.append(permutate(string, left + 1, right, p))
            string[left], string[_] = string[_], string[left]
    return p

########################################################################################################################
import time
s_time = time.time()
count_ephemeral(1, 20, 2)
e_time = time.time()

#path = [1, 123]

#print(get_similar(path, 10000000))

#path = list(map(str, path))

#for p in path:
#    _p = permutate(p, 0, len(p) - 1)
#    _p = [n for n in _p if type(n) == int]
#print(_p)