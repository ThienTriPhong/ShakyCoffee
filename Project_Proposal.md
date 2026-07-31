# Shaky Coffee Order System Project Proposal

## Company

Shaky Coffee is an imaginary Vietnamese local coffee shop created for this course project.

## Purpose of the System

The purpose of the Shaky Coffee Order System is to help organize customer orders and reduce the need to calculate totals manually. The system allows a user to enter a customer name, select menu items and quantities, calculate the total cost, and place the completed order into a waiting list.

The waiting list displays orders in first-come-first-served order so employees can see which customer order should be prepared next.

## Project Scope

The system focuses on basic coffee shop order management. Users can:

- Enter a customer name
- View menu items and prices
- Select quantities
- Add items to a current order
- View an order summary
- Calculate the total automatically
- Place an order into a waiting list
- Complete orders in first-come-first-served order
- Clear the current order
- Exit the program

The project does not include online payments, customer accounts, inventory management, or permanent database storage.

## General System Design

The application is written in Python and uses Tkinter for the graphical user interface. The interface contains sections for customer information, menu selection, the current order summary, and the waiting-order list.

The program uses lists and dictionaries to organize menu items, current-order information, and placed orders.

## Classes

The system uses three main classes:

### Customer

The `Customer` class stores the customer's name and provides a method for retrieving it.

### MenuItem

The `MenuItem` class stores the name, price, and category of each menu item. It also provides a method for displaying an item and its price.

### Order

The `Order` class stores selected menu items and quantities. It adds items, combines repeated items, calculates the total, creates order summaries, creates order details without prices, and clears the current order.

## Expected Results

The completed system should run without syntax or runtime errors. It should calculate order totals correctly, validate user input, display placed orders in first-come-first-served order, and allow the oldest waiting order to be completed first.