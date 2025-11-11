import tkinter as tk
from tkinter import ttk, messagebox
import datainput
import configs
import dbsearch_csv
import dbsearch

def validate_number():
    """Check if the entry is a valid number (int)."""
    user_text = entry.get()


    if not datainput.phone_verification(user_text):
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return None
    return user_text

def show_input():
    """Open a new window with the entered number."""
    user_text = validate_number()
    if user_text is None:
        return

    new_win = tk.Toplevel(root)
    new_win.title("Output")

    label = ttk.Label(new_win, text=f"You entered the number: {user_text}")
    label.pack(padx=20, pady=20)

def search_input():
    """Simulate a search with the entered number."""
    user_text = validate_number()
    if user_text is None:
        return

    custlistindex = dbsearch.lookup_lists_of_lists(listoflistscustomer, user_text, phoneindex)
    if custlistindex == -1:
        messagebox.showerror("Entry Not Found", f"Could not find {user_text} in the database.")
        return
    for element in custlistindex:
        print(element)
    #todo Add lookup function

    new_win = tk.Toplevel(root)
    new_win.title("Search Result")

    label = ttk.Label(new_win, text=f"Searching for number: {user_text}...")
    label.pack(padx=20, pady=20)

file_path = configs.file_path
listoflistscustomer = [] #initialize variable
checkcollist = dbsearch_csv.csv_import(file_path, listoflistscustomer)
phoneindex = dbsearch.get_list_index(checkcollist, "phone")


# Main window
root = tk.Tk()
root.title("Enter the phone number")

ttk.Label(root, text="Enter a phone number (Numbers Only): ex: 1234567890").pack(padx=10, pady=5)
entry = ttk.Entry(root, width=30)
entry.pack(padx=10, pady=5)

# Buttons in a frame (side by side)
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

#ttk.Button(button_frame, text="Submit", command=show_input).pack(side="left", padx=5)
ttk.Button(button_frame, text="Search", command=search_input).pack(side="left", padx=5)

root.mainloop()