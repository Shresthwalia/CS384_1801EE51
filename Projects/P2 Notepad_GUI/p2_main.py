import pathlib
import datetime
import tkinter as tk
from tkinter import Event, font as tkfont
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from tkinter import ttk


class Find(tk.Toplevel):
    """Find whole or partial words within a text widget"""

    def __init__(self, master, text_widget):
        super().__init__(master)
        self.text = text_widget
        self.title('Find')
        self.transient(master)
        self.resizable(False, False)
        self.wm_attributes('-topmost', 'true', '-toolwindow', 'true')
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.focus_set()

        # create widgets
        lbl = tk.Label(self, text='Find what:')
        self.text_find = tk.Entry(self, width=30, font='-size 10')
        self.btn_next = tk.Button(
            self, text='Find Next', width=10, command=self.ask_find_match)
        self.whole_word_var = tk.IntVar()
        self.whole_word_var.set(0)
        check_btn = tk.Checkbutton(
            self,
            text='Match whole word only',
            variable=self.whole_word_var, anchor=tk.W, command=self.change_match_type)

        # add widgets to window
        lbl.grid(row=0, column=0, padx=(15, 2), pady=15)
        self.text_find.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=15)
        self.btn_next.grid(row=0, column=2, sticky=tk.EW,
                           padx=(5, 15), pady=15)
        self.text_find.focus_set()
        check_btn.grid(row=1, column=0, padx=15, pady=(
            5, 15), columnspan=2, sticky=tk.EW)

        # other variables
        self.chars = 0
        self.term = None
        self.start = '1.0'

        # configure text widget tags
        self.text.tag_configure(
            'found', foreground='black', background='silver')
        self.text.tag_configure(
            'found.focus', foreground='white', background='SystemHighlight')

        # add additional bindings
        self.bind("<Return>", self.ask_find_match)

    def cancel(self):
        """Cancel the request and return control to main window"""
        end = self.start
        start = self.start + f'-{self.chars}c'
        self.text.tag_delete('found', 1.0, tk.END)
        self.text.tag_delete('found.focus', 1.0, tk.END)
        self.text.tag_add(tk.SEL, start, end)
        self.text.mark_set(tk.INSERT, start)
        self.text.focus_set()
        self.destroy()

    def change_match_type(self):
        """Reset found tags when match type is changed"""
        self.term = None
        self.chars = None
        self.text.tag_remove('found', '1.0', tk.END)
        self.text.tag_remove('found.focus', '1.0', tk.END)

    def ask_find_match(self, event=None):
        """Check for new searches, and route traffic by search types"""
        term = self.text_find.get()
        if term == '':
            return
        if self.term != term:
            self.term = term
            self.chars = len(term)
            self.text.tag_remove('found', '1.0', tk.END)
            self.route_match()
        self.highlight_next_match()

    def route_match(self):
        """Direct to whole or partial match"""
        if self.whole_word_var.get():
            self.whole_word_matches()
        else:
            self.partial_word_matches()

    def whole_word_matches(self):
        """Locate and tag all whole word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + ' wordend'
            # whole word includes a space before
            found = self.text.get(start + '-1c', end)
            if found == ' ' + self.term:
                self.text.tag_add('found', start, end)
            start = end

    def partial_word_matches(self):
        """Locate and tag all partial word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + f'+{self.chars}c'
            self.text.tag_add('found', start, end)
            start = end

    def highlight_next_match(self):
        """Highlight the next matching word"""
        self.text.tag_remove('found.focus', '1.0',
                             tk.END)  # remove existing tag
        try:
            start, end = self.text.tag_nextrange('found', self.start, tk.END)
            self.text.tag_add('found.focus', start, end)
            self.text.mark_set(tk.INSERT, start)
            self.text.see(start)
            self.start = end
        except ValueError:
            if self.start != '1.0':
                self.start = '1.0'
                self.text.see('1.0')
                self.highlight_next_match()


class Replace(tk.Toplevel):
    """Find and replace words within a text widget"""

    def __init__(self, master, text_widget):
        super().__init__(master)
        self.text = text_widget
        self.title('Find and Replace')
        self.transient(master)
        self.resizable(False, False)
        self.wm_attributes('-topmost', 'true', '-toolwindow', 'true')
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.focus_set()

        # create widgets
        lbl1 = tk.Label(self, text='Find what:', anchor=tk.W)
        self.text_find = tk.Entry(self, width=30, font='-size 10')
        self.text_find.focus_set()
        self.btn_next = tk.Button(
            self, text='Find Next', width=12, command=self.ask_find_match)

        lbl2 = tk.Label(self, text='Replace with:', anchor=tk.W)
        self.text_replace = tk.Entry(self, width=30, font='-size 10')
        self.btn_replace = tk.Button(
            self, text='Replace', width=12, command=self.find_replace_next)
        self.btn_replace_all = tk.Button(
            self, text='Replace All', width=12, command=self.find_replace_all)

        self.whole_word_var = tk.IntVar()
        self.whole_word_var.set(0)
        check_btn = tk.Checkbutton(
            self,
            text='Match whole word only',
            variable=self.whole_word_var, anchor=tk.W, command=self.change_match_type)

        # add widgets to window
        lbl1.grid(row=0, column=0, sticky=tk.EW, padx=(15, 2), pady=(15, 0))
        lbl2.grid(row=1, column=0, sticky=tk.EW, padx=(15, 2))
        self.text_find.grid(row=0, column=1, sticky=tk.EW,
                            padx=5, pady=(15, 2))
        self.text_replace.grid(row=1, column=1, sticky=tk.EW, padx=5)
        self.btn_next.grid(row=0, column=2, sticky=tk.EW,
                           padx=(5, 15), pady=(15, 2))
        self.btn_replace.grid(
            row=1, column=2, sticky=tk.EW, padx=(5, 15), pady=2)
        self.btn_replace_all.grid(
            row=2, column=2, sticky=tk.EW, padx=(5, 15), pady=(2, 15))
        check_btn.grid(row=2, column=0, columnspan=2,
                       sticky=tk.EW, padx=15, pady=(5, 15))

        # other variables
        self.chars = 0
        self.term = None
        self.start = '1.0'

        # configure text widget tags
        self.text.tag_configure(
            'found', foreground='black', background='silver')
        self.text.tag_configure(
            'found.focus', foreground='white', background='SystemHighlight')

        # add additional bindings
        self.bind("<Return>", self.ask_find_match)

    def cancel(self):
        """Cancel the request and return control to main window"""
        end = self.start
        start = self.start + f'-{self.chars}c'
        self.text.tag_delete('found', 1.0, tk.END)
        self.text.tag_delete('found.focus', 1.0, tk.END)
        self.text.tag_add(tk.SEL, start, end)
        self.text.mark_set(tk.INSERT, start)
        self.text.focus_set()
        self.destroy()

    def change_match_type(self):
        """Reset found tags when match type is changed"""
        self.term = None
        self.chars = None
        self.text.tag_remove('found', '1.0', tk.END)
        self.text.tag_remove('found.focus', '1.0', tk.END)

    def ask_find_match(self, event=None):
        """Check for new searches, and route traffic by search types"""
        term = self.text_find.get()
        if term == '':
            return
        if self.term != term:
            self.term = term
            self.chars = len(term)
            self.text.tag_remove('found', '1.0', tk.END)
            self.route_match()
        self.highlight_next_match()

    def route_match(self):
        """Direct to whole or partial match"""
        if self.whole_word_var.get():
            self.whole_word_matches()
        else:
            self.partial_word_matches()

    def whole_word_matches(self):
        """Locate and tag all whole word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + ' wordend'
            # whole word includes a space before
            found = self.text.get(start + '-1c', end)
            if found == ' ' + self.term:
                self.text.tag_add('found', start, end)
            start = end

    def partial_word_matches(self):
        """Locate and tag all partial word matches"""
        start = '1.0'
        while True:
            start = self.text.search(self.term, start, stopindex=tk.END)
            if not start:
                break
            end = start + f'+{self.chars}c'
            self.text.tag_add('found', start, end)
            start = end

    def highlight_next_match(self):
        """Highlight the next matching word"""
        self.text.tag_remove('found.focus', '1.0',
                             tk.END)  # remove existing tag
        try:
            start, end = self.text.tag_nextrange('found', self.start, tk.END)
            self.text.tag_add('found.focus', start, end)
            self.text.mark_set(tk.INSERT, start)
            self.text.see(start)
            self.start = end
        except ValueError:
            if self.start != '1.0':
                self.start = '1.0'
                self.text.see('1.0')
                self.highlight_next_match()

    def find_replace_next(self):
        """Find the next available match and replace it"""
        old_term = self.text_find.get()
        new_term = self.text_replace.get()
        idx = '1.0'
        #start = self.text.search(old_term, tk.INSERT, tk.END)
        idx = self.text.search(old_term, idx, nocase=1,
                               stopindex=tk.END)
        lastidx = '% s+% dc' % (idx, len(old_term))
        try:
            #self.text.replace(start, start + ' wordend', new_term)
            self.text.delete(idx, lastidx)
            self.text.insert(idx, new_term)
            self.highlight_next_match()
        except tk.TclError:
            return

    def find_replace_all(self):
        """Find all matches and replace"""
        old_term = self.text_find.get()
        new_term = self.text_replace.get()
        while True:
            idx = '1.0'
            idx = self.text.search(old_term, idx, nocase=1,
                                   stopindex=tk.END)
            lastidx = '% s+% dc' % (idx, len(old_term))
            #start = self.text.search(old_term, '1.0', tk.END)
            if not idx:
                break
            #self.text.replace(start, start + ' wordend', new_term)
            self.text.delete(idx, lastidx)
            self.text.insert(idx, new_term)


class StatusBar(tk.Frame):
    """Status bar that shows text widget statistics"""

    def __init__(self, master, text_widget):
        super().__init__(master, relief=tk.SUNKEN, bd=1)
        self.master = master
        self.text = text_widget
        ttk.Separator(self).pack(fill=tk.X, expand=tk.YES)

        # Line Index
        self.line_var = tk.StringVar()
        self.line_var.set('1')
        tk.Label(self, text='Line:', anchor=tk.W).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.line_var,
                 anchor=tk.W).pack(side=tk.LEFT)

        # Column Index
        self.col_var = tk.StringVar()
        self.col_var.set('0')
        tk.Label(self, text='Col:', anchor=tk.W).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.col_var,
                 anchor=tk.W).pack(side=tk.LEFT)

        # Character Count
        self.char_var = tk.StringVar()
        self.char_var.set('0')
        tk.Label(self, text='Chars:', anchor=tk.W).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.char_var,
                 anchor=tk.W).pack(side=tk.LEFT)

        # Word Count
        self.word_var = tk.StringVar()
        self.word_var.set('0')
        tk.Label(self, text='Words:', anchor=tk.W).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.word_var,
                 anchor=tk.W).pack(side=tk.LEFT)

        # Event binding
        self.text.bind("<KeyRelease>", self.update_status)
        self.text.bind("<ButtonRelease-1>", self.update_status)
        self.update_status()  # set initial status
        self.pack(side=tk.BOTTOM, fill=tk.X, padx=2, pady=2)

    def update_status(self, event=None):
        """Update Status Bar"""
        line, col = self.text.index(tk.INSERT).split('.')
        self.line_var.set(line)
        self.col_var.set(col)

        raw_text = self.text.get('1.0', tk.END)
        spaces = raw_text.count(' ')

        char_count = "{:,d}".format(len(raw_text)-spaces)
        self.char_var.set(char_count)

        word_list = [char for char in raw_text.split(
            ' ') if char not in (' ', '', '\n')]
        word_count = "{:,d}".format(len(word_list))
        self.word_var.set(word_count)


class Notepad(tk.Tk):
    """A notepad application"""

    def __init__(self):
        super().__init__()
        self.withdraw()

        # check platform & set zoom status
        platform = self.tk.call('tk', 'windowingsystem')
        self.wm_state('zoomed') if platform == 'win32' else self.attributes(
            '-zoomed', 1)

        # file variables
        self.file = pathlib.Path.cwd() / 'untitled.txt'
        self.file_defaults = {
            'defaultextension': '*',
            'filetypes': [('All Files', '.*')]}

        # find search replace variables
        self.query = None
        self.matches = None
        self.findnext = None
        self.findreplace = None

        # main menu setup
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.menu_file = tk.Menu(self.menu, tearoff=False)
        self.menu_edit = tk.Menu(self.menu, tearoff=False)

        # file menu
        self.menu_file.add_command(
            label='New', accelerator='Ctrl+N', command=self.new_file)
        self.menu_file.add_command(
            label='Open...', accelerator='Ctrl+O', command=self.open_file)
        self.menu_file.add_command(
            label='Save', accelerator='Ctrl+S', command=self.save_file)
        self.menu_file.add_command(
            label='Save As...', accelerator='Ctrl+Shift+S', command=self.save_file_as)

        # edit menu
        self.menu_edit.add_command(
            label='Undo', accelerator='Ctrl+Z', command=self.undo_edit)
        self.menu_edit.add_command(
            label='Redo', accelerator='Ctrl+Y', command=self.redo_edit)
        self.menu_edit.add_command(
            label='Cut', accelerator='Ctrl+X', command=self.text_cut)
        self.menu_edit.add_command(
            label='Copy', accelerator='Ctrl+C', command=self.text_copy)
        self.menu_edit.add_command(
            label='Paste', accelerator='Ctrl+V', command=self.text_paste)
        self.menu_edit.add_command(
            label='Find', accelerator='Ctrl+F', command=self.ask_find_next)
        self.menu_edit.add_command(
            label='Find and Replace', accelerator='Ctrl+H', command=self.ask_find_replace)
        self.menu_edit.add_command(
            label='Time/Date', accelerator='F5', command=self.get_datetime)
        
        # general callback binding
        self.bind("<Control-n>", self.new_file)
        self.bind("<Control-o>", self.open_file)
        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-S>", self.save_file_as)
        self.bind("<Control-f>", self.ask_find_next)
        self.bind("<Control-h>", self.ask_find_replace)
        self.bind("<F5>", self.get_datetime)

        # add cascading menus to main menu
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu.add_cascade(label='Edit', menu=self.menu_edit)

        # setup text text widget
        self.text_frame = tk.Frame(self)
        self.text = ScrolledText(self.text_frame, wrap=tk.WORD, font='-size 14', undo=True, maxundo=10,
                                 autoseparator=True, blockcursor=False, padx=5, pady=10)

        # set default tab size to 4 characters
        self.font = tkfont.Font(family='Courier New', size=12, weight=tkfont.NORMAL,
                                slant=tkfont.ROMAN, underline=False, overstrike=False)
        self.text.configure(font=self.font)
        tab_width = self.font.measure(' ' * 4)
        self.text.configure(tabs=(tab_width,))
        self.text.insert(tk.END, self.file.read_text()
                         if self.file.is_file() else '')

        # pack all widget to screen
        self.text.pack(fill=tk.BOTH, expand=tk.YES)
        self.text_frame.pack(fill=tk.BOTH, expand=tk.YES)

        # add status bar
        self.status_bar = StatusBar(self, self.text)

        # final setup
        self.update_title()

        #self.eval('tk::PlaceWindow . center')
        self.deiconify()

    # ---FILE MENU CALLBACKS------------------------------------------------------------------------

    def new_file(self, event=None):
        """Create a new file"""
        # check for content change before opening new file
        self.confirm_changes()

        # reset text widget
        self.text.delete(1.0, tk.END)
        self.file = pathlib.Path.cwd() / 'untitled.txt'
        self.update_title()

    def open_file(self, event=None):
        """Open an existing file"""
        # check for content change before opening new file
        self.confirm_changes()

        # open new file
        file = filedialog.askopenfilename(
            initialdir=self.file.parent, **self.file_defaults)
        if file:
            self.text.delete(1.0, tk.END)  # delete existing content
            self.file = pathlib.Path(file)
            self.text.insert(tk.END, self.file.read_text())
            self.update_title()
            self.status_bar.update_status()

    def save_file(self, event=None):
        """Save the currently open file"""
        if self.file.name == 'untitled.txt':
            file = filedialog.asksaveasfilename(
                initialfile=self.file, **self.file_defaults)
            self.file = pathlib.Path(file) if file else self.file
        self.file.write_text(self.text.get(1.0, tk.END))
        self.update_title()

    def save_file_as(self, event=None):
        """Save the currently open file with a different name or location"""
        file = filedialog.asksaveasfilename(
            initialdir=self.file.parent, **self.file_defaults)
        if file:
            self.file = pathlib.Path(file)
            self.file.write_text(self.text.get(1.0, tk.END))
            self.update_title()

    def confirm_changes(self):
        """Check to see if content has changed from original file; if so, confirm save"""
        if self.file.is_file():
            original = self.file.read_text()
            current = self.text.get(1.0, tk.END)
            if original != current:
                confirm = messagebox.askyesno(
                    message="Save current file changes?")
                if confirm:
                    self.save_file()
        # new unsaved document with content is prompted to save
        elif self.text.count(1.0, tk.END)[0] > 1:
            confirm = messagebox.askyesno(message="Save current document?")
            if confirm:
                self.save_file()

    def update_title(self):
        """Update the title with the file name"""
        self.title(self.file.name + " - Notepad")

    # ---EDIT MENU CALLBACKS------------------------------------------------------------------------

    def undo_edit(self):
        """Undo the last edit in the stack"""
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo_edit(self):
        """Redo the last edit in the stack"""
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def text_copy(self):
        """Append selected text to the clipboard"""
        selected = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.clipboard_clear()
        self.text.clipboard_append(selected)

    def text_paste(self):
        """Paste clipboard text into text widget at cursor"""
        self.text.insert(tk.INSERT, self.text.clipboard_get())

    def text_cut(self):
        """Cut selected text and append to clipboard"""
        selected = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.clipboard_clear()
        self.text.clipboard_append(selected)

    def quit_application(self, event=None):
        """Quit application after checking for user changes"""
        self.confirm_changes()
        self.destroy()

    def ask_find_next(self, event=None):
        """Create find next popup widget"""
        self.findnext = Find(self, self.text)

    def ask_find_replace(self, event=None):
        """Create replace popup widget"""
        self.findreplace = Replace(self, self.text)

    def get_datetime(self, event=None):
        """insert date and time at cursor position"""
        self.text.insert(tk.INSERT, datetime.datetime.now().strftime("%c"))


if __name__ == '__main__':
    notepad = Notepad()
    notepad.mainloop()
