import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Orange Manager")
        self.geometry("900x700") 
        self.iconbitmap("slike/Orange_Manager.ico")
        self.protocol("WM_DELETE_WINDOW", sys.exit) 

        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
        self.addbutton = self.appmenu.add_cascade("add", command=self.NewLine)
        self.editbutton = self.appmenu.add_cascade("edit", command=self.EditLine)
        self.deletebutton = self.appmenu.add_cascade("delete", command=self.DeleteLine)
        self.notepadbutton = self.appmenu.add_cascade("notepad", command=self.OpenNotepad)
        self.aichatbot = self.appmenu.add_cascade("AI", command=self.OpenAIChantbot)

        self.tableframe = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill="both", expand=True)

        self.tablevalue = [["name", "manager", "department", "job title", "hours", "additional comment"]]

        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue)
        self.table.pack(fill="both", expand=True)

    def NewLine(self):
        self.nameinput = customtkinter.CTkInputDialog(title="name", text="enter name", button_fg_color="orange").get_input()
        if self.nameinput == "" or self.nameinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
           return

        self.managerinput = customtkinter.CTkInputDialog(title="manager", text="enter manager", button_fg_color="orange").get_input()
        if self.managerinput == "" or self.managerinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
           return

        self.departmentinput = customtkinter.CTkInputDialog(title="department", text="enter department", button_fg_color="orange").get_input()
        if self.departmentinput == "" or self.departmentinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
           return
                
        self.jobtitleinput = customtkinter.CTkInputDialog(title="job title", text="enter job title", button_fg_color="orange").get_input()
        if self.jobtitleinput == "" or self.jobtitleinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
           return         
        
        self.hoursinput = customtkinter.CTkInputDialog(title="hours", text="enter hours", button_fg_color="orange").get_input()
        if self.hoursinput == "" or self.hoursinput == None:
           tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
           return

        self.additionalcommentinput = customtkinter.CTkInputDialog(title="additional comment", text="enter additional comment", button_fg_color="orange").get_input()
        if self.additionalcommentinput == "" or self.additionalcommentinput == None:
            tkinter.messagebox.showerror("Greska", "Morate da popunite polje")
            return                
              
        self.table.add_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"])
      
    def EditLine(self):
        self.columnline = customtkinter.CTkInputDialog(title="column", text="enter column", button_fg_color="orange").get_input()
        self.rowline = customtkinter.CTkInputDialog(title="row", text="enter row", button_fg_color="orange").get_input()
        if self.rowline == "0" or self.rowline == None:
           tkinter.messagebox.showerror("Error", "You cannot edit the header")
        else:
            self.newvalue = customtkinter.CTkInputDialog(title="new value", text="enter new value").get_input()
            self.table.edit(row=int(self.rowline), column=int(self.columnline), textvariable=tkinter.StringVar(value=self.newvalue))
    
    def DeleteLine(self):
        self.rowline = customtkinter.CTkInputDialog(title="row", text="enter row", button_fg_color="orange").get_input()
        if self.rowline == "0" or self.rowline == None:
            tkinter.messagebox.showerror("Error", "You cannot delete the header")
        else:
            self.table.delete_row(int(self.rowline))
        
    def OpenNotepad(self):
        import notepad

        notepad.Notes().mainloop()

    def OpenAIChantbot(self):
        import AI

        AI.AI_Window().mainloop()

if __name__ == "__main__":
    App().mainloop()