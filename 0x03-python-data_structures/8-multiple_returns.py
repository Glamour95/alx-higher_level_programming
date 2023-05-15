#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return 0, None
    return len(sentence), sentence[0]


# Test the function
text = "Hello, World!"
result = multiple_returns(text)
print("Length:", result[0])
print("First character:", result[1])
