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
    
number1 = parse_input("First input: ")
number2 = parse_input("Second input: ")    

total = number1 & number2
print("The total is:", total)
