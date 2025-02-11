import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys, os

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Orange Manager")
        self.geometry("900x700")
        self.protocol("WM_DELETE_WINDOW", sys.exit) 

        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
        self.addbutton = self.appmenu.add_cascade("add", command=self.NewLine)
        self.editbutton = self.appmenu.add_cascade("edit", command=self.EditLine)
        self.deletebutton = self.appmenu.add_cascade("delete", command=self.DeleteLine)
        self.notepadbutton = self.appmenu.add_cascade("notepad", command=self.OpenNotepad)
        self.aichatbot = self.appmenu.add_cascade("AI", command=lambda: os.popen("AI.py"))

        self.tableframe = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill="both", expand=True)

        self.tablevalue = [["name", "manager", "department", "job title", "hours", "additional comment"]]
        self.tableindex = 1
        self.tablevalueindex = 0

        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
        self.table.pack(fill="both", expand=True)

    def NewLine(self):
        self.nameinput = customtkinter.CTkInputDialog(title="name", text="enter name").get_input()
        if self.nameinput == "" or self.nameinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")

        else:
            self.managerinput = customtkinter.CTkInputDialog(title="manager", text="enter manager").get_input()
            if self.managerinput == "" or self.managerinput == None:
                tkinter.messagebox.showerror("Greska", "Morate da popunite polje")

            else:
                self.departmentinput = customtkinter.CTkInputDialog(title="department", text="enter department").get_input()
                if self.departmentinput == "" or self.departmentinput == None:
                    tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
                else:
                    self.jobtitleinput = customtkinter.CTkInputDialog(title="job title", text="enter job title").get_input()
                    if self.jobtitleinput == "" or self.jobtitleinput == None:
                        tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
                    else:
                        self.hoursinput = customtkinter.CTkInputDialog(title="hours", text="enter hours").get_input()
                        if self.hoursinput == "" or self.hoursinput == None:
                           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
                        else:
                            self.additionalcommentinput = customtkinter.CTkInputDialog(title="additional comment", text="enter additional comment").get_input()
                            if self.additionalcommentinput == "" or self.additionalcommentinput == None:
                                tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
                            else:
                                self.table.add_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"], index=self.tableindex+1)
      
    def EditLine(self):
        self.rowline = int(customtkinter.CTkInputDialog(title="row", text="enter row").get_input())
        self.columnline = int(customtkinter.CTkInputDialog(title="column", text="enter column").get_input())
        if self.rowline == "0":
           tkinter.messagebox.showerror("Error", "You cannot edit the header")
        else:
            self.newvalue = customtkinter.CTkInputDialog(title="new value", text="enter new value").get_input()
            self.table.edit(row=self.rowline, column=self.columnline, text=f"{self.newvalue}")
    
    def DeleteLine(self):
        self.rowline = customtkinter.CTkInputDialog(title="row", text="enter row").get_input()
        if self.rowline == "0":
            tkinter.messagebox.showerror("Error", "You cannot delete the header")
        else:
            self.table.delete_row(int(self.rowline))
        
    def OpenNotepad(self):
        import notepad

        notepad.Notes().mainloop()

if __name__ == "__main__":
    App().mainloop()

"""
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

"""