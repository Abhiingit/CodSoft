import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#calc with a classic gui--> performs basic arithmatic operations with exceptional handling(for bad user input)

window = tk.Tk()
window.title("Simple GUI Calc")
window.geometry("300x400")
window.configure(bg="#202124")

entry = tk.Entry(window, justify='right', font=('Arial', 20), bg="#3C4043", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

result_label = tk.Label(window, text="", pady=10, bg="#202124", fg="#FFFFFF", font=('Arial', 16))
result_label.grid(row=1, column=0, columnspan=4)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text=f"{result}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def insert_number(character):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(character))

def clear_entry():
    entry.delete(0, tk.END)
    result_label.config(text="")

style = ttk.Style()
style.configure('TButton', font=('Arial', 14), foreground="black", background="#E0E0E0")
style.map('TButton', background=[('active', '#B0B0B0')])

button_clear = ttk.Button(window, text="C", command=clear_entry, style="TButton")
button_clear.grid(row=2, column=0, sticky="nsew")
button_div = ttk.Button(window, text="/", command=lambda: insert_number('/'), style="TButton")
button_div.grid(row=2, column=1, sticky="nsew")
button_mul = ttk.Button(window, text="*", command=lambda: insert_number('*'), style="TButton")
button_mul.grid(row=2, column=2, sticky="nsew")
button_sub = ttk.Button(window, text="-", command=lambda: insert_number('-'), style="TButton")
button_sub.grid(row=2, column=3, sticky="nsew")

button7 = ttk.Button(window, text="7", command=lambda: insert_number(7), style="TButton")
button7.grid(row=3, column=0, sticky="nsew")
button8 = ttk.Button(window, text="8", command=lambda: insert_number(8), style="TButton")
button8.grid(row=3, column=1, sticky="nsew")
button9 = ttk.Button(window, text="9", command=lambda: insert_number(9), style="TButton")
button9.grid(row=3, column=2, sticky="nsew")
button_add = ttk.Button(window, text="+", command=lambda: insert_number('+'), style="TButton")
button_add.grid(row=3, column=3, sticky="nsew")

button4 = ttk.Button(window, text="4", command=lambda: insert_number(4), style="TButton")
button4.grid(row=4, column=0, sticky="nsew")
button5 = ttk.Button(window, text="5", command=lambda: insert_number(5), style="TButton")
button5.grid(row=4, column=1, sticky="nsew")
button6 = ttk.Button(window, text="6", command=lambda: insert_number(6), style="TButton")
button6.grid(row=4, column=2, sticky="nsew")

button1 = ttk.Button(window, text="1", command=lambda: insert_number(1), style="TButton")
button1.grid(row=5, column=0, sticky="nsew")
button2 = ttk.Button(window, text="2", command=lambda: insert_number(2), style="TButton")
button2.grid(row=5, column=1, sticky="nsew")
button3 = ttk.Button(window, text="3", command=lambda: insert_number(3), style="TButton")
button3.grid(row=5, column=2, sticky="nsew")

button0 = ttk.Button(window, text="0", command=lambda: insert_number(0), style="TButton")
button0.grid(row=6, column=0, columnspan=2, sticky="nsew")
button_point = ttk.Button(window, text=".", command=lambda: insert_number('.'), style="TButton")
button_point.grid(row=6, column=2, sticky="nsew")

button_equals = ttk.Button(window, text="=", command=calculate, style="TButton")
button_equals.grid(row=4, column=3, rowspan=3, sticky="nsew")

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(7):
    window.rowconfigure(i, weight=1)

window.mainloop()