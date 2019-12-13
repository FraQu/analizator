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
        self.scrollbar_text = tk.Scrollbar(self.win)
        self.scrollbar_text.place(in_=self.text, relx=1., rely=0, relheight=1.)
        self.scrollbar_text.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar_text.set)
        self.text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)


app = Application()


