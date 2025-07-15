import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys, csv, typing, LLM, speech_recognition, threading

slm = LLM.LargeLanguageModel().init_model()

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
        AI_Window()

class AI_Window(customtkinter.CTkToplevel):
    def __init__(self: typing.Self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title("ai chatbot")
        self.geometry(f"525x300")
        self.resizable(False, False)
        self.after(250, lambda: self.iconbitmap("slike/Orange_Manager.ico"))
        
        self.ai_window_textbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
        self.ai_window_textbox.place(x=0, y=0)

        self.ai_window_textbox.configure(state=f"disabled")

        self.ai_window_entry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
        self.ai_window_entry.place(x=0, y=269)

        self.ai_window_microphone_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.AudioInput)
        self.ai_window_microphone_button.place(x=465, y=269)

        self.ai_window_send_request_button = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.Response)
        self.ai_window_send_request_button.place(x=495, y=269)

        self.ai_window_entry.bind(f"<Return>", self.Response)

    def Response(self, configure):
        self.ai_window_entry_data = self.ai_window_entry.get()

        def run_model():
            self.query = LLM.LargeLanguageModel().ResponseFromAI(f"<|system|>You are a helpful AI assistant, who knows everything about business and organization.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>", slm)

            def update_gui():
                self.ai_window_textbox.configure(state="normal")
                self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nLlama:\n{self.query}\n")
                self.ai_window_textbox.configure(state="disabled")
                self.ai_window_entry.delete(0, tkinter.END)

            self.after(0, update_gui)

        threading.Thread(target=run_model).start()

    def AudioInput(self):
        self.recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as self.source:
            self.audio_data = self.recognizer.record(self.source, duration=5)
            self.text = self.recognizer.recognize_google(self.audio_data)

        self.ai_window_entry.insert(f"0", self.text)

if __name__ == "__main__":
    App().mainloop() 
