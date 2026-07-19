import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from customer import Customer
from menu_item import MenuItem
from order import Order


# Create the menu items.
menu_items = [
    MenuItem("Vietnamese Iced Coffee", 4.50, "Coffee"),
    MenuItem("Hot Vietnamese Coffee", 4.00, "Coffee"),
    MenuItem("Iced Milk Coffee", 4.25, "Coffee"),
    MenuItem("Jasmine Tea", 3.00, "Tea"),
    MenuItem("Banh Mi", 7.50, "Food")
]

# Create an empty order.
current_order = Order()


def find_menu_item(item_name):
    """Find and return a menu item using its name."""

    for item in menu_items:
        if item.name == item_name:
            return item

    return None


def update_order_display():
    """Update the order summary and total on the screen."""

    order_text.config(state="normal")
    order_text.delete("1.0", tk.END)

    if len(current_order.items) == 0:
        order_text.insert(tk.END, "No items have been added.")
    else:
        order_text.insert(
            tk.END,
            current_order.get_order_summary()
        )

    order_text.config(state="disabled")

    total = current_order.calculate_total()
    total_label.config(text=f"Total: ${total:.2f}")


def add_to_order():
    """Add the selected menu item to the current order."""

    customer_name = customer_entry.get().strip()

    if customer_name == "":
        messagebox.showwarning(
            "Missing Customer Name",
            "Please enter the customer's name."
        )
        return

    selected_name = menu_combobox.get()

    if selected_name == "":
        messagebox.showwarning(
            "Missing Menu Item",
            "Please select a menu item."
        )
        return

    try:
        quantity = int(quantity_spinbox.get())
    except ValueError:
        messagebox.showwarning(
            "Invalid Quantity",
            "Please enter a valid quantity."
        )
        return

    if quantity < 1:
        messagebox.showwarning(
            "Invalid Quantity",
            "Quantity must be at least 1."
        )
        return

    selected_item = find_menu_item(selected_name)

    if selected_item is not None:
        current_order.add_item(selected_item, quantity)
        update_order_display()


def place_order():
    """Display the completed order."""

    customer_name = customer_entry.get().strip()

    if customer_name == "":
        messagebox.showwarning(
            "Missing Customer Name",
            "Please enter the customer's name."
        )
        return

    if len(current_order.items) == 0:
        messagebox.showwarning(
            "Empty Order",
            "Please add at least one item."
        )
        return

    customer = Customer(customer_name)

    order_summary = (
        f"Customer: {customer.get_name()}\n\n"
        f"{current_order.get_order_summary()}\n"
        f"Total: ${current_order.calculate_total():.2f}"
    )

    messagebox.showinfo(
        "Order Complete",
        order_summary
    )


def clear_order():
    """Remove all items from the current order."""

    current_order.clear_order()
    update_order_display()


# Create the main window.
window = tk.Tk()
window.title("Shaky Coffee Order System")
window.geometry("600x750")
window.resizable(True, True)

# Main title.
title_label = tk.Label(
    window,
    text="Shaky Coffee",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    window,
    text="Coffee Shop Order System",
    font=("Arial", 13)
)
subtitle_label.pack(pady=(0, 15))

# Customer information section.
customer_frame = tk.Frame(window)
customer_frame.pack(pady=10)

customer_label = tk.Label(
    customer_frame,
    text="Customer Name:"
)
customer_label.grid(row=0, column=0, padx=5)

customer_entry = tk.Entry(
    customer_frame,
    width=30
)
customer_entry.grid(row=0, column=1, padx=5)

# Menu selection section.
menu_frame = tk.LabelFrame(
    window,
    text="Select a Menu Item",
    padx=15,
    pady=15
)
menu_frame.pack(padx=20, pady=10, fill="x")

menu_label = tk.Label(
    menu_frame,
    text="Menu Item:"
)
menu_label.grid(row=0, column=0, padx=5, pady=5)

menu_names = []

for item in menu_items:
    menu_names.append(item.name)

menu_combobox = ttk.Combobox(
    menu_frame,
    values=menu_names,
    state="readonly",
    width=27
)
menu_combobox.grid(row=0, column=1, padx=5, pady=5)
menu_combobox.current(0)

quantity_label = tk.Label(
    menu_frame,
    text="Quantity:"
)
quantity_label.grid(row=1, column=0, padx=5, pady=5)

quantity_spinbox = tk.Spinbox(
    menu_frame,
    from_=1,
    to=10,
    width=5
)
quantity_spinbox.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(
    menu_frame,
    text="Add to Order",
    width=18,
    command=add_to_order
)
add_button.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=10
)

# Order summary section.
summary_frame = tk.LabelFrame(
    window,
    text="Order Summary",
    padx=10,
    pady=10
)
summary_frame.pack(padx=20, pady=10, fill="both")

order_text = tk.Text(
    summary_frame,
    width=52,
    height=10,
    state="disabled"
)
order_text.pack()

total_label = tk.Label(
    window,
    text="Total: $0.00",
    font=("Arial", 15, "bold")
)
total_label.pack(pady=10)

# Final buttons.
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

place_order_button = tk.Button(
    button_frame,
    text="Place Order",
    width=14,
    command=place_order
)
place_order_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear Order",
    width=14,
    command=clear_order
)
clear_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=14,
    command=window.destroy
)
exit_button.grid(row=0, column=2, padx=5)

# Show the empty order message when the program starts.
update_order_display()

# Keep the window running.
window.mainloop()