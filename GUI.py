import tkinter as tk
import RenewBooks

class Application(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.geometry("200x200")
        self.parent.title("Log In")
        self.entry1 = tk.Entry(self.parent)
        self.entry1.grid(column=1, row=1)
        self.entry2 = tk.Entry(self.parent, show="*")
        self.entry2.grid(column=1, row=2)
        self.button = tk.Button(self.parent, text="Renovar libros", command=self.renovarLibros)
        self.button.grid(column=1, row=3)
        self.label = tk.Label(self.parent, text="Introduce tu DNI y PIN:")
        self.label.grid(column=1, row=0)

    def renovarLibros(self):
        dni = self.entry1.get()
        pin = self.entry2.get()
        ans = RenewBooks.renew(dni, pin)
        if ans:
            self.label2 = tk.Label(self.parent, text="Libros renovados con exito!!")
            self.label2.grid(column=1, row=4)



root = tk.Tk()
run = Application(root)
root.mainloop()