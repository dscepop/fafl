def is_valid_string(input_str):
    stack = []
    i = 0
    n = len(input_str)
    
    # Push all leading '0's onto the stack
    while i < n and input_str[i] == '0':
        stack.append('0')
        i += 1
    
    # Pop '0's for each '1'
    while i < n and input_str[i] == '1':
        if not stack:  # Stack is empty (no matching '0')
            return False
        stack.pop()
        i += 1
    
    # String is valid if we processed all characters and stack is empty
    return i == n and not stack

# Example usage:
input_str = input("Enter a string of 0's and 1's: ")
if is_valid_string(input_str):
    print("Accepted: The string has equal number of 0's and 1's in the form 0^n1^n.")
else:
    print("Rejected: The string does not have equal number of 0's and 1's in the form 0^n1^n.")
