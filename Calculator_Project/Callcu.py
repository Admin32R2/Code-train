# Function to get user input and display a message
def main():
     # Ask for user inputs
    while True:
        
        #General Inputs
        Inputs = input(" ")
        #for User Input 1    
        Input1, Operation, Input2 = Inputs.split()
        
        try: 
            Input1 = int(Input1)
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return
        
        try: 
            Input2 = int(Input2)
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return
        
        #Checks which operation has been selected
        if Operation == ("+"):
            # Perform the addition
            result = calculator_addition(Input1, Input2)

            # Print the result
            print(f"{Input1} + {Input2} = {result}")
        
        elif Operation == ("-"):
            # Perform the addition
            result = calculator_subtaction(Input1, Input2)

            # Print the result
            print(f"{Input1} - {Input2} = {result}")
        
        elif Operation == ("x"):
            # Perform the addition
            result = calculator_multiplication(Input1, Input2)

            # Print the result
            print(f"{Input1} x {Input2} = {result}")
            
        elif Operation == "/":
            #if the user tries tpp divived by zero
            if Input2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = calculator_division(Input1, Input2)
            print(f"{Input1} / {Input2} = {result}")
            
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            continue
        
        
def calculator_addition(Input1, Input2):
    return Input1 + Input2

def calculator_subtaction(Input1, Input2):
    return Input1 - Input2

def calculator_multiplication(Input1, Input2):
    return Input1 * Input2

def calculator_division(Input1, Input2):
    return Input1 / Input2
    
 
   
# Call the function
if __name__ == "__main__":
    main()
