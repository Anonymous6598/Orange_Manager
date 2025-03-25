import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys, csv

class App(customtkinter.CTk): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        
        self.title("Orange Manager")
        self.geometry("900x700") 
        self.iconbitmap("slike/Orange_Manager.ico")
        self.protocol("WM_DELETE_WINDOW", sys.exit)
        
        self.appmenu = CTkMenuBar.CTkTitleMenu(self)
            
        self.addbutton = self.appmenu.add_cascade("Dodaj", command=self.NewLine)
        self.editbutton = self.appmenu.add_cascade("Uredi", command=self.EditLine)
        self.deletebutton = self.appmenu.add_cascade("Obriši", command=self.DeleteLine)
        self.loadbutton = self.appmenu.add_cascade("Učitaj tabelu", command=self.LoadData)
        self.savebutton = self.appmenu.add_cascade("Sačuvaj tabelu", command=self.SaveData)
        self.notepadbutton = self.appmenu.add_cascade("Beleške", command=self.OpenNotepad)
        self.aichatbot = self.appmenu.add_cascade("Veštačka inteligencija", command=self.OpenAIChantbot)

        self.tableframe = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill="both", expand=True)

        self.tablevalue = [["Ime", "Menadžer", "Odeljenje", "Naziv posla", "Sati", "Dodatni komentar"]] 

        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) 
        self.table.pack(fill="both", expand=True)

        self.tablevaluecount = 0

    def NewLine(self): 
        self.nameinput = customtkinter.CTkInputDialog(title="Ime", text="Unesite ime", button_fg_color="orange").get_input() 
        if self.nameinput == "" or self.nameinput == None: 
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje") 
           return

        self.managerinput = customtkinter.CTkInputDialog(title="Menadzer", text="Unesite menadzera", button_fg_color="orange").get_input()
        if self.managerinput == "" or self.managerinput == None:
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje")
           return

        self.departmentinput = customtkinter.CTkInputDialog(title="Odeljenje", text="Unesite odeljenje", button_fg_color="orange").get_input()
        if self.departmentinput == "" or self.departmentinput == None:
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje")
           return
                
        self.jobtitleinput = customtkinter.CTkInputDialog(title="Naziv_posla", text="Unesite naziv posla", button_fg_color="orange").get_input()
        if self.jobtitleinput == "" or self.jobtitleinput == None:
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje")
           return         
        
        self.hoursinput = customtkinter.CTkInputDialog(title="Sati", text="Unesite radne sate", button_fg_color="orange").get_input()
        if self.hoursinput == "" or self.hoursinput == None:
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje")
           return

        self.additionalcommentinput = customtkinter.CTkInputDialog(title="Dodatni komentar", text="Unesite dodatni komentar", button_fg_color="orange").get_input()
        if self.additionalcommentinput == "" or self.additionalcommentinput == None:
            tkinter.messagebox.showerror("Greška", "Morate da popunite polje")
            return                

        self.tablevaluecount += 1

        if self.tablevaluecount == 1:
            self.table.add_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"])
        
        else:
            self.table.add_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"])
            self.tablevalue.append([f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"]) 
      
    def EditLine(self):  
        self.columnline = customtkinter.CTkInputDialog(title="Kolona", text="Unesite kolonu", button_fg_color="orange").get_input()
        self.rowline = customtkinter.CTkInputDialog(title="Red", text="Unesite red", button_fg_color="orange").get_input() 
        if self.rowline == "0" or self.rowline == None: 
           tkinter.messagebox.showerror("Greška", "Ne možete da menjate zaglavlje") 
        
        else:
            self.newvalue = customtkinter.CTkInputDialog(title="nova vrednost", text="unesite novu vrednost", button_fg_color="orange").get_input() 

            self.table.edit(row=int(self.rowline), column=int(self.columnline), textvariable=tkinter.StringVar(value=self.newvalue)) 
            self.tablevalue[int(self.rowline)][int(self.columnline)] = self.newvalue
    
    def DeleteLine(self): 
        self.rowline = customtkinter.CTkInputDialog(title="Red", text="Unesite red", button_fg_color="orange").get_input() 
        if self.rowline == "0" or self.rowline == None: 
            tkinter.messagebox.showerror("Greška", "Ne možete da obrisete zaglavlje") 
        
        else:
            self.table.delete_row(int(self.rowline)) 
            for i in range(2):
                self.tablevalue.pop(int(self.rowline)) 
            
            print(self.tablevalue)

    def LoadData(self): 
        self.tablevalue[:] = [] 
        try:
            with open(tkinter.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")], defaultextension=[("CSV Files", "*.csv"), ("All Files", "*.*")]), "r+", newline="") as self.file:
                self.reader = csv.reader(self.file)
                for self.row in self.reader:
                    self.tablevalue.append(self.row)

        except FileNotFoundError:
            pass

        self.table.pack_forget() 
        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) 
        self.table.pack(fill="both", expand=True) 

    def SaveData(self): 
        self.data = self.tablevalue[:] 
        with open(tkinter.filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")], defaultextension=[("CSV Files", "*.csv"), ("All Files", "*.*")]), "w+", newline="") as self.file:
            self.writer = csv.writer(self.file)
            self.writer.writerows(self.data)
        
    def OpenNotepad(self): 
        import notepad 

        notepad.Notes().mainloop()

    def OpenAIChantbot(self): 
        import AI_Window 

        AI_Window.AI_Window().mainloop() 

if __name__ == "__main__":
    App().mainloop() 
