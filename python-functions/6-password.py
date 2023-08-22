#!/usr/bin/env/python3
def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False
    
    for char in password:
        # Check for at least one uppercase letter
        if char.isupper():
            has_upper = True
         # Check for at least one lowercase letter
        elif char.islower():
            has_lower = True
        # Check for at least one digit
        elif char.isdigit():
            has_digit = True
         # Check for at least one space
        elif char.isspace():
            has_space = True

    return has_upper and has_lower and has_digit and not has_space
