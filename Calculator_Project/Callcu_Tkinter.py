import tkinter as tk

# Function to get user input from the entry widget
def get_input():
    entered_text = entry.get()  # Retrieve the text from the entry widget
    return entered_text

# Function to perform calculations and display the result
def display():
    inputs = get_input()  # Get input from entry widget
    try:
        input1, operation, input2 = inputs.split()

        input1 = int(input1)
        input2 = int(input2)

        if operation == "+":
            result = calculator_addition(input1, input2)
        elif operation == "-":
            result = calculator_subtraction(input1, input2)
        elif operation == "x":
            result = calculator_multiplication(input1, input2)
        elif operation == "/":
            if input2 == 0:
                label.config(text="Error: Division by zero is not allowed.")
                return
            result = calculator_division(input1, input2)
        else:
            label.config(text="Invalid operation. Please choose from +, -, x, /.")
            return

        label.config(text=f"{input1} {operation} {input2} = {result}")

    except ValueError:
        label.config(text="Invalid input. Please enter numeric values for numbers.")

# Function definitions for basic arithmetic operations
def calculator_addition(input1, input2):
    return input1 + input2

def calculator_subtraction(input1, input2):
    return input1 - input2

def calculator_multiplication(input1, input2):
    return input1 * input2

def calculator_division(input1, input2):
    return input1 / input2

# Create the main application window
root = tk.Tk()
root.title("Entry Example")

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=display)
submit_button.pack()

# Create a label widget
label = tk.Label(root, text="")
label.pack(pady=20)

# Start the main event loop
root.mainloop()
