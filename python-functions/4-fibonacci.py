#!/usr/bin/env/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0, 1]
    
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers[:n]
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))