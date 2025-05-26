from enum import Enum

class State(Enum):
    S0 = 0  # Remainder 0 (divisible by 3)
    S1 = 1  # Remainder 1
    S2 = 2  # Remainder 2

def is_divisible_by_3(input_str):
    current_state = State.S0
    
    for c in input_str:
        if current_state == State.S0:
            if c == '0':
                current_state = State.S0
            elif c == '1':
                current_state = State.S1
        elif current_state == State.S1:
            if c == '0':
                current_state = State.S2
            elif c == '1':
                current_state = State.S0
        elif current_state == State.S2:
            if c == '0':
                current_state = State.S1
            elif c == '1':
                current_state = State.S2
    
    return current_state == State.S0

# Test the function
input_str = input("Enter a binary string: ")
if is_divisible_by_3(input_str):
    print("Accepted (the number is divisible by 3)")
else:
    print("Rejected (the number is not divisible by 3)")
