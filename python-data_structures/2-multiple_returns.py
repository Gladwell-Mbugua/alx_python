#!usr/bin/ptyhon3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

# Test
sentence = "Hello, world!"
result = multiple_returns(sentence)
print(result)  # Output: (13, 'H')

empty_sentence = ""
empty_result = multiple_returns(empty_sentence)
print(empty_result)  # Output: (0, None)
