import customtkinter as ctk
from tkinter import ttk, messagebox


def add_record():
    """Open a new window to add a record."""
    def save_new_record():
        name = name_entry.get()
        manager = manager_entry.get()
        department = department_entry.get()
        job_title = job_title_entry.get()
        hours = hours_entry.get()

        if all([name, manager, department, job_title, hours]):
            treeview.insert("", "end", values=(name, manager, department, job_title, hours))
            add_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_window = ctk.CTkToplevel()
    add_window.title("Add Record")
    add_window.geometry("900x700")

   
    ctk.CTkLabel(add_window, text="Name:").pack(pady=5)
    name_entry = ctk.CTkEntry(add_window)
    name_entry.pack(pady=5)

    ctk.CTkLabel(add_window, text="Manager:").pack(pady=5)
    manager_entry = ctk.CTkEntry(add_window)
    manager_entry.pack(pady=5)

    ctk.CTkLabel(add_window, text="Department:").pack(pady=5)
    department_entry = ctk.CTkEntry(add_window)
    department_entry.pack(pady=5)

    ctk.CTkLabel(add_window, text="Job Title:").pack(pady=5)
    job_title_entry = ctk.CTkEntry(add_window)
    job_title_entry.pack(pady=5)

    ctk.CTkLabel(add_window, text="Hours:").pack(pady=5)
    hours_entry = ctk.CTkEntry(add_window)
    hours_entry.pack(pady=5)

    
    save_button = ctk.CTkButton(add_window, text="Save", command=save_new_record)
    save_button.pack(pady=10)


def edit_record():
    """Edit the selected record."""
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a record to edit!")
        return

    def save_edited_record():
        name = name_entry.get()
        manager = manager_entry.get()
        department = department_entry.get()
        job_title = job_title_entry.get()
        hours = hours_entry.get()

        if all([name, manager, department, job_title, hours]):
            treeview.item(selected_item, values=(name, manager, department, job_title, hours))
            edit_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    current_values = treeview.item(selected_item, "values")

    edit_window = ctk.CTkToplevel()
    edit_window.title("Edit Record")
    edit_window.geometry("400x300")

    ctk.CTkLabel(edit_window, text="Name:").pack(pady=5)
    name_entry = ctk.CTkEntry(edit_window)
    name_entry.insert(0, current_values[0])
    name_entry.pack(pady=5)

    ctk.CTkLabel(edit_window, text="Manager:").pack(pady=5)
    manager_entry = ctk.CTkEntry(edit_window)
    manager_entry.insert(0, current_values[1])
    manager_entry.pack(pady=5)

    ctk.CTkLabel(edit_window, text="Department:").pack(pady=5)
    department_entry = ctk.CTkEntry(edit_window)
    department_entry.insert(0, current_values[2])
    department_entry.pack(pady=5)

    ctk.CTkLabel(edit_window, text="Job Title:").pack(pady=5)
    job_title_entry = ctk.CTkEntry(edit_window)
    job_title_entry.insert(0, current_values[3])
    job_title_entry.pack(pady=5)

    ctk.CTkLabel(edit_window, text="Hours:").pack(pady=5)
    hours_entry = ctk.CTkEntry(edit_window)
    hours_entry.insert(0, current_values[4])
    hours_entry.pack(pady=5)

    save_button = ctk.CTkButton(edit_window, text="Save", command=save_edited_record)
    save_button.pack(pady=10)


def remove_record():
    """Remove the selected record."""
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a record to remove!")
        return

    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
    if confirm:
        treeview.delete(selected_item)



app = ctk.CTk()
app.title("Overview")
app.geometry("900x700")


title_label = ctk.CTkLabel(app, text="Overview", font=("Arial", 20))
title_label.pack(pady=10)


columns = ("Name", "Manager", "Department", "Job Title", "Hours")
treeview = ttk.Treeview(app, columns=columns, show="headings", height=10)

for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=100)

treeview.insert("", "end", values=("Alice Smith", "John Doe", "Marketing", "Senior Marketing Analyst", 25))
treeview.insert("", "end", values=("Jacob", "Kevin Black", "Finance", "Accountant", 40))
treeview.insert("", "end", values=("Casper", "Lisa Blue", "IT", "Software Developer", 37))

treeview.pack(pady=10, padx=10, fill="both", expand=True)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

add_button = ctk.CTkButton(button_frame, text="Add", fg_color="green", text_color="white", command=add_record)
add_button.grid(row=0, column=0, padx=5)

edit_button = ctk.CTkButton(button_frame, text="Edit", fg_color="yellow", text_color="black", command=edit_record)
edit_button.grid(row=0, column=1, padx=5)

remove_button = ctk.CTkButton(button_frame, text="Remove", fg_color="red", text_color="white", command=remove_record)
remove_button.grid(row=0, column=2, padx=5)

close_button = ctk.CTkButton(button_frame, text="Close", fg_color="black", text_color="white", command=app.quit)
close_button.grid(row=0, column=3, padx=5)


app.mainloop()
