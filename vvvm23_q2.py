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
            path, eph = r_eph(c, k, good, [c]) # Get path to terminating value and whether c is ephemeral or eternal
            good.update({p: eph for p in path}) # Update dictionary

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

'''
    All permutations of a ephermeral number are also ephermeral. Likewise with eternal numbers.
    Therfore if we calculate these permutations we do not need to check them in the future.
    This should theoretically lead to speed up.
    Although it leads to massive speed up on certain options (approx. 10 second speed up on given tests) 
    ..leads to slow down on other options (1 to 10**7).
    Therefore I have commented the related functions out.
'''
'''
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
'''
import time

s_time = time.time()
count_ephemeral(1, 10, 2)
print(time.time() - s_time)

s_time = time.time()
count_ephemeral(1000, 10000, 3)
print(s_time - time.time())

s_time = time.time()
count_ephemeral(123456, 654321, 4)
print(s_time - time.time())

s_time = time.time()
count_ephemeral(1, 10000000, 2)
print(s_time - time.time())

s_time = time.time()
count_ephemeral(1, 10000000, 3)
print(s_time - time.time())

s_time = time.time()
count_ephemeral(1, 10000000, 4)
print(s_time - time.time())