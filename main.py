def get_operation(prompt, var1, var2):
    while True:
        get_operator = input(prompt + "Which operation do you want to use? \n"
                "1. AND operation \n"
                "2. OR operation \n"
                "3. NOT operation \n"
                "4. NAND operation \n"
                "5. NOR operation \n")

        if get_operator == "1":
            return ANDgate(var1, var2)
        elif get_operator == "2":
            return ORgate(var1,var2)
        elif get_operator == "3":
            print("Note: NOT gate only uses the first input.")
            return NOTgate(var1)
        elif get_operator == "4":
            return NANDgate(var1,var2)
        elif get_operator == "5":
            return NORgate(var1,var2)
        else:
            print("Invalid input. Please try again.")



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
    return a | b

def NOTgate(a):
    return int(not a)

def NANDgate(a, b):
  return int(not ANDgate(a, b))

def NORgate(a, b):
    return int(not ORgate(a,b))




var1 = parse_input("First input: ")
var2 = parse_input("Second input: ") 

operator_name = get_operation("--- LOGIC GATE MENU ---\n", var1, var2)
print("The final output is: ", operator_name)
   