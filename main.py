def parse_input(prompt):
    high_inputs = ["1", "High", "high", "Yes", "yes", "On", "on", "True", "true"]
    low_inputs = ["0", "Low", "low", "No", "no", "Off", "off", "False", "false"]

    while True: 
        user_input = input(prompt) 
        
        if user_input in high_inputs:
            return 1 
        elif user_input in low_inputs:
            return 0
        else:
            print("Invalid input. Please try again.")


def ANDgate(a, b):
    return a & b

def ORgate(a, b):
    return a or b

def NOTgate(a):
    return int(not a)

def NANDgate(a, b):
  return int(not ANDgate(a, b))

def NORgate(a, b):
    return int(not ORgate(a,b))



var1 = parse_input("First input: ")
var2 = parse_input("Second input: ")    


