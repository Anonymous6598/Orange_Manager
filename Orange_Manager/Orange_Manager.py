import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, os, sys, subprocess

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Orange Manager")
        self.geometry("900x700")

        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
        self.employlistbutton = self.appmenu.add_cascade("open employee list", command=self.OpenEmployList)
        self.addbutton = self.appmenu.add_cascade("add", command=self.NewLine)
        self.editbutton = self.appmenu.add_cascade("edit", command=self.EditLine)
        self.deletebutton = self.appmenu.add_cascade("delete", command=self.DeleteLine)
        self.aichatbot = self.appmenu.add_cascade("AI", command=lambda: os.startfile("AI.py", show_cmd=False))

        self.tableframe = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill="both", expand=True)

        self.tablevalue = [["name", "manager", "department", "job title", "hours", "additional comment"]]
        self.tableindex = 1

        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
        self.table.pack(fill="both", expand=True)

    def NewLine(self):
        self.nameinput = customtkinter.CTkInputDialog(title="name", text="enter name").get_input()
        self.managerinput = customtkinter.CTkInputDialog(title="manager", text="enter manager").get_input()
        self.departmentinput = customtkinter.CTkInputDialog(title="department", text="enter department").get_input()
        self.jobtitleinput = customtkinter.CTkInputDialog(title="job title", text="enter job title").get_input()
        self.hoursinput = customtkinter.CTkInputDialog(title="hours", text="enter hours").get_input()
        self.additionalcommentinput = customtkinter.CTkInputDialog(title="additional comment", text="enter additional comment").get_input()

        self.table.add_row([f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"], index=self.tableindex+1)
      
    def EditLine(self):
        self.rowline = customtkinter.CTkInputDialog(title="row", text="enter row").get_input()
        if self.rowline == "0":
            tkinter.messagebox.showerror("Error", "You cannot edit the header")
        else:
            self.nameinput = customtkinter.CTkInputDialog(title="name", text=f"{self.tablevalue[int(self.rowline)][0]}").get_input()
            self.managerinput = customtkinter.CTkInputDialog(title="manager", text=f"{self.tablevalue[int(self.rowline)][1]}").get_input()
            self.departmentinput = customtkinter.CTkInputDialog(title="department", text=f"{self.tablevalue[int(self.rowline)][2]}").get_input()
            self.jobtitleinput = customtkinter.CTkInputDialog(title="job title", text=f"{self.tablevalue[int(self.rowline)][3]}").get_input()
            self.hoursinput = customtkinter.CTkInputDialog(title="hours", text=f"{self.tablevalue[int(self.rowline)][4]}").get_input()
            self.additionalcommentinput = customtkinter.CTkInputDialog(title="additional comment", text=f"{[int(self.rowline)][-1]}").get_input()
            self.table.edit_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"], row=int(self.rowline))

    def DeleteLine(self):
        self.rowline = customtkinter.CTkInputDialog(title="row", text="enter row").get_input()
        if self.rowline == "0":
            tkinter.messagebox.showerror("Error", "You cannot delete the header")
        else:
            self.table.delete_row(int(self.rowline)+1)
        
    def OpenEmployList(self):
        employeelistwindow = customtkinter.CTkToplevel()
        employeelistwindow.title("Employee List")
        employeelisttextbox = customtkinter.CTkTextbox(employeelistwindow, state="disabled")
        employeelisttextbox.pack(fill="both", expand=True)

        with open(tkinter.filedialog.askopenfilename(), "r+") as employeelist:
             employeelisttextbox.configure(state="normal")
             employeelisttextbox.insert("1.0", employeelist.read())
             employeelisttextbox.configure(state="disabled")

if __name__ == "__main__":
    App().mainloop()