"""
before running any code, python sets certain special variables and __name__ is one of them.
by default, it sets __name__ as '__main__'
"""
print('current module __name__ :', __name__)

"""
If we import someother module, then that module name variable will be by default the file name, then present file name variable will be '__main__'
"""

import helping_module