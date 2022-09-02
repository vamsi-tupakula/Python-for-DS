"""
    This module will be imported to 12_modules.py file to use the content inside this file
"""

print("Imported helping module...")
string = "this is a string"

def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
        
    return -1

def main():
    print('helping_module\'s main method...')

print('helping_module __name__ :', __name__)

if __name__ == '__main__':
    main()
    print('this file is ran individually....')