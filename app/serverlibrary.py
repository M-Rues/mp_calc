def merge(array, p, q, r,byfunc=None):
    n_left = q-p+1
    n_right = r-q
    left = 0
    right = 0
    dest = p
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    while left<n_left and right <n_right:
        if left_array[left]<=right_array[right]:
            array[dest]=left_array[left]
            left+=1
        else:
            array[dest]=right_array[right]
            right+=1
        dest+=1
    while left<n_left:
        array[dest]=left_array[left]
        left+=1
        dest+=1
    while right<n_right:
        array[dest]=right_array[right]
        right+=1
        dest+=1
def mergesort_recursive(array, p, r):
    if r > p:
        q = (p+r)//2
        mergesort_recursive(array, p, q)
        mergesort_recursive(array, q+1, r)
        merge(array, p, q, r)

def mergesort(array, byfunc=None):
    if byfunc == None:
        mergesort_recursive(array, 0, len(array)-1)
    else:
        mergesort_recursive(tuple_sort(array, byfunc), 0, len(array)-1)
        for i in ls:
            for j in range(len(array)):
                if byfunc(array[j]) == i:
                    array.append(array[j])
                    array.remove(array[j])
                    break

ls =[]
def tuple_sort(array, byfunc):
    ls.clear()
    for i in range(0, len(array)):
        ls.append(byfunc(array[i]))
    return ls

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) ==0:
            return None
        else:
            return self.__items.pop()

    def peek(self):
        if len(self.__items) ==0:
            return None
        else:
            return self.__items[-1]
    @property
    def is_empty(self):
        if len(self.__items) ==0:
            return True
        else:
            False

    @property
    def size(self):
        return len(self.__items)
        pass

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self._expression = string
    for i in string:
        if not i in self.valid_char:
            self.expression = ""

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    self._expression = new_expr
    for i in new_expr:
        if not i in self.valid_char:
            self._expression = ""

  def insert_space(self):
    op = "+-*/()"
    s = ""
    self._expression.replace(" ","")
    for i in self.expression:
        if i in op:
            s = s+" " + i + " "
        else:
            s += i
    self._expression = s
    return self._expression

  
  def helper(self, op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
            return op2 - op1
    elif op == "*":
            return op1 * op2
    else:
        return op2 // op1
    
  def process_operator(self, operand_stack, operator_stack):
    op1 = operand_stack.pop()
    op2 = operand_stack.pop()
    op = operator_stack.pop()
    operand_stack.push(self.helper(op1, op2, op))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    #phase 1
    for i in tokens:
        if i.isdigit():
            operand_stack.push(int(i))
        elif i in "+-":
            while not operator_stack.size == 0 and operator_stack.peek() != '(':
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(i)
        elif i in "*/":
            while operator_stack.peek() == "*" or operator_stack.peek() == "/":
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(i)
        elif i == "(":
            operator_stack.push(i)
        elif i == ")":
            while not operator_stack.peek() == "(":
                self.process_operator(operand_stack, operator_stack)
            operator_stack.pop()
    #phase 2
    while not operator_stack.size == 0:
            self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





