def prefix_decorator(prefix):
    def decorator_function(original):
        def inner_function():
            print(prefix, 'This is from decorator function')
            return original()
        return inner_function
    return decorator_function

@prefix_decorator('LOG:')
def display():
    print('hello, world...')

# my_func = decorator_function(display)
# my_func()

display()