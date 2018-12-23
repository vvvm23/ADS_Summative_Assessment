# Quadratic hashing function
def hash_quadratic(keys):
    MAX_ITERATIONS = 1000 # Define max attempts before giving up

    table = ['-'] * 19 # Create empty hash table
    h = lambda k : (6*k + 3) % 19 # Define hash function

    for k in keys: # For all key in keys
        if not (type(k) is int): # If not integer throw exception
            raise MyException("Non-integer value passed!")

        brk = False
        i = 0 # Set ith term in hash sequence to 0
        start = h(k) # Get start value
        while not (table[(start + i**2) % 19] == '-'): # If current space is not empty in quadratic sequence..
            i += 1 # ..increment i and try again
            if i > MAX_ITERATIONS: # if i is greater than max attemps give up and try next position
                print("Unable to place {0} after {1} tries with quadratic probing.".format(k, MAX_ITERATIONS))
                brk = True
                break

        if not brk: # If successfully found free position place key in position
            table[(start+i**2)%19] = k

    return table # Return table once all keys have been iterated through

# Double hashing function
def hash_double(keys):
    MAX_ITERATIONS = 1000 # Define max attempts before giving up
    
    table = ['-'] * 19 # Create empty hash table
    h_1 = lambda k : (6*k + 3) % 19 # Define primary hash function
    h_2 = lambda k : 11 - (k % 11) # Define secondary hash function

    for k in keys: # For all key in keys
        if not (type(k) is int): # If not integer throw exception
            raise MyException("Non-integer value passed!")
            
        brk = False
        i = 0 # Set ith term in hash sequence to 0
        start = h_1(k) # Get start value
        inc = h_2(k) # Get increment
        while not (table[(start + i*inc)%19] == '-'): # If current space is not empty in double linear sequence..
            i += 1 # ..increment i and try again
            if i > MAX_ITERATIONS: # if i is greater than max attempts give up and try next position
                print("Unable to place {0} after {1} tries with quadratic probing.".format(k, MAX_ITERATIONS))
                brk = True
                break
            
        if not brk: # If successfully found free position place key in position
            table[(start + i*inc)%19] = k

    return table # Return table once all keys have been iterated through

class MyException(Exception): # Class to throw exceptions with
    pass