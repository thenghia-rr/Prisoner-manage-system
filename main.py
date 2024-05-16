from tkinter import *
import src.login as login


def main():
    root = Tk()
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    # root.geometry(f"{screen_width}x{screen_height}+0+0")
    icon = PhotoImage(file='img/icon_prison.png')
    root.iconphoto(False, icon)

    root.title("Prisoner Management System")
    root.geometry(f"1400x760")
    root.resizable(False, True)
    login.Login(root)

    root.mainloop()


if __name__ == '__main__':
    main()
