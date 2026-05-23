from tkinter import *
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt

root = Tk()

root.title("Smart Expense Tracker")

root.geometry("700x600")


# ADD EXPENSE FUNCTION
def add_expense():

    title = title_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    conn = sqlite3.connect("expense.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(title, amount, category, date) VALUES (?, ?, ?, date('now'))",
        (title, amount, category)
    )

    conn.commit()

    conn.close()

    print("Expense Added")


# VIEW EXPENSE FUNCTION
def view_expenses():

    conn = sqlite3.connect("expense.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    table.delete(*table.get_children())

    for row in rows:

        table.insert("", END, values=row)

    conn.close()
def show_pie_chart():

    conn = sqlite3.connect("expense.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category"
    )

    data = cursor.fetchall()

    categories = []
    amounts = []

    for row in data:

        categories.append(row[0])

        amounts.append(row[1])

    plt.pie(
        amounts,
        labels=categories,
        autopct='%1.1f%%'
    )

    plt.title("Expense Analysis")

    plt.show()

    conn.close()
def show_bar_graph():

    conn = sqlite3.connect("expense.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category"
    )

    data = cursor.fetchall()

    categories = []
    amounts = []

    for row in data:

        categories.append(row[0])

        amounts.append(row[1])

    plt.bar(categories, amounts)

    plt.title("Expense Bar Graph")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.show()

    conn.close()


# TITLE
Label(
    root,
    text="SMART EXPENSE TRACKER",
    font=("Arial", 18, "bold")
).pack(pady=20)


# EXPENSE TITLE
Label(root, text="Expense Title").pack()

title_entry = Entry(root, width=40)
title_entry.pack(pady=5)


# AMOUNT
Label(root, text="Amount").pack()

amount_entry = Entry(root, width=40)
amount_entry.pack(pady=5)


# CATEGORY
Label(root, text="Category").pack()

category_entry = Entry(root, width=40)
category_entry.pack(pady=5)


# ADD BUTTON
Button(
    root,
    text="Add Expense",
    command=add_expense,
    width=20
).pack(pady=10)


# VIEW BUTTON
Button(
    root,
    text="View Expenses",
    command=view_expenses,
    width=20
).pack(pady=10)
# PIE CHART BUTTON
Button(
    root,
    text="View Pie Chart",
    command=show_pie_chart,
    width=20
).pack(pady=10)
Button(
    root,
    text="View Bar Graph",
    command=show_bar_graph,
    width=20
).pack(pady=10)


# TABLE
table = ttk.Treeview(
    root,
    columns=("ID", "Title", "Amount", "Category", "Date"),
    show="headings"
)

table.heading("ID", text="ID")
table.heading("Title", text="Title")
table.heading("Amount", text="Amount")
table.heading("Category", text="Category")
table.heading("Date", text="Date")

table.pack(pady=20)


root.mainloop()