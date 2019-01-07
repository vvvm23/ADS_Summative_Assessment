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
                brk = True
                break
            
        if not brk: # If successfully found free position place key in position
            table[(start + i*inc)%19] = k

    return table # Return table once all keys have been iterated through

class MyException(Exception): # Class to throw exceptions with
    pass

def test_hq():
    assert hash_quadratic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_quadratic([19,38,57,76,95,114,133,152,171,190]) == [95, 133, '-', 19, 38, '-', '-', 57, 190, 114, 171, '-', 76, '-', 152, '-', '-', '-', '-']
    assert hash_quadratic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 71, 3, 19, 43, 13, 29, 7, 23, 61, 17, 41, 11, 59, 5, 2, 37, 53, 31]
    print ("all tests passed")


def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == [304, 361, 266, 19, 76, 152, 228, 95, 171, 38, 114, 190, 57, 133, 209, 247, 285, 323, 342]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 67, 3, 19, 53, 13, 29, 7, 23, 59, 17, 41, 11, 61, 5, 2, 37, 43, 31]
    print ("all tests passed")

import time
s_time = time.time()
test_hq()
test_dh()
print(time.time() - s_time)
