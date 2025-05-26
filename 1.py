
from enum import Enum

class State(Enum):
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3

def accepts_string(input_str):
    current_state = State.S0
    
    for c in input_str:
        if current_state == State.S0:
            if c == '1':
                current_state = State.S1
        elif current_state == State.S1:
            if c == '1':
                current_state = State.S2
            else:
                current_state = State.S0
        elif current_state == State.S2:
            if c == '1':
                current_state = State.S3
            else:
                current_state = State.S0
        elif current_state == State.S3:
            pass  # Stay in S3
    
    return current_state == State.S3

# Directly take input and check
input_str = input("Enter a binary string: ")
if accepts_string(input_str):
    print("Accepted (contains 111)")
else:
    print("Rejected (does not contain 111)")
