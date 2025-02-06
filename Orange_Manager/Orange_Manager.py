import customtkinter, CTkMenuBar, tkinter, tkinter.filedialog, tkinter.messagebox, os, sys, subprocess

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Orange Manager")
        self.geometry("900x700")
        self.resizable(False, False)

        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
        self.employlistbutton = self.appmenu.add_cascade("open employee list", command=self.OpenEmployList)
        self.aichatbot = self.appmenu.add_cascade("AI", command=lambda: os.startfile("AI.py", show_cmd=False))

        # Task Manager
                
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