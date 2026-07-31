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


def find_menu_item(display_text):
    """Find a menu item using the text shown in the menu."""

    for item in menu_items:
        if item.display_item() == display_text:
            return item

    return None


def update_order_display():
    """Update the order summary and total shown in the window."""

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


def reset_quantity():
    """Reset the quantity box to 1."""

    quantity_spinbox.delete(0, tk.END)
    quantity_spinbox.insert(0, "1")


def add_to_order():
    """Add the selected menu item to the current order."""

    customer_name = customer_entry.get().strip()

    if customer_name == "":
        messagebox.showwarning(
            "Missing Customer Name",
            "Please enter the customer's name."
        )
        customer_entry.focus()
        return

    selected_text = menu_combobox.get()

    if selected_text == "":
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
            "Please enter a whole number from 1 to 10."
        )
        reset_quantity()
        return

    if quantity < 1 or quantity > 10:
        messagebox.showwarning(
            "Invalid Quantity",
            "Quantity must be between 1 and 10."
        )
        reset_quantity()
        return

    selected_item = find_menu_item(selected_text)

    if selected_item is not None:
        current_order.add_item(selected_item, quantity)
        update_order_display()
        reset_quantity()

        status_label.config(
            text=f"Added {quantity} {selected_item.name}(s) to the order."
        )


def place_order():
    """Display the completed customer order."""

    customer_name = customer_entry.get().strip()

    if customer_name == "":
        messagebox.showwarning(
            "Missing Customer Name",
            "Please enter the customer's name."
        )
        customer_entry.focus()
        return

    if len(current_order.items) == 0:
        messagebox.showwarning(
            "Empty Order",
            "Please add at least one item before placing the order."
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

    status_label.config(
        text="The order was completed successfully."
    )


def clear_order():
    """Clear the order and reset all input fields."""

    current_order.clear_order()

    customer_entry.delete(0, tk.END)
    menu_combobox.current(0)
    reset_quantity()
    update_order_display()

    status_label.config(
        text="The order form has been cleared."
    )

    customer_entry.focus()


def confirm_exit():
    """Ask the user to confirm before closing the program."""

    should_exit = messagebox.askyesno(
        "Exit Program",
        "Are you sure you want to exit?"
    )

    if should_exit:
        window.destroy()


# Create the main window.
window = tk.Tk()
window.title("Shaky Coffee Order System")
window.geometry("680x740")
window.minsize(650, 700)
window.configure(bg="#f4eadf")
window.protocol("WM_DELETE_WINDOW", confirm_exit)

# Create a style for the menu box.
style = ttk.Style()

style.configure(
    "Menu.TCombobox",
    font=("Arial", 11)
)

# Main title area.
header_frame = tk.Frame(
    window,
    bg="#5c3d2e",
    padx=20,
    pady=18
)
header_frame.pack(fill="x")

title_label = tk.Label(
    header_frame,
    text="Shaky Coffee",
    font=("Arial", 26, "bold"),
    bg="#5c3d2e",
    fg="white"
)
title_label.pack()

subtitle_label = tk.Label(
    header_frame,
    text="Vietnamese Coffee Shop Order System",
    font=("Arial", 12),
    bg="#5c3d2e",
    fg="white"
)
subtitle_label.pack(pady=(4, 0))

# Main content area.
content_frame = tk.Frame(
    window,
    bg="#f4eadf",
    padx=25,
    pady=20
)
content_frame.pack(
    fill="both",
    expand=True
)

# Customer information section.
customer_frame = tk.LabelFrame(
    content_frame,
    text="Customer Information",
    font=("Arial", 11, "bold"),
    bg="#f4eadf",
    padx=15,
    pady=12
)
customer_frame.pack(
    fill="x",
    pady=(0, 12)
)

customer_label = tk.Label(
    customer_frame,
    text="Customer Name:",
    font=("Arial", 11),
    bg="#f4eadf"
)
customer_label.grid(
    row=0,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

customer_entry = tk.Entry(
    customer_frame,
    width=34,
    font=("Arial", 11)
)
customer_entry.grid(
    row=0,
    column=1,
    padx=8,
    pady=5,
    sticky="ew"
)

customer_frame.columnconfigure(
    1,
    weight=1
)

# Menu selection section.
menu_frame = tk.LabelFrame(
    content_frame,
    text="Menu Selection",
    font=("Arial", 11, "bold"),
    bg="#f4eadf",
    padx=15,
    pady=12
)
menu_frame.pack(
    fill="x",
    pady=(0, 12)
)

menu_label = tk.Label(
    menu_frame,
    text="Menu Item:",
    font=("Arial", 11),
    bg="#f4eadf"
)
menu_label.grid(
    row=0,
    column=0,
    padx=5,
    pady=6,
    sticky="w"
)

menu_choices = []

for item in menu_items:
    menu_choices.append(
        item.display_item()
    )

menu_combobox = ttk.Combobox(
    menu_frame,
    values=menu_choices,
    state="readonly",
    width=34,
    style="Menu.TCombobox"
)
menu_combobox.grid(
    row=0,
    column=1,
    padx=8,
    pady=6,
    sticky="ew"
)
menu_combobox.current(0)

quantity_label = tk.Label(
    menu_frame,
    text="Quantity:",
    font=("Arial", 11),
    bg="#f4eadf"
)
quantity_label.grid(
    row=1,
    column=0,
    padx=5,
    pady=6,
    sticky="w"
)

quantity_spinbox = tk.Spinbox(
    menu_frame,
    from_=1,
    to=10,
    width=8,
    font=("Arial", 11)
)
quantity_spinbox.grid(
    row=1,
    column=1,
    padx=8,
    pady=6,
    sticky="w"
)

add_button = tk.Button(
    menu_frame,
    text="Add to Order",
    width=18,
    font=("Arial", 11, "bold"),
    bg="#c88b4a",
    fg="white",
    activebackground="#ad7438",
    activeforeground="white",
    command=add_to_order
)
add_button.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=(10, 2)
)

menu_frame.columnconfigure(
    1,
    weight=1
)

# Order summary section.
summary_frame = tk.LabelFrame(
    content_frame,
    text="Order Summary",
    font=("Arial", 11, "bold"),
    bg="#f4eadf",
    padx=12,
    pady=12
)
summary_frame.pack(
    fill="both",
    expand=True,
    pady=(0, 10)
)

order_text = tk.Text(
    summary_frame,
    width=55,
    height=9,
    font=("Consolas", 11),
    state="disabled",
    wrap="word"
)
order_text.pack(
    fill="both",
    expand=True
)

total_label = tk.Label(
    content_frame,
    text="Total: $0.00",
    font=("Arial", 17, "bold"),
    bg="#f4eadf",
    fg="#5c3d2e"
)
total_label.pack(
    pady=(4, 8)
)

status_label = tk.Label(
    content_frame,
    text="Enter a customer name and select an item.",
    font=("Arial", 10, "italic"),
    bg="#f4eadf",
    fg="#5c3d2e"
)
status_label.pack(
    pady=(0, 10)
)

# Final buttons.
button_frame = tk.Frame(
    content_frame,
    bg="#f4eadf"
)
button_frame.pack(
    pady=(0, 5)
)

place_order_button = tk.Button(
    button_frame,
    text="Place Order",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#5f7f5f",
    fg="white",
    command=place_order
)
place_order_button.grid(
    row=0,
    column=0,
    padx=6
)

clear_button = tk.Button(
    button_frame,
    text="Clear Order",
    width=14,
    font=("Arial", 10, "bold"),
    command=clear_order
)
clear_button.grid(
    row=0,
    column=1,
    padx=6
)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#9b4d4d",
    fg="white",
    command=confirm_exit
)
exit_button.grid(
    row=0,
    column=2,
    padx=6
)

# Display the empty order message.
update_order_display()

# Move the cursor to the customer name field.
customer_entry.focus()

# Keep the window running.
window.mainloop()