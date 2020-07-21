import tkinter as tk
import keyboard
from extract import Extract, OCRFailed

class ResultList(tk.Listbox):
    def __init__(self, parent, *args, **kwargs):
        tk.Listbox.__init__(self, parent, *args, **kwargs)
        self.extract = Extract()
        self.index = 1
    
    def paste(self):
        try:
            self.extract.clipboardToImage()
            self.extract.imageToText()
            self.extract.textToClipboard(self.extract.result)
            self.updateEntry(self.extract.result)
        except OCRFailed:
            pass
        except AttributeError:
            pass

    def updateEntry(self, data):
        self.insert(self.index, data)
        self.index += 1

    def onSelect(self, evt):
        try:
            self.extract.textToClipboard(self.get(self.curselection()[0]))
        except IndexError:
            pass

class Menu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="Settings", command=)
        self.add_cascade(label="File", menu=filemenu)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, width=800, height=600, **kwargs):
        parent.geometry(f"{width}x{height}")
        parent.resizable(False, False)
        
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.menu = Menu(self)
        parent.config(menu=self.menu)

        self.resultlist = ResultList(self)
        self.resultlist.pack(side="bottom", fill="both", expand=True)
        self.resultlist.bind("<<ListboxSelect>>", self.resultlist.onSelect)

        keyboard.add_hotkey("Ctrl+Shift+V", lambda: self.resultlist.paste())

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
