def count_ephemeral(n_1, n_2, k):
    candidates = range(n_1, n_2)
    good, bad = [], []

    for c in reversed(candidates):
        if not (c in good or c in bad):
            path, eph = r_eph(c, k, good, bad, [c])
            remove, _ = get_similar(path, n_2, n_1)
            if eph:
                good = list(set(good + remove))
            else:
                bad = list(set(bad + remove))
    return len(good)

def r_eph(c, k, good, bad, path):
    next = get_child(c, k)
    if next == 1 or next in good:
        return path, True
    elif next in path or next in bad:
        return path, False
    else:
        path.append(next)
        return r_eph(next, k, good, bad, path)

def get_child(n, k):
    sum = 0
    for base in range(7, 0, -1):
        sum += (n // (10**base)) ** k
        n = n % (10**base)
    return sum + n**k
def get_similar(path, max, min):
    path = list(map(str, [n for n in path]))
    _p = []
    for p in path:
        _p = permutate(p, 0, len(p) - 1, _p)
        _p = [n for n in _p if type(n) == int and n < max]

    lists = list(map(lambda n : [n * 10**x for x in range(7) if n * 10**x < max and n * 10**x >= min], _p))
    out = list(set([i for _ in lists for i in _]))
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
print(count_ephemeral(1, 1000, 2))
e_time = time.time()
print(e_time - s_time)