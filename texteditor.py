from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile


class TextEditor:
    def __init__(self, master):
        master.title ('Text Editor')
        master.resizable(False, False)
        self.text_editor = Text(master)
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()
        open_button = ttk.Button(self.frame1, text="Open", command=self.open)
        open_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        save_button= ttk.Button(self.frame1, text="Save as", command=self.saveas)
        save_button.grid(row=1, column=0, padx=5, sticky='e')
        self.frame1.grid(row=0, column=0, sticky="ns")
        self.text_editor.grid(row=0, column=1, sticky="nsew")
        self.label_file_explorer = Label(master, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4)
                        
    def open(self):
        file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
        if not file_path:
            return
        self.text_editor.delete("1.0", END)
        with open(file_path, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            self.text_editor.insert(END, text)
        
    
    def saveas(self):
        files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)        
        


def main():
    main_window = Tk()
    text_editor = TextEditor(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
