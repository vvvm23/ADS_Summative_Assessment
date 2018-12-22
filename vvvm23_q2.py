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
            if next == 1 or next in good:
                remove, remove_count = get_similar(path, n_2)
                candidates = [i for i in candidates if i not in remove]
                good += remove
                count += remove_count
                brk = True
                print(c,"is ephermeral")
            elif next in bad or next in path:
                remove, _ = get_similar(path, n_2)
                candidates = [i for i in candidates if i not in remove]
                bad += remove
                brk = True
                print(c,"is eternal")
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
    lists = list(map(lambda n : [n * 10**x for x in range(7) if n * 10**x < max], path))
    out = [i for _ in lists for i in _]
    return out, len(out)
########################################################################################################################
import time
s_time = time.time()
print(count_ephemeral(1, 10000000, 4))
e_time = time.time()
print(e_time - s_time)