def decorator_function(original):
    def inner_function():
        print('This is from decorator function')
        return original()
    return inner_function

@decorator_function
def display():
    print('hello, world...')

# my_func = decorator_function(display)
# my_func()

display()