#!/usr/bin/env python3
def fibonacci_sequence(n):
    sequence = [0, 1]  # Initializing the first two terms of the Fibonacci sequence

    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Calculating the next term in the sequence
        sequence.append(next_term)

    return sequence

print("{}".format(fibonacci_sequence(6)))
print("{}".format(fibonacci_sequence(1)))
print("{}".format(fibonacci_sequence(0)))
print("{}".format(fibonacci_sequence(20)))