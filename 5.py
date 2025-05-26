def is_well_formed_parentheses(input_str):
    stack = []
    for c in input_str:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:  # If stack is empty
                return False
            stack.pop()
        else:
            return False  # Invalid character
    return not stack  # True if stack is empty

# Example usage:
input_str = input("Enter a string of parentheses: ")
if is_well_formed_parentheses(input_str):
    print("Accepted: The parentheses are well-formed.")
else:
    print("Rejected: The parentheses are not well-formed.")
