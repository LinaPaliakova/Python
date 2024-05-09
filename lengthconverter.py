from tkinter import *
from tkinter import ttk


class Form:
    def __init__(self, master):
        master.title ('Length Converter: Miles to KM')
        master.resizable(False, False)

        self.frame1 = ttk.Frame(master)
        self.frame1.pack()

        self.number_entry = ttk.Entry(self.frame1, width=20)
        self.number_entry.grid(row=0, column=0, padx=5, pady=9)
        ttk.Label(self.frame1, text="Mile").grid(row=0, column=1)
        ttk.Label(self.frame1, text="KM").grid(row=0, column=4, padx=5)
        ttk.Button(self.frame1, text="\N{RIGHTWARDS BLACK ARROW}", command=self.compute).grid(row=0, column=2, padx=5, sticky='e')
        self.output_entry = ttk.Label(self.frame1)
    
    def compute(self):
        x1 = self.number_entry.get()
        result = float(x1) * 1.609344    
        self.output_entry.configure(text=str(round(result,2)))
        self.output_entry.grid(row=0, column=3, padx=5)
        
     
            
def main():
    main_window = Tk()
    form = Form(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
