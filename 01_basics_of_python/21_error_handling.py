# a = 5
# b= 0
# try:
#     print(a//b)
# except Exception:
#     print('cannot divide with zero....')

try:
    f = open('not_exists.txt')
    print(5//0)
    while(True):
        print('true')
except FileNotFoundError:
    print('file you are looking does not exists')
except ZeroDivisionError:
    print('cannot divide with zero..')
except KeyboardInterrupt:
    print('interrupted!')
except Exception:
    print('sorry, something went wrong...')