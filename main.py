# ToDo list
from tkinter import *


class Window:
    def __init__(self, width, height, x, y, title, resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)

    def draw_widget(self):
        def bt_add():
            e_text = e_input.get()
            if e_text:
                l_list.insert(END, e_text)
                e_input.delete(0, END)

        def bt_delete():
            selected = l_list.curselection()
            l_list.delete(selected)

        # ======== Label ==========
        l_title = Label(self.root, text='ToDo List', font='Arial 18')
        l_title.place(x=250, y=0)

        list_title = Label(self.root, text='Tasks:', font='Arial 14')
        list_title.place(x=10, y=30)

        list_title = Label(self.root, text='New Task:', font='Arial 14')
        list_title.place(x=10, y=340)

        # ======== Input ==========
        l_list = Listbox(self.root, width=55, height=14, font='Arial 12')
        l_list.place(x=10, y=60)

        e_input = Entry(self.root, width=55, font='Arial 12')
        e_input.place(x=10, y=370)

        # ======== Button ==========
        bt_delete = Button(self.root, text='Delete', command=bt_delete)
        bt_delete.place(x=525, y=60)

        bt_add = Button(self.root, text='Add', command=bt_add)
        bt_add.place(x=525, y=366)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(600, 410, 400, 120, 'ToDo List')
    window.draw_widget()
    window.run()
