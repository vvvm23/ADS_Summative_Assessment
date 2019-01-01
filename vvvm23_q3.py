def good_expression(expression):

    ''' Ruleset
        Check these rules recursively every time an open bracket is encountered:
        If expression entirely encompasses in brackets then not good
        If entirely consists of multiplication then it is not good
        ..except for highest level
        If expression is surrounded in addition operators or nothing then it is not good.
        ..except for highest level.
        If any of these rules are triggered ignore everything else and return false
        ..at highest level.
    '''

    expression_stack = Stack() # Stack to store expression as it is read through so previous character can be read
    object_stack = Stack() # Stores Expression objects so most recent expression can be popped when ) met

    for c in expression: # Iterate through every character in expression
        if not expression_stack.isEmpty():
            if expression_stack.top() == ')': # Check if top of stack is end of an expression
                _e = object_stack.pop() #..if so pop from stack
                _e.after = c
                if _e.after in ['', '+', '(', ')'] and _e.before in ['', '+', '(', ')']:
                    return False # If before and after character of a stack is not multiply then return false
                elif not _e.contains_add:
                    return False # If expression only contained multiplication return false

        if c == '(': # Check if current character is start of expression
            object_stack.push(Expression()) #..if so push new expression object to stack
            if expression_stack.isEmpty():
                _e = object_stack.pop() # if first character set expression.before to nothing
                _e.before = ''
                object_stack.push(_e)
            else:
                _e = object_stack.pop() # else, set expression.before to top of expression stack
                _e.before = expression_stack.top()
                object_stack.push(_e)

        if c == '+' and not object_stack.isEmpty(): # if current character is + and not on top level
            _e = object_stack.pop()
            _e.contains_add = True # set expression.contains_add to true
            object_stack.push(_e)

        expression_stack.push(c) # push current character to expression stack

    # at end of loop check if last character was )
    if expression_stack.top() == ')':
        _e = object_stack.pop()
        _e.after = ''
        if _e.after in ['', '+', '(', ')'] and _e.before in ['', '+', '(', ')']: # if before and after was not multiply
            return False # ..return false
        elif not _e.contains_add: # if expression only contains multiplication
            return False #..return false.

    return True # if does not trigger any rules in ruleset return true.

class Expression:
    def __init__(self):
        self.before = ''
        self.after = ''
        self.contains_add = False

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after

########################################################################################################################
assert good_expression("1+2+3+4")
assert not good_expression("(1+2+3+4)")
assert good_expression("(1+2)*3+4")
assert not good_expression("((1+2))*3+4")
assert good_expression("1+2*3+4")
assert not good_expression("1+(2*3)+4")
assert good_expression("1*2+3+4")
assert not good_expression("1*2+(3+4)")
assert good_expression("(2+3)*(4+3*(3*2+34))")
assert not good_expression("((2+3)*(4+3*(3*2+34)))")
assert not good_expression("(((2+3)*(4+3*(3*2+34))))")
assert good_expression("(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)")
assert not good_expression("((2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4)*(2+3)*(1+7)*(1+4))")
assert good_expression("(3+2)*1")
assert good_expression("3*2*1")
assert not good_expression("(3*2*1)")


print ("all tests passed\n")
