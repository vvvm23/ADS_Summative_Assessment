def good_expression(expression):

    ''' Better ruleset
        Check these rules recursively every time an open bracket is encountered:
        If expression entirely encompasses in brackets then not good
        If entirely consists of multiplication then it is not good
        ..except for highest level
        If expression is surrounded in addition operators or nothing then it is not good.
        ..except for highest level.
        If any of these rules are triggered ignore everything else and return false
        ..at highest level.
    '''

    expression_stack = Stack()
    object_stack = Stack()

    for c in expression:
        if not expression_stack.isEmpty():
            if expression_stack.top() == ')':
                _e = object_stack.pop()
                _e.after = c
                if _e.after in ['', '+', '(', ')'] and _e.before in ['', '+', '(', ')']:
                    return False
                elif not _e.contains_add:
                    return False

        if c == '(':
            object_stack.push(Expression())
            if expression_stack.isEmpty():
                _e = object_stack.pop()
                _e.before = ''
                object_stack.push(_e)
            else:
                _e = object_stack.pop()
                _e.before = expression_stack.top()
                object_stack.push(_e)

        if c == '+' and not object_stack.isEmpty():
            _e = object_stack.pop()
            _e.contains_add = True
            object_stack.push(_e)

        expression_stack.push(c)

    if expression_stack.top() == ')':
        _e = object_stack.pop()
        _e.after = ''
        if _e.after in ['', '+', '(', ')'] and _e.before in ['', '+', '(', ')']:
            return False
        elif not _e.contains_add:
            return False

    return True

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

print ("all tests passed\n")
