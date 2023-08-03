#!usr/bin/ptyhon3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

# Test
sentence = "Hello, world!"
result = multiple_returns(sentence)
print("Length: {} - First character: {}".format(result[0], result[1]))

