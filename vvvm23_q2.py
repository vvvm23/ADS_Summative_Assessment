# Main function
def count_ephemeral(n_1, n_2, k):
    good = {} # Create empty dictionary of values that have been explored
    c = n_2 # Get initial candidate value

    while c > n_1: # While candidate is more than min
        c = c - 1 # Decrement candidate
        if not (c in good): # If candidate has already been discovered skip it.
            path, eph = r_eph(c, k, good, [c]) # Get path to terminating value and whether c is ephemeral or eternal
            if len(path) > 2:
                path = get_similar(path, n_2, n_1)
            good.update({p: eph for p in path if p >= n_1 and p < n_2}) # Update dictionary

    return sum(v == True for v in good.values()) # Count all True values in dictionary and return.

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
        total += (n // (10**base)) ** k
        n = n % (10**base)
    return total + n**k

# Function to get all permutations of all items in path
def get_similar(path, max, min):
    path = list(map(lambda p : list(str(p)), path)) # Convert all integers in path to strings
    _p = []
    for p in path: # Iterate through all integers in path
        _p = permutate(p, 0, len(p) - 1, _p) # Get permutations of current integer
        _p = [n for n in _p if type(n) == int and n >= min and n < max] # Check if within bounds and remove self-identifying lists from within list
    return _p
    
# Function to get permutations of a string
def permutate(string, left, right, p=[]):
    if right == 0: # If one digit integer simply append
        p.append(int(''.join(string)))
    elif left == right: # Base case
        return int(''.join(string))
    else:
        for _ in range(left, right + 1):
            string[left], string[_] = string[_], string[left] # Swap
            p.append(permutate(string, left + 1, right, p)) # Call permutate recursively and append.
            string[left], string[_] = string[_], string[left] # Swap
    return p

import time
"""tests for the function count_ephemeral"""
s_time = time.time()
correct = True
result = count_ephemeral(1, 10, 2)
if result != 2:
    correct = False
    print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was ", result)
result = count_ephemeral(1000, 10000, 3)
if result != 91:
    correct = False
    print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was ", result)
result = count_ephemeral(123456, 654321, 4)
if result != 376:
    correct = False
    print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was ", result)
if correct:
    print("all tests passed")

print(time.time() - s_time)