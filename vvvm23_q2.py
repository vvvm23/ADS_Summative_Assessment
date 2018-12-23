# Main function
def count_ephemeral(n_1, n_2, k):
    candidates = range(n_1, n_2) # Generate list of candidate values
    good = {} # Create empty dictionary of values that have been explored

    for c in reversed(candidates): # Iterate through reverse of list (to take advantage of permutation effect)
        if not (c in good): # If candidate has already been discovered skip it.
            path, eph = r_eph(c, k, good, [c]) # Get path to terminating value and whether c is ephemeral or eternal
            remove = get_similar(path, n_2, n_1) # Get permutations of c as they will evaluate to same sequence as c
            good.update({r: eph for r in remove}) # Update dictionary
            '''
            Doing commented method leads to similar timings to above.
            Not quite sure why.
            if eph:
                good.update({r: True for r in remove})
            else:
                good.update({r: False for r in remove})'''

    return sum(v == True for v in good.values()) # Count all True values in dictionary and return.

# Recursive function
def r_eph(c, k, good, path):
    next = get_child(c, k) # Get next integer in sequence
    if next == 1: # If child terminates with 1 return path and that c is ephemeral
        return path, True
    elif next in good: # If child has been discovered return path and value in dictionary
        return path, good[next]
    elif next in path: # If child is in path return path and that c is eternal
        return path, False
    else: # If non-terminating append to path and recursively call.
        path.append(next)
        return r_eph(next, k, good, path)

# Function to get next integer in sequence
def get_child(n, k):
    sum = 0
    for base in range(7, 0, -1):
        sum += (n // (10**base)) ** k
        n = n % (10**base)
    return sum + n**k

# Function to get all permutations of all items in path
def get_similar(path, max, min):
    path = list(map(str, [n for n in path])) # Convert all integers in path to strings
    _p = []
    for p in path: # Iterate through all integers in path
        _p = permutate(p, 0, len(p) - 1, _p) # Get permutations of current integer
        _p = [n for n in _p if type(n) == int]# and n < max] # Check if within bounds and remove self-identifying lists from within list

    out = [n for n in _p if n >= min and n < max] # Check bounds
    return out
    
# Function to get permutations of a string
def permutate(string, left, right, p=[]):
    if type(string) == str: # If string, convert to list to allow for manipulating like a char list.
        string = list(string)
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