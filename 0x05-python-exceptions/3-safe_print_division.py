#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print('Result: {}'.format(result))
        return(result)
