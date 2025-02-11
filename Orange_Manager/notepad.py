import customtkinter, CTkMenuBar, tkinter, tkinter.messagebox, tkinter.messagebox

class Notes(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        self.title("Notes")
        self.geometry("600x500")

        self.menu_bar = CTkMenuBar.CTkTitleMenu(self)
        self.config(menu=self.menu_bar)

        self.menu_bar.add_cascade("Otvori", command=self.open_file)
        self.menu_bar.add_cascade("Sacuvaj", command=self.save_file)
        self.menu_bar.add_cascade("Obrisi", command=self.clear_text)

        self.text_area = customtkinter.CTkTextbox(self, wrap="word", font=("Arial", 14))
        self.text_area.pack(fill="both", expand=True)

    def save_file(self):
        self.file_path = tkinter.filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if self.file_path:
            try:
                with open(self.file_path, "w+", encoding="utf-8") as self.file:
                    self.file.write(self.text_area.get("1.0", tkinter.END))
                    tkinter.messagebox.showinfo("Sacuvano", "Beleska je uspesno sacuvana.")
            
            except Exception as e:
                tkinter.messagebox.showerror("Greska", f"Doslo je do greske pri cuvanju: {e}")


    def open_file(self):
        self.file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if self.file_path:
           try:
               with open(self.file_path, "r+", encoding="utf-8") as self.file:
                    self.content = self.file.read()
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", self.content)
           
           except Exception("Fajl ne postoji") as e:
               tkinter.messagebox.showerror("Greska", f"Doslo je do greske pri otvaranju: {e}")
       
    def clear_text(self):
        self.text_area.delete("1.0", "end")    

if __name__ == "__main__":
    app = Notes().mainloop()
                                     