import sqlite3
import tkinter as tk

# Create a new database if it doesn't already exist
conn = sqlite3.connect('database.db')

# Create a table in the database
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, date TEXT, symbol TEXT, amount TEXT, direction TEXT)''')

# Create the main window
window = tk.Tk()
window.title("Ticker Movement")

# Create the entry fields
date_label = tk.Label(text="Date")
date_entry = tk.Entry()
symbol_label = tk.Label(text="Symbol")
symbol_entry = tk.Entry()
amount_label = tk.Label(text="Amount")
amount_entry = tk.Entry()
direction_label = tk.Label(text="Direction")
direction_entry = tk.Entry()

# Create a function to insert the user's information into the database
def submit():
  # Get the user's input
  date = date_entry.get()
  symbol = symbol_entry.get()
  amount = amount_entry.get()
  direction = direction_entry.get()

  # Insert the user's information into the database
  conn.execute("INSERT INTO users (date, symbol, amount, direction) VALUES (?, ?, ?, ?)", (date, symbol, amount, direction))

  # Commit the changes to the database
  conn.commit()
  
# Create the submit button
submit_button = tk.Button(text="Submit", command=submit)

# Pack the widgets into the window
date_label.pack()
date_entry.pack()
symbol_label.pack()
symbol_entry.pack()
amount_label.pack()
amount_entry.pack()
direction_label.pack()
direction_entry.pack()
submit_button.pack()

# Start the main loop
window.mainloop()
