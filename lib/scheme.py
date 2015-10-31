from functools import reduce

def _get(name):
    return globals()[name]

def eq(x, y):
    "equal? ="
    return x == y

def lt(x, y):
    "<"
    return x < y

def lteq(x, y):
    "<="
    return x <= y

def gt(x, y):
    ">"
    return x > y

def gteq(x, y):
    ">="
    return x >= y

def add(*ps):
    "add +"
    return reduce(lambda x, y: x + y, ps)

def subtract(*ps):
    "subtract -"
    return reduce(lambda x, y: x - y, ps)

def multiply(*ps):
    "multiply *"
    return reduce(lambda x, y: x * y, ps)

def divide(*ps):
    "divide /"
    return reduce(lambda x, y: x / y, ps)

def car(xs):
    "car head"
    return xs[0]

def cdr(xs):
    "cdr tail"
    return xs[1:]

def cons(x, xs):
    "cons"
    if not isinstance(xs, list):
        raise Exception("value '{}' is not a list".format(xs))
    return [x] + xs
