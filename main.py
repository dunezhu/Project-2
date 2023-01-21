import sqlite3
import tkinter as tk

# Create a new database if it doesn't already exist
conn = sqlite3.connect('database.db')

# Create a table in the database
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, date TEXT, subject TEXT, description TEXT)''')

# Create the main window
window = tk.Tk()
window.title("Everything Application")

# Create the entry fields
date_label = tk.Label(text="Date")
date_entry = tk.Entry()
subject_label = tk.Label(text="Subject")
subject_entry = tk.Entry()
description_label = tk.Label(text="Description")
description_entry = tk.Entry()

# Create a function to insert the user's information into the database
def submit():
  # Get the user's input
  date = date_entry.get()
  subject = subject_entry.get()
  description = description_entry.get()

  # Insert the user's information into the database
  conn.execute("INSERT INTO users (date, subject, description) VALUES (?, ?, ?)", (date, subject, description))

  # Commit the changes to the database
  conn.commit()
  
# Create the submit button
submit_button = tk.Button(text="Submit", command=submit)

# Pack the widgets into the window
date_label.pack()
date_entry.pack()
subject_label.pack()
subject_entry.pack()
description_label.pack()
description_entry.pack()
submit_button.pack()

# Start the main loop
window.mainloop()
