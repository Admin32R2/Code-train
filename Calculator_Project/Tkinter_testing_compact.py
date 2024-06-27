import tkinter as tk

# Function to handle button clicks and update the entry widget
def on_button_click(character):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(character))

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function to perform calculations and display the result
def calculate_display_error():
    expression = entry.get()  # Get input from entry widget
    try:
        # Evaluate the expression
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Division by zero")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
root = tk.Tk()
root.title("Flexible Calculator")

# Create an entry widget
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons (expanded to include more types of inputs)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 1, 4)
]

# Create and place buttons in the grid
for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    rowspan = button[3] if len(button) > 3 else 1
    colspan = button[4] if len(button) > 4 else 1
    
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=calculate_display_error)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)

# Start the main event loop
root.mainloop()
