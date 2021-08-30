# ToDo list
from tkinter import *


class Window:
    def __init__(self, width, height, x, y, title, resizable=(False, False), icon=None):
        self.white = '#fff'
        self.bt_bg = '#8D4AEA'
        self.input_bg = '#F3F1F4'

        self.root = Tk()
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)
        self.root['bg'] = self.white

    def draw_widget(self):
        def bt_add_press():
            e_text = e_input.get()
            if e_text:
                l_list.insert(END, e_text)
                e_input.delete(0, END)

        def bt_delete_press():
            selected = l_list.curselection()
            l_list.delete(selected)

        def bt_clear_press():
            l_list.delete(0, END)

        # ======== Label ==========
        l_title = Label(self.root, text='ToDo List', font='ComicSansMs 18', bg=self.white)
        l_title.place(x=250, y=0)

        list_title = Label(self.root, text='Tasks:', font='ComicSansMs 14', bg=self.white)
        list_title.place(x=10, y=30)

        list_title = Label(self.root, text='New Task:', font='ComicSansMs 14', bg=self.white)
        list_title.place(x=10, y=340)

        # ======== Input ==========
        l_list = Listbox(self.root, width=55, height=14, font='ComicSansMs 12', bg=self.input_bg)
        l_list.place(x=10, y=60)

        e_input = Entry(self.root, width=55, font='ComicSansMs 12', bd=1, bg=self.input_bg)
        e_input.place(x=10, y=370)

        # ======== Button ==========
        bt_delete = Button(self.root, text='Delete', command=bt_delete_press, bg=self.bt_bg, fg=self.white, bd=0,
                           font='ComicSansMS 12')
        bt_delete.place(x=525, y=60)

        bt_clear = Button(self.root, text='Clear', command=bt_clear_press, bg=self.bt_bg, fg=self.white, bd=0,
                           font='ComicSansMS 12')
        bt_clear.place(x=525, y=95)

        bt_add = Button(self.root, text='Add', command=bt_add_press, bg=self.bt_bg, fg=self.white, bd=0,
                           font='ComicSansMS 12')
        bt_add.place(x=525, y=366)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(600, 410, 400, 120, 'ToDo List')
    window.draw_widget()
    window.run()
