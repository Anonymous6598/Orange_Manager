import customtkinter, CTkMenuBar, tkinter, tkinter.filedialog, tkinter.messagebox, g4f, sqlite3, json, os, sys


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Orange Manager")
        self.geometry("900x700")
        self.resizable(False, False)

        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
        self.employlistbutton = self.appmenu.add_cascade("open employee list", command=self.OpenEmployList)
        self.databasebutton = self.appmenu.add_cascade("database")
        self.aichatbot = self.appmenu.add_cascade("AI")

        self.databasesubmenu = CTkMenuBar.CustomDropdownMenu(widget=self.databasebutton)
        self.importdatabasebutton = self.databasesubmenu.add_option(option="import")
        self.createdatabasebutton = self.databasesubmenu.add_option(option="create")

                
    def OpenEmployList(self):
        employeelistwindow = customtkinter.CTkToplevel()
        employeelistwindow.title("Employee List")
        employeelisttextbox = customtkinter.CTkTextbox(employeelistwindow, state="disabled")
        employeelisttextbox.pack(fill="both", expand=True)

        with open(tkinter.filedialog.askopenfilename(), "r+") as employeelist:
             employeelisttextbox.configure(state="normal")
             employeelisttextbox.insert("1.0", employeelist.read())
             employeelisttextbox.configure(state="disabled")
        
FILE_PATH = "employees.txt"

def load_employees():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return [line.strip().split(",") for line in file.readlines()]

def save_employees(employees):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for emp in employees:
            file.write(",".join(emp) + "\n")

    def add_employee(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()
        
        if not name or not position or not salary:
            messagebox.showerror("Greška", "Sva polja moraju biti popunjena!")
            return
        
        try:
            salary = float(salary)
        except ValueError:
            messagebox.showerror("Greška", "Plata mora biti broj!")
            return
        
        employees = load_employees()
        emp_id = str(len(employees) + 1)
        employees.append([emp_id, name, position, str(salary)])
        save_employees(employees)
        
        messagebox.showinfo("Uspešno", "Zaposleni je dodat!")
        self.name_entry.delete(0, 'end')
        self.position_entry.delete(0, 'end')
        self.salary_entry.delete(0, 'end')
        
    def remove_employee(self):
        employee_id = self.name_entry.get()
        
        if not employee_id:
            messagebox.showerror("Greška", "Unesite ID zaposlenog!")
            return
        
        employees = load_employees()
        employees = [emp for emp in employees if emp[0] != employee_id]
        save_employees(employees)
        
        messagebox.showinfo("Uspešno", "Zaposleni je uklonjen!")
        self.name_entry.delete(0, 'end')
        
    def view_employees(self):
        self.employee_list.delete("1.0", "end")
        employees = load_employees()
        
        for emp in employees:
            self.employee_list.insert("end", f"ID: {emp[0]}, Ime: {emp[1]}, Pozicija: {emp[2]}, Plata: {emp[3]}\n")
        

if __name__ == "__main__":
    App().mainloop()