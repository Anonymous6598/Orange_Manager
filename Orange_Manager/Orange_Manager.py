import customtkinter, CTkMenuBar, CTkTable, tkinter, tkinter.filedialog, tkinter.messagebox, sys, csv  # Uvoz potrebnih modula i biblioteka

class App(customtkinter.CTk): # Definisanje glavne aplikacione klase koja nasleđuje CTk klasu iz customtkinter biblioteke
    def __init__(self, *args, **kwargs): # Konstruktor klase
        super().__init__(*args, **kwargs) # Poziv konstruktora roditeljske klase
        
        self.title("Orange Manager")
        self.geometry("900x700") 
        self.iconbitmap("slike/Orange_Manager.ico")
        self.protocol("WM_DELETE_WINDOW", sys.exit) # Postavljanje funkcije koja se poziva pri zatvaranju prozora

        self.appmenu = CTkMenuBar.CTkTitleMenu(self) # Kreiranje menija aplikacije
        self.addbutton = self.appmenu.add_cascade("Dodaj", command=self.NewLine)
        self.editbutton = self.appmenu.add_cascade("Uredi", command=self.EditLine)
        self.deletebutton = self.appmenu.add_cascade("Obriši", command=self.DeleteLine)
        self.loadbutton = self.appmenu.add_cascade("Učitaj tabelu", command=self.LoadData)
        self.savebutton = self.appmenu.add_cascade("Sačuvaj tabelu", command=self.SaveData)
        self.notepadbutton = self.appmenu.add_cascade("Beleške", command=self.OpenNotepad)
        self.aichatbot = self.appmenu.add_cascade("Veštačka inteligencija", command=self.OpenAIChantbot)

        self.tableframe = customtkinter.CTkScrollableFrame(self)
        self.tableframe.pack(fill="both", expand=True)

        self.tablevalue = [["Ime", "Menadžer", "Odeljenje", "Naziv posla", "Sati", "Dodatni komentar"]]  # Inicijalizacija vrednosti tabele sa kolonama

        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) # Kreiranje okvira sa mogućnošću skrolovanja
        self.table.pack(fill="both", expand=True) # Postavljanje tabele u prozor

    def NewLine(self): # Definisanje metode za dodavanje novog reda u tabelu
        self.nameinput = customtkinter.CTkInputDialog(title="Ime", text="Unesite ime", button_fg_color="orange").get_input() # Prikaz dijaloga za unos imena
        if self.nameinput == "" or self.nameinput == None: # Provera da li je ime uneseno
           tkinter.messagebox.showerror("Greška", "Morate da popunite polje") # Prikaz poruke o grešci
           return # Prekida rad

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
              
        self.tablevalue.append([f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"]) # Dodavanje novih vrednosti u tabelu
        self.table.add_row(values=[f"{self.nameinput}", f"{self.managerinput}", f"{self.departmentinput}", f"{self.jobtitleinput}", f"{self.hoursinput}", f"{self.additionalcommentinput}"]) # Dodavanje novog reda u tabelu
      
    def EditLine(self): # Definisanje funkcije za uredjivanje reda 
        self.columnline = customtkinter.CTkInputDialog(title="Kolona", text="Unesite kolonu", button_fg_color="orange").get_input() # Unos kolone
        self.rowline = customtkinter.CTkInputDialog(title="Red", text="Unesite red", button_fg_color="orange").get_input() # Unos reda
        if self.rowline == "0" or self.rowline == None: # Provera da li je red zaglavlje
           tkinter.messagebox.showerror("Greška", "Ne možete da menjate zaglavlje") # Prikazivanje greske ako je red zaglavlje
        
        else:
            self.newvalue = customtkinter.CTkInputDialog(title="nova vrednost", text="unesite novu vrednost", button_fg_color="orange").get_input() # Unos nove vrednosti

            self.table.edit(row=int(self.rowline), column=int(self.columnline), textvariable=tkinter.StringVar(value=self.newvalue)) # Menjanje vrednosti u tabeli
            self.tablevalue[int(self.rowline)][int(self.columnline)] = self.newvalue # Azuriranje vrednosti u tabeli
    
    def DeleteLine(self): # Definisanje funkcije za brisanje reda
        self.rowline = customtkinter.CTkInputDialog(title="Red", text="Unesite red", button_fg_color="orange").get_input() # Unos reda
        if self.rowline == "0" or self.rowline == None: # Provera da li je red zaglavlje
            tkinter.messagebox.showerror("Greška", "Ne možete da obrisete zaglavlje") # Prikazivanje greske ako je red zaglavlje
        
        else:
            self.table.delete_row(int(self.rowline)) # Brisanje reda iz tabele
            for i in range(2):
                self.tablevalue.pop(int(self.rowline)) # Uklanjanje vrednosti iz liste

    def LoadData(self): # Definisanje funkcije za ucitavanje podataka
        self.tablevalue[:] = [] # Brisanje trenutnih vrednosti iz tabele
        try:
            with open(tkinter.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")], defaultextension=[("CSV Files", "*.csv"), ("All Files", "*.*")]), "r+", newline="") as self.file:
                self.reader = csv.reader(self.file) # Citanje podataka iz fajla
                for self.row in self.reader: # Iteracija kroz redove u fajlu
                    self.tablevalue.append(self.row) # Dodavanje redova u tabelu

        except FileNotFoundError:
            pass

        self.table.pack_forget() # Skrivanje trenutne tabele
        self.table = CTkTable.CTkTable(self.tableframe, values=self.tablevalue) # Kreiranje nove tabele sa ucitanim vrednostima
        self.table.pack(fill="both", expand=True) # Postavljanje nove tabele u prozor

    def SaveData(self): # Definisanje funkcije za cuvanje podataka
        self.data = self.tablevalue[:] # Kopiranje trenutnih vrednosti iz tabele
        with open(tkinter.filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")], defaultextension=[("CSV Files", "*.csv"), ("All Files", "*.*")]), "w+", newline="") as self.file: # Otvaranje CSV fajla za pisanje
             self.writer = csv.writer(self.file)
             self.writer.writerows(self.data)
        
    def OpenNotepad(self): # Definisanje funkcije za otvaranje beleski
        import notepad # Uvoz modula za beleske

        notepad.Notes().mainloop()

    def OpenAIChantbot(self): # Definisanje funkcije za otvaranje AI chatbot-a
        import AI_Window # Uvoz modula za vestacku inteligenciju

        AI_Window.AI_Window().mainloop() # Pokretanje glavne petlje AI chatbot-a

if __name__ == "__main__":
    App().mainloop() # Pokretanje glavne petlje aplikacije