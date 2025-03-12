import customtkinter, CTkMenuBar, tkinter, tkinter.messagebox, tkinter.messagebox, platform, tkinterdnd2

class Window(customtkinter.CTk, tkinterdnd2.TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.TkdndVersion = tkinterdnd2.TkinterDnD._require(self)

class Notes(Window):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        self.title("Notes")
        self.geometry("600x500")
        if platform.system() == f"Windows":
            self.iconbitmap("slike/Orange_Manager.ico")

        if platform.system() == f"Windows":
            self.menu_bar = CTkMenuBar.CTkTitleMenu(self) 
        
        else:
            self.menu_bar = CTkMenuBar.CTkMenuBar(self) 

        self.menu_bar.add_cascade("Otvori", command=self.open_file)
        self.menu_bar.add_cascade("Sačuvaj", command=self.save_file)
        self.menu_bar.add_cascade("Obriši", command=self.clear_text)

        self.text_area = customtkinter.CTkTextbox(self, wrap="word", font=("Arial", 14))
        self.text_area.pack(fill="both", expand=True)

        self.text_area.drop_target_register(tkinterdnd2.DND_ALL)
        self.text_area.dnd_bind("<<Drop>>", self.drop_files)

    def save_file(self):
        self.file_path = tkinter.filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], defaultextension=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if self.file_path:
            try:
                with open(self.file_path, "w+", encoding="utf-8") as self.file:
                    self.file.write(self.text_area.get("1.0", tkinter.END))
                    tkinter.messagebox.showinfo("Sačuvano", "Beleška je uspešno sačuvana.")
            
            except FileNotFoundError as e:
                tkinter.messagebox.showerror("Greška", f"Došlo je do greške pri čuvanju: {e}")


    def open_file(self):
        self.file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], defaultextension=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if self.file_path:
           try:
               with open(self.file_path, "r+", encoding="utf-8") as self.file:
                    self.content = self.file.read()
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", self.content)
           
           except FileNotFoundError("Fajl ne postoji") as e:
               tkinter.messagebox.showerror("Greška", f"Došlo je do greške pri otvaranju: {e}")

    def drop_files(self, event):
        try:
            with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file:
                 self.text_area.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass
       
    def clear_text(self):
        self.text_area.delete("1.0", "end")    

if __name__ == "__main__":
    app = Notes().mainloop()  