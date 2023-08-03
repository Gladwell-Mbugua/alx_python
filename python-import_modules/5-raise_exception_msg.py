#!usr/bin/env/python3

def raise_exception_msg(message=""):
    raise NameError(message)

# Test
try:
    raise_exception_msg("This is a custom name exception.")
except NameError as e:
    print("Caught exception:", e)