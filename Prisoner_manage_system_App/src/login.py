from tkinter import *
from tkinter import messagebox
import json
import re
import src.admin as admin
import src.user as user

PRIMARY_COLOR = '#5856a0'
account_file = 'data/account.json'

class Login:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()
        self.re_password = StringVar()  # Add re_password for registration
        self.role = StringVar()

        self.username.set('admin')
        self.password.set('admin')

        # Background Color
        self.root.config(bg=PRIMARY_COLOR)

        # Call the login interface creation method
        self.loginControlFrame()

    """CTA Methods"""

    # Login function to navigate to the next frames
    def loginFunc(self):
        with open(account_file, 'r') as f:
            accounts = json.load(f)

        for account in accounts:
            if self.txtUsername.get() == account['username'] and self.txtPassword.get() == account['password']:
                if account['role'] == 'admin':
                    self.role = "admin"
                    self.loginFrame.destroy()
                    self.rightFrame.destroy()
                    admin.AdminControls(self.root, account['role'])
                    return
                elif account['role'] == 'user':
                    self.role = "user"
                    self.loginFrame.destroy()
                    self.rightFrame.destroy()
                    name_user = account['username']
                    user.UserControls(self.root, name_user, account['role'])
                    return
        
        messagebox.showerror("Lỗi xác thực!", "Không tìm thấy tài khoản hoặc thông tin không chính xác")
        self.username.set("")
        self.password.set("")

    # Register function to create a new user account
    def registerFunc(self):
        username = self.regUsername.get()
        password = self.regPassword.get()
        re_password = self.regRePassword.get()

        if not re.match("^[a-zA-Z0-9_]+$", username):
            messagebox.showerror("Invalid Username", "Tên người dùng chỉ được chứa các chữ cái, số và dấu gạch dưới!")
            return
        if len(password) < 5:
            messagebox.showerror("Invalid Password", "Chiều dài mật khẩu tối thiểu là 5")
            return
        if password != re_password:
            messagebox.showerror("Password Mismatch", "Mật khẩu không khớp")
            return

        with open(account_file, 'r+') as f:
            accounts = json.load(f)
            new_id = str(int(accounts[-1]['id']) + 1 if 'id' in accounts[-1] else len(accounts) + 1)
            new_account = {
                'id': new_id,
                'username': username,
                'password': password,
                'role': 'user'
            }
            accounts.append(new_account)
            f.seek(0)
            json.dump(accounts, f, indent=4)

        messagebox.showinfo("Success", "Tạo tài khoản thành công!")
        self.registerFrame.destroy()
        self.rightFrame.destroy()  # Ensure rightFrame is destroyed
        self.loginControlFrame()

    """Login Frame"""

    def loginControlFrame(self):
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)
        self.login_frame_title = Label(self.loginFrame, text="WELCOME BACK", font=("Impact", 35), bg="white",
                                       fg=PRIMARY_COLOR)
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.labelUsername = Label(self.loginFrame, text="Username", font=("Tahoma", 14, "bold"), bg="white",
                                   fg=PRIMARY_COLOR)
        self.labelUsername.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Courier", 13), width=30,
                                 bd=5)
        self.txtUsername.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.labelPassword = Label(self.loginFrame, text="Password", font=("Tahoma", 14, "bold"), bg="white",
                                   fg=PRIMARY_COLOR)
        self.labelPassword.grid(row=2, column=0, padx=10, pady=15, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Courier", 13), width=30,
                                 bd=5, show="*")
        self.txtPassword.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.btnLogin = Button(self.loginFrame, text="Login", bd=0, cursor="hand2",
                               fg="white", bg=PRIMARY_COLOR, width=10, font=("Impact", 15), command=self.loginFunc)
        self.btnLogin.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        self.btnRegister = Button(self.loginFrame, text="Register", bd=0, cursor="hand2",
                                  fg="white", bg=PRIMARY_COLOR, width=10, font=("Impact", 15), command=self.registerControlFrame)
        self.btnRegister.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.rightFrame = Frame(self.root, bg=PRIMARY_COLOR)
        self.rightFrame.pack(side=RIGHT)

        self.labelHeroName = Label(self.rightFrame, text="Hệ Thống Quản Lí Phạm Nhân", font=("Tahoma", 36, "bold"),
                                      bg=PRIMARY_COLOR,
                                      fg="white")
        self.labelHeroName.grid(row=0, column=2, columnspan=2, padx=10)
        self.labelDesc = Label(self.rightFrame, text="Hãy đảm bảo an toàn và trật tự!", font=("Courier New", 25, "italic",),
                               bg=PRIMARY_COLOR,
                               fg="white",
                               )
        self.labelDesc.grid(row=1, column=2, columnspan=2, padx=10, pady=9)

        img_flag_vn = PhotoImage(file='img/flag_vn.png')
        self.flagVN = Label(self.rightFrame, image=img_flag_vn, bg=PRIMARY_COLOR)
        self.flagVN.image = img_flag_vn  # Giữ tham chiếu đến ảnh
        self.flagVN.grid(row=2, column=2, columnspan=2, padx=10, pady=9)
        
        

    """Register Frame"""

    def registerControlFrame(self):
        self.loginFrame.destroy()
        self.rightFrame.destroy()  # Ensure rightFrame is destroyed

        self.registerFrame = Frame(self.root, bg="white")
        self.registerFrame.pack(side=LEFT, fill=X, padx=60)

        self.register_frame_title = Label(self.registerFrame, text="REGISTER ACCOUNT", font=("Impact", 30), bg="white",
                                          fg=PRIMARY_COLOR)
        self.register_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.labelRegUsername = Label(self.registerFrame, text="Username", font=("Tahoma", 14, "bold"), bg="white",
                                      fg=PRIMARY_COLOR)
        self.labelRegUsername.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.regUsername = Entry(self.registerFrame, font=("Courier", 13), width=30, bd=5)
        self.regUsername.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.labelRegPassword = Label(self.registerFrame, text="Password", font=("Tahoma", 14, "bold"), bg="white",
                                      fg=PRIMARY_COLOR)
        self.labelRegPassword.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.regPassword = Entry(self.registerFrame, font=("Courier", 13), width=30, bd=5, show="*")
        self.regPassword.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.labelRegRePassword = Label(self.registerFrame, text="Re-Password", font=("Tahoma", 14, "bold"), bg="white",
                                        fg=PRIMARY_COLOR)
        self.labelRegRePassword.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.regRePassword = Entry(self.registerFrame, font=("Courier", 13), width=30, bd=5, show="*")
        self.regRePassword.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.btnCreateAccount = Button(self.registerFrame, text="Create Account", bd=0, cursor="hand2",
                                       fg="white", bg=PRIMARY_COLOR, width=15, font=("Impact", 15), command=self.registerFunc)
        self.btnCreateAccount.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        self.btnBackToLogin = Button(self.registerFrame, text="Back to Login", bd=0, cursor="hand2",
                                     fg="white", bg=PRIMARY_COLOR, width=15, font=("Impact", 15), command=self.backToLogin)
        self.btnBackToLogin.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.rightFrame = Frame(self.root, bg=PRIMARY_COLOR)
        self.rightFrame.pack(side=RIGHT)

        self.labelHeroName = Label(self.rightFrame, text="Hệ Thống Quản Lí Phạm Nhân", font=("Tahoma", 36, "bold"),
                                      bg=PRIMARY_COLOR,
                                      fg="white")
        self.labelHeroName.grid(row=0, column=2, columnspan=2, padx=10)
        self.labelDesc = Label(self.rightFrame, text="Vì một xã hội văn minh!", font=("Courier New", 25, "italic"),
                               bg=PRIMARY_COLOR,
                               fg="white")
        self.labelDesc.grid(row=1, column=2, columnspan=2, padx=10, pady=9)

        img_bualiem = PhotoImage(file='img/bualiem.png')
        self.dangKyDCS = Label(self.rightFrame, image=img_bualiem, bg=PRIMARY_COLOR)
        self.dangKyDCS.image = img_bualiem  # Giữ tham chiếu đến ảnh
        self.dangKyDCS.grid(row=2, column=2, columnspan=2, padx=10, pady=9)


    def backToLogin(self):
        self.registerFrame.destroy()
        self.rightFrame.destroy()  # Ensure rightFrame is destroyed
        self.loginControlFrame()


