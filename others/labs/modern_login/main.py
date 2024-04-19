from tkinter import *


# class

class App:
    def __init__(self):
        # window

        self.main = Tk()
        self.main.geometry('430x500')
        self.main.title('Modern Login')

        # images

        self.user_image = PhotoImage(file='./images/user.png')
        self.password_image = PhotoImage(file='./images/password.png')

        self.login_ui()

        self.main.mainloop()

    def login_ui(self):

        # entry

        user_entry = Entry(self.main, borderwidth=1, highlightthickness=0)

        pass_entry = Entry(self.main, borderwidth=1, highlightthickness=0)

        # place

        user_entry.place(x=130, y=30)
        pass_entry.place(x=130, y=100)

    def new_user_ui(self):
        pass


if __name__ == '__main__':
    App()
