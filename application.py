import tkinter as tk


class Application:
    def __init__(self):
        self.win = tk.Tk()
        self.text = tk.Text(self.win)
        self._widgets_styling()
        self.win.mainloop()

    def _widgets_styling(self):
        ##
        # Style widgets
        ##
        self.win.geometry("800x800")
        self.win.title("Text Analyzer")
        self.win.iconbitmap(default="icons/text_analyzer.ico")


app = Application()


