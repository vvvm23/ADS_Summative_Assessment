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
    return sum(good[k] == True for k in good.keys() if k >= n_1 and k < n_2)
	
# Function to get next integer in sequence
def get_child(n, k):
    total = 0
    for base in range(7, 0, -1):
        total += power_dictionary[(n//base_dictionary[base])]
        n = n % base_dictionary[base]
    return total + power_dictionary[n]