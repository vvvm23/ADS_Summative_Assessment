power_dictionary, base_dictionary = {}, {} # Contains calculate powers of k from 0 to 9 and powers of 10 from 0 to 7
# Main function
def count_ephemeral(n_1, n_2, k):
    # Populate power and base dictionaries
    power_dictionary.update({p: p**k for p in range(10)})
    base_dictionary.update({b: 10**b for b in range(10)})
    good = {} # Create empty dictionary of values that have been explored
    c = n_2 # Get initial candidate value
    
    while c > n_1: # While candidate is more than min
        c = c - 1 # Decrement candidate
        if not (c in good): # If candidate has already been discovered skip it.
            path = [c]
            eph = False
            term = False

            #path, eph = r_eph(c, k, good, [c]) # Get path to terminating value and whether c is ephemeral or eternal
            _c = c
            while not term:
                _c = get_child(_c, k)
                if _c == 1:
                    eph = True
                    term = True
                elif _c in good:
                    eph = good[_c]
                    term = True
                elif _c in path:
                    eph = False
                    term = True
                else:
                    path.append(_c)

            good.update({p: eph for p in path}) # Update dictionary

    print(sum(good[k] == True for k in good.keys() if k >= n_1 and k < n_2))
    return sum(good[k] == True for k in good.keys() if k >= n_1 and k < n_2)

# Recursive function
def r_eph(c, k, good, path):
    _c = get_child(c, k) # Get next integer in sequence
    if _c == 1: # If child terminates with 1 return path and that c is ephemeral
        return path, True
    elif _c in good: # If child has been discovered return path and value in dictionary
        return path, good[_c]
    elif _c in path: # If child is in path return path and that c is eternal
        return path, False
    else: # If non-terminating append to path and recursively call.
        path.append(_c)
        return r_eph(_c, k, good, path)

# Function to get next integer in sequence
def get_child(n, k):
    total = 0
    for base in range(7, 0, -1):
        total += power_dictionary[(n//base_dictionary[base])]
        n = n % base_dictionary[base]
    return total + power_dictionary[n]

import time
s_time = time.time()
print(time.time() - s_time)
s_time = time.time()
assert count_ephemeral(1000, 10000, 3) == 91
print(s_time - time.time())

s_time = time.time()
assert count_ephemeral(123456, 654321, 4) == 376
print(s_time - time.time())

s_time = time.time()
assert count_ephemeral(1, 10000000, 2) == 1418853
print(s_time - time.time())

s_time = time.time()
assert count_ephemeral(1, 10000000, 3) == 167818
print(s_time - time.time())

s_time = time.time()
assert count_ephemeral(1, 10000000, 4) == 6727
print(s_time - time.time())