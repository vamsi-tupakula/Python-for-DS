def add(a, b):
    """Add Numbers"""
    return a+b

def sub(a, b):
    """Subtract Numbers"""
    return a - b

def mul(a, b):
    """Multiply Numbers"""
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero(0)..')
    return a/b