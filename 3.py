from enum import Enum

class State(Enum):
    S0 = 0
    S1 = 1
    S2 = 2
    
def is_divisible_by_3(input_str):
    current_state = State.S0
    
    for c in input_str:
        if not c.isdigit():
            print("Invalid input: Non-decimal character encountered!")
            return False
        
        digit = int(c)  
        
        if current_state == State.S0:
            current_state = State((0*10+digit)%3)
        elif current_state == State.S1:
            current_state = State((1*10+digit)%3)
        elif current_state == State.S2:
            current_state = State((2*10+digit)%3)
            
    return current_state == State.S0
    
input_str = input("Enter your input string: ")
if is_divisible_by_3(input_str):
    print("Accepted (is divisible by 3)")
else:
    print("Rejected (is not divisible by 3)")
