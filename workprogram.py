import tkinter as tk
from tkinter import ttk
import csv
import os

#check if there is a data.csv file
if not os.path.isfile('data.csv'):
    #create a new data.csv file
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["company name", "location", "date", "callback"])

# Window where the data will be displayed


def data_window():
    popup_window = tk.Toplevel()
    label = tk.Label(popup_window, text="Stats of job hunting")
    label.pack()

    # TODO calculations here to display the data

    # Close button
    close_button = tk.Button(
        popup_window, text="Close Window", command=popup_window.destroy)
    close_button.pack()

# load the data from the file


def load_data():
    table.delete(*table.get_children())
    with open("data.csv", 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            table.insert("", "end", values=row)

# inputs that get the new data from the user


def edit_table():
    selected_row_id = table.focus()

    selected_row_values = table.item(selected_row_id)["values"]

    popup_window = tk.Toplevel(window)
    popup_window.geometry("300x250")

    # Create the entry and labels for the values
    NAME_LABEL = tk.Label(popup_window, text="Enter new name:")
    new_name_entry = tk.Entry(popup_window)
    new_name_entry.insert(0, selected_row_values[0])

    LOCATION_LABEL = tk.Label(popup_window, text="Enter new location:")
    new_location_entry = tk.Entry(popup_window)
    new_location_entry.insert(0, selected_row_values[1])

    DATE_LABEL = tk.Label(popup_window, text="Enter new Date")
    new_date_entry = tk.Entry(popup_window)
    new_date_entry.insert(0, selected_row_values[2])

    CALLBACK_LABEL = tk.Label(popup_window, text="Did the call back?")
    new_callback_entry = tk.Entry(popup_window)
    new_callback_entry.insert(0, selected_row_values[2])

    # Pack the entries & labels
    NAME_LABEL.pack()
    new_name_entry.pack()

    LOCATION_LABEL.pack()
    new_location_entry.pack()

    DATE_LABEL.pack()
    new_date_entry.pack()

    CALLBACK_LABEL.pack()
    new_callback_entry.pack()

    # Creating a save button
    SAVE_BTN = tk.Button(popup_window, text='Save')

    def save_changes():
        # get the values from the entry widgets
        new_name = new_name_entry.get()
        new_location = new_location_entry.get()
        new_date = new_date_entry.get()
        new_callback = new_callback_entry.get()

        # update the selected row
        table.item(selected_row_id, values=(
            new_name, new_location, new_date, new_callback))

        # close the popup
        popup_window.destroy()
    SAVE_BTN.config(command=save_changes)
    SAVE_BTN.pack()


# This function gets the user input and adds it to the list
def add_data():
    # create the popup window
    popup = tk.Toplevel(window)
    # create the labels and the entry widgets
    data_name_label = tk.Label(popup, text="Enter name:")
    name_entry = tk.Entry(popup)

    data_location_label = tk.Label(popup, text="Enter location:")
    location_entry = tk.Entry(popup)

    data_date_label = tk.Label(popup, text="Enter date:")
    date_entry = tk.Entry(popup)

    data_callback_label = tk.Label(popup, text="Enter callback:")
    callback_entry = tk.Entry(popup)

    # after getting the data from the user we write to the csv file
    def save_to_csv():
        data_name = name_entry.get()
        data_location = location_entry.get()
        data_date = date_entry.get()
        data_callback = callback_entry.get()
        with open('data.csv', "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([data_name, data_location,
                            data_date, data_callback])
        load_data()
        popup.destroy()

    data_name_label.pack()
    name_entry.pack()
    data_location_label.pack()
    location_entry.pack()
    data_date_label.pack()
    date_entry.pack()
    data_callback_label.pack()
    callback_entry.pack()
    save_data_button = tk.Button(
        popup, text='Save', command=save_to_csv)
    save_data_button.pack()
    load_data()


def on_closing():
    window.destroy()


# create the window
window = tk.Tk()


# Creates the table
table = ttk.Treeview(window)

table.tag_configure("light", background="lightgray")
table.tag_configure("dark", background="lightblue")

table.pack()
table['columns'] = ('Name', 'Location', 'Date', 'Callback')
# Add column headings
table.heading('Name', text='Name')
table.heading('Location', text='Location')
table.heading('Date', text='Date')
table.heading('Callback', text='Callback')

# tries to open and read the file with the list companies is on
try:
    with open("data.csv", 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            table.insert("", "end", values=row)


except FileNotFoundError:
    print("Data file was not found. Starting with an empty list.")

# table.insert(parent='', index='end', text='0',
#              values=('John', 'sd', 'today', 'no'))

# create button to submit text
add_button = tk.Button(window, text="Add Data", command=add_data)
# Button that shows the data
show_button = tk.Button(window, text="Show Stats", command=data_window)
# button that closes the window
close_button = tk.Button(window, text="Close Window", command=on_closing)
# button that edits the data
edit_button = tk.Button(window, text="Edit", command=edit_table)

add_button.pack(side=tk.LEFT)
edit_button.pack(side=tk.LEFT)
show_button.pack(side=tk.LEFT)
close_button.pack(side=tk.LEFT)

# run main loop
window.mainloop()
