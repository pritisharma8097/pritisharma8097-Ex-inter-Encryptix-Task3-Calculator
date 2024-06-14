import tkinter as tk

def click(event):
    current = display_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(current + button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create a display widget
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvar=display_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 18))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI event loop
root.mainloop()
