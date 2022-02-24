import doctest

# NO ADDITIONAL IMPORTS ALLOWED!
# You are welcome to modify the classes below, as well as to implement new
# classes and helper functions as necessary.


class Symbol:
    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(other, self)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)

class Var(Symbol):
    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `name`, containing the
        value passed in to the initializer.
        """
        self.name = n
        self.prec = 10

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Var(' + repr(self.name) + ')'

    def deriv(self, var):
        if var == self.name:
            return Num(1)
        else:
            return Num(0)

    def simplify(self):
        return Var(self.name)

    def eval(self, mapping):
        return mapping[self.name]

class Num(Symbol):
    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `n`, containing the
        value passed in to the initializer.
        """
        self.n = n
        self.prec = 10

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return 'Num(' + repr(self.n) + ')'

    def deriv(self, var):
        return Num(0)

    def simplify(self):
        return Num(self.n)

    def eval(self, mapping):
        return self.n

class BinOp(Symbol):
    def __init__(self, left, right):
        if isinstance(left, int):
            left = Num(left)
        if isinstance(left, str):
            left = Var(left)
        if isinstance(right, int):
            right = Num(right)
        if isinstance(right, str):
            right = Var(right)
        self.left = left
        self.right = right

    def __repr__(self):
        return self.operation + '(' + repr(self.left) + ',' + repr(self.right) + ')'

    def __str__(self):
        l = str(self.left)
        r = str(self.right)
        if self.prec > self.left.prec:
            l = '(' + str(self.left) + ')'
        if self.prec > self.right.prec:
            r = '(' + str(self.right) + ')'
        if self.operand == '-' or self.operand == '/':
            if self.prec == self.right.prec:
                r = '(' + str(self.right) + ')'
        return l + ' ' + self.operand + ' ' + r

class Add(BinOp):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operation = 'Add'
        self.operand = '+'
        self.prec = 0

    def deriv(self, var):
        return Add(self.left.deriv(var), self.right.deriv(var))

    def simplify(self):
        l = self.left.simplify()
        r = self.right.simplify()
        if l.__str__() == '0':
            return r
        if r.__str__() == '0':
            return l
        if isinstance(l, Num) and isinstance(r, Num):
            return Num(l.n + r.n)
        else:
            return l + r

    def eval(self, mapping):
        l = self.left.eval(mapping)
        r = self.right.eval(mapping)
        return l+r

class Sub(BinOp):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operation = 'Sub'
        self.operand = '-'
        self.prec = 0

    def deriv(self, var):
        return Sub(self.left.deriv(var), self.right.deriv(var))

    def simplify(self):
        l = self.left.simplify()
        r = self.right.simplify()
        if r.__str__() == '0':
            return l
        if isinstance(l, Num) and isinstance(r, Num):
            return Num(l.n - r.n)
        else:
            return l - r

    def eval(self, mapping):
        l = self.left.eval(mapping)
        r = self.right.eval(mapping)
        return l-r

class Mul(BinOp):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operation = 'Mul'
        self.operand = '*'
        self.prec = 1

    def deriv(self, var):
        return Add(Mul(self.left, self.right.deriv(var)),Mul(self.left.deriv(var), self.right))

    def simplify(self):
        l = self.left.simplify()
        r = self.right.simplify()
        if l.__str__() == '0':
            return Num(0)
        if r.__str__() == '0':
            return Num(0)
        if l.__str__() == '1':
            return r
        if r.__str__() == '1':
            return l
        if isinstance(l, Num) and isinstance(r, Num):
            return Num(l.n * r.n)
        else:
            return l * r

    def eval(self, mapping):
        l = self.left.eval(mapping)
        r = self.right.eval(mapping)
        return l*r

class Div(BinOp):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operation = 'Div'
        self.operand = '/'
        self.prec = 1

    def deriv(self, var):
        num = Sub(Mul(self.left.deriv(var), self.right),Mul(self.left, self.right.deriv(var)))
        den = Mul(self.right, self.right)
        return Div(num, den)

    def simplify(self):
        l = self.left.simplify()
        r = self.right.simplify()
        # if l.__str__() == '1' and r.__str__() == '-1':
        #     return Num(-1.0)
        if isinstance(l, Num) and isinstance(r, Num):
            return Num(int(l.n / r.n))
        if l.__str__() == '0':
            return Num(0)
        if r.__str__() == '1':
            return l
        return l / r

    def eval(self, mapping):
        l = self.left.eval(mapping)
        r = self.right.eval(mapping)
        return l/r

def tokenize(expr):
    return expr.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(tokens):
    def parse_expression(index):
        if tokens[index].lstrip('-').isdigit():
            return (Num(int(tokens[index])), index + 1)
        if tokens[index].isalpha():
            return (Var(tokens[index]), index + 1)
        left, op_index = parse_expression(index+1)
        op = tokens[op_index]
        right, end = parse_expression(op_index + 1)
        if op == '+':
            return (Add(left,right), end + 1)
        if op == '-':
            return (Sub(left,right), end + 1)
        if op == '*':
            return (Mul(left,right), end + 1)
        if op == '/':
            return (Div(left,right), end + 1)
    parsed_expression, next_index = parse_expression(0)
    return parsed_expression

def sym(expr):
    return parse(tokenize(expr))

if __name__ == '__main__':
    doctest.testmod()
