# a = 5
# b= 0
# try:
#     print(a//b)
# except Exception:
#     print('cannot divide with zero....')

try:
    # f = open('not_exists.txt')
    # print(5//0)
    i = 0;
    while(i < 5):
        print('true')
        i = i + 1
except FileNotFoundError:
    print('file you are looking does not exists')
except ZeroDivisionError:
    print('cannot divide with zero..')
except KeyboardInterrupt:
    print('interrupted!')
except Exception:
    print('sorry, something went wrong...')
else:
    print('code run successful')