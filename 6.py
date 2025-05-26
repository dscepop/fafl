def is_valid_wCwR(input_str):
    stack = []
    i = 0
    n = len(input_str)
    
    # Step 1: Push the first part (w) onto stack until 'C'
    while i < n and input_str[i] != 'C':
        if input_str[i] not in ('0', '1'):
            return False
        stack.append(input_str[i])
        i += 1
    
    # Check if 'C' was found
    if i == n or input_str[i] != 'C':
        return False
    i += 1  # Skip the 'C'
    
    # Step 2: Verify second part matches reverse of first part (wR)
    while i < n:
        if input_str[i] not in ('0', '1'):
            return False
        if not stack or stack.pop() != input_str[i]:
            return False
        i += 1
    
    # Step 3: Accept if stack is empty
    return not stack

# Example usage:
input_str = input("Enter a string (in the form wCwR, where w is binary and C is a special symbol): ")
if is_valid_wCwR(input_str):
    print("Accepted: The string is in the form wCwR.")
else:
    print("Rejected: The string is not in the form wCwR.")
