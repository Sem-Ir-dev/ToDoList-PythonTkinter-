from tkinter import *
from tkinter import messagebox


class Window:
    def __init__(self, width, height, x, y, title, resizable=(False, False), icon=None):
        self.white = '#fff'
        self.bt_bg = '#8D4AEA'
        self.input_bg = '#F3F1F4'
        self.sel_bg = '#CBCACC'

        self.root = Tk()
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)
        self.root['bg'] = self.white

    def draw_widget(self):
        def makebt(text, cmd):
            return Button(self.root, text=text, command=cmd, bg=self.bt_bg, fg=self.white, bd=0, font='ComicSansMS 12',
                          width=6)

        def bt_add_press(event=None):
            try:
                if event.char == '\r':
                    e_text = e_input.get()
                    if e_text:
                        l_list.insert(END, e_text)
                        e_input.delete(0, END)
            except AttributeError:
                e_text = e_input.get()
                if e_text:
                    l_list.insert(END, e_text)
                    e_input.delete(0, END)

        def bt_delete_press():
            try:
                selected = l_list.curselection()
                l_list.delete(selected)
            except TclError:
                pass

        def bt_clear_press():
            l_list.delete(0, END)

        def bt_save_press():
            text = l_list.get(0, END)

            with open('saved.txt', 'w') as f:
                for i in text:
                    f.write(str(i) + '\n')

            messagebox.showinfo('Info', 'Saved')

        def bt_open_press():
            try:
                f = open('saved.txt', 'r')
                l_list.delete(0, END)

                for line in f:
                    l_list.insert(END, line)
            except FileNotFoundError:
                messagebox.showerror('FileNotFound', 'File "saved.txt" not found in directory')

        # ======== Label ==========
        l_title = Label(self.root, text='ToDo List', font='ComicSansMs 18', bg=self.white)
        l_title.place(x=250, y=0)

        list_title = Label(self.root, text='Tasks:', font='ComicSansMs 14', bg=self.white)
        list_title.place(x=10, y=30)

        list_title = Label(self.root, text='New Task:', font='ComicSansMs 14', bg=self.white)
        list_title.place(x=10, y=340)

        # ======== Input ==========
        l_list = Listbox(self.root, width=55, height=14, font='ComicSansMs 13', bg=self.input_bg,
                         selectbackground=self.sel_bg, selectforeground='#000')
        l_list.place(x=10, y=60)

        e_input = Entry(self.root, width=55, font='ComicSansMs 12', bd=1, bg=self.input_bg)
        e_input.place(x=10, y=370)
        e_input.bind('<Key>', bt_add_press)

        # ======== Button ==========
        bt_delete = makebt('Delete', bt_delete_press)
        bt_delete.place(x=525, y=60)

        bt_clear = makebt('Clear', bt_clear_press)
        bt_clear.place(x=525, y=95)

        bt_save = makebt('Save', bt_save_press)
        bt_save.place(x=525, y=130)

        bt_open = makebt('Open', bt_open_press)
        bt_open.place(x=525, y=165)

        bt_add = makebt('Add', bt_add_press)
        bt_add.place(x=525, y=366)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(600, 410, 390, 160, 'ToDo List')
    window.draw_widget()
    window.run()
