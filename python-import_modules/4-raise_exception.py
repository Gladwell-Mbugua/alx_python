#!usr/bin/python3
def raise_exception():
    value = "string"
    value += 5  # This will raise a TypeError
    
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

