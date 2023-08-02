#!/usr/bin/env/python3
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any value between 2 and sqrt(number), it's not prime

    return True 