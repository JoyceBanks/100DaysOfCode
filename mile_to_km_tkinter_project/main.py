from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=250, height=120)
window.config(padx=20, pady=20)

# Input
miles_input = Entry(width=10)
miles_input.pack()
miles_input.grid(column=2, row=0)

# Miles
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=3, row=0)
miles_label.config(padx=5, pady=5)

# is equal to
is_equal = Label(text="is equal to", font=("Arial", 10))
is_equal.grid(column=0, row=2)
is_equal.config(padx=5, pady=5)

# Km
kilometer_label = Label(text="Km", font=("Arial", 10))
kilometer_label.grid(column=3, row=2)
kilometer_label.config(padx=5, pady=5)

# Result
result = Label(text=" ")
result.grid(column=2, row=2)


# Calculation
def miles_to_km():
    miles = miles_input.get()
    conversion = int(miles) * 1.609344
    result.config(text=round(conversion, 2))


# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)

window.mainloop()
