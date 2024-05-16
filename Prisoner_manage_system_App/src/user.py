from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
import json
import src.login as login
import src.laws as laws

PRIMARY_COLOR = "#5856a0"
file_json_prisoners = "data/prisoners.json"

class UserControls:
    def __init__(self, root, name_user, role):
        self.root = root
        self.name_user = name_user
        self.role = role

        # Local variables
        self.fullname = StringVar()
        self.date_of_birth = StringVar()
        self.gender = StringVar()
        self.nationality = StringVar()
        self.citizen_id = StringVar()
        self.hometown = StringVar()
        self.offense_type = StringVar()
        self.criminal_behaviors  = StringVar()

        self.userControlsFrame()
        self.userFrameButtons()
        self.tableOutputFrame()
    

    """Prisoner Info Entries Frame - Khung nhập thông tin phạm nhân"""
    def userControlsFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#5856a0")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.admin_frame_title = Label(self.entriesFrame, text="User Control Panel", font=("Arial", 35, 'bold'),
                                       bg="#5856a0",
                                       fg="white")
        self.admin_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # User image
        img_user = PhotoImage(file='img/user_icon.png')
        self.userImg = Label(self.entriesFrame, image=img_user, bg=PRIMARY_COLOR)
        self.userImg.image = img_user  # Giữ tham chiếu đến ảnh
        self.userImg.grid(row=0, column=2, padx=1, pady=9)

        # Welcome user
        self.labelNameUser = Label(self.entriesFrame, text=f"Welcome, {self.name_user}", font=("Courier", 15, "italic", "bold"), bg=PRIMARY_COLOR,
                                   fg="#C2C224")
        self.labelNameUser.grid(row=0, column=5)
        

        # Prisoner Name
        self.labelName = Label(self.entriesFrame, text="Họ Tên", font=("Calibri", 16, "bold"), bg="#5856a0",
                               fg="white")
        self.labelName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtName = Entry(self.entriesFrame, textvariable=self.fullname, font=("Calibri", 14), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Prisoner Gender
        self.labelGender = Label(self.entriesFrame, text="Giới Tính", font=("Calibri", 16, "bold"), bg="#5856a0",
                                 fg="white")
        self.labelGender.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.comboGender = ttk.Combobox(self.entriesFrame, textvariable=self.gender, font=("Calibri", 14),
                                        width=28,
                                        state="readonly")
        self.comboGender['values'] = ("Nam", "Nữ", "Khác")
        self.comboGender.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        # Prisoner date of birth
        self.labelDOB = Label(self.entriesFrame, text="Ngày Sinh", font=("Calibri", 16, "bold"), bg="#5856a0",
                                fg="white")
        self.labelDOB.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtDOB = Entry(self.entriesFrame, textvariable=self.date_of_birth, font=("Calibri", 14), width=30)
        # txtDOB.insert(0, "DD/MM/YYYY")
        # txtDOB.config(state="readonly")
        self.txtDOB.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Prisoner Nationality
        self.labelNationality = Label(self.entriesFrame, text="Quốc Tịch", font=("Calibri", 16, "bold"),
                                bg="#5856a0",
                                fg="white")
        self.labelNationality.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.txtNationality = Entry(self.entriesFrame, textvariable=self.nationality, font=("Calibri", 14), width=30)
        self.txtNationality.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        # Prisoner Citizen ID
        self.lableCitizenID = Label(self.entriesFrame, text="Số CCCD/CMND", font=("Calibri", 16, "bold"),
                                 bg="#5856a0",
                                 fg="white")
        self.lableCitizenID.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtCitizenID = Entry(self.entriesFrame, textvariable=self.citizen_id, font=("Calibri", 14), width=30)
        self.txtCitizenID.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Prisoner Hometown
        self.labelHometown = Label(self.entriesFrame, text="Quê Quán", font=("Calibri", 16, "bold"),
                                bg="#5856a0",
                                fg="white")
        self.labelHometown.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.txtHometown = Entry(self.entriesFrame, textvariable=self.hometown, font=("Calibri", 14),
                                 width=30,)
        self.txtHometown.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        # Prisoner Offense_type
        self.labelOffenseType = Label(self.entriesFrame, text="Loại tội phạm", font=("Calibri", 16, "bold"), bg="#5856a0",
                                 fg="white")
        self.labelOffenseType.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.comboOffenseType = ttk.Combobox(self.entriesFrame, textvariable=self.offense_type, font=("Calibri", 14),
                                        width=28,
                                        )

        self.comboOffenseType['values'] = ("Hình sự", "Dân sự", "Hành chính","Lao động", "Thuế", "Doanh nghiệp" ,'khác')
        self.comboOffenseType.grid(row=4, column=1, padx=10, pady=5, sticky="w")

         # Prisoner Criminal behaviors
        self.labelCrimimalBehavior = Label(self.entriesFrame, text="Hành vi phạm tội",
                                   font=("Calibri", 16, "bold"),
                                   bg="#5856a0",
                                   fg="white")
        self.labelCrimimalBehavior.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.txtCriminalBehavior = Text(self.entriesFrame, font=("Calibri", 14), width=44, height=5)
        # self.txtCriminalBehavior.insert('1.0', self.txt.get())
        self.txtCriminalBehavior.grid(row=4, column=3, columnspan=3, rowspan=6, padx=10, pady=5, sticky="w")

    """Sub Methods to be used in primary CTA methods"""
    def displaySelectedPrisoner(self, event):
        # Kiểm tra xem có mục nào được chọn không
        if not self.out.selection():
            return

        # Lấy ID của phạm nhân được chọn
        selected_item = self.out.selection()[0]
        # Lấy thông tin của phạm nhân từ Treeview
        prisoner_info = self.out.item(selected_item, 'values')
        
        # Xác định chỉ mục của cột chứa thông tin criminal_behaviors
        criminal_behaviors_index = self.out["columns"].index("9")
        # Lấy giá trị của cột criminal_behaviors từ hàng được chọn
        criminal_behaviors_value = prisoner_info[criminal_behaviors_index]

        # Hiển thị thông tin của phạm nhân lên các widget tương ứng trên form
        self.fullname.set(prisoner_info[1])
        self.date_of_birth.set(prisoner_info[2])
        self.gender.set(prisoner_info[3])
        self.nationality.set(prisoner_info[4])
        self.citizen_id.set(prisoner_info[5])
        self.hometown.set(prisoner_info[6])
        self.offense_type.set(prisoner_info[7])
        # Xóa nội dung hiện tại trong Text widget
        self.txtCriminalBehavior.delete('1.0', END)
        # Chèn nội dung mới vào Text widget
        self.txtCriminalBehavior.insert('1.0', criminal_behaviors_value)

    """ All method to manipulations with file json """
    # Method load list prisoners from json file
    def loadPrisonersJson(self): 
        try:
            with open(file_json_prisoners, "r", encoding="utf-8") as file:
                # Đọc dữ liệu từ file JSON
                data = json.load(file)

                # Xóa hết dữ liệu hiện tại trong Treeview
                self.out.delete(*self.out.get_children())

                # Hiển thị dữ liệu từ JSON lên Treeview
                for idx, prisoner in enumerate(data, start=1):
                    self.out.insert("", "end", values=(
                        idx,
                        prisoner["fullname"],
                        prisoner["date_of_birth"],
                        prisoner["gender"],
                        prisoner["nationality"],
                        prisoner["citizen_id"],
                        prisoner["hometown"],
                        prisoner["offense_type"],
                        prisoner["criminal_behaviors"]
                    ))
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy file JSON!")
        except json.JSONDecodeError:
            messagebox.showerror("Lỗi", "Lỗi khi đọc dữ liệu từ file JSON!")

    """CTA Methods"""
    # Method to display all Prisoners in the Treeview Frame
    def viewPrisoners(self):
        self.loadPrisonersJson()

     #  Method to refresh form Prisoner
    def resetForm(self):
        self.txtName.delete(0, END)
        self.txtDOB.delete(0, END)
        self.comboGender.set("")  # Assuming this is a Combobox widget
        self.txtNationality.delete(0, END)
        self.txtCitizenID.delete(0, END)
        self.txtHometown.delete(0, END)
        self.comboOffenseType.set("")  # Assuming this is a Combobox widget
        self.txtCriminalBehavior.delete('1.0', END)  # Assuming this is a Text widget

    # Method to search prisoner by Citizen ID
    def searchPrisonerByCitizenID(self):
        # Create a pop-up window to get the Citizen ID
        citizen_id = simpledialog.askstring("Tìm phạm nhân", "Nhập số CCCD/CMND:")

        if citizen_id:
            try:
                with open(file_json_prisoners, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    
                    # Search for the prisoner with the given Citizen ID
                    for prisoner in data:
                        if prisoner.get("citizen_id") == citizen_id:
                            # Display prisoner information in the Treeview
                            self.out.delete(*self.out.get_children())  # Clear existing data
                            self.out.insert("", "end", values=(
                                1,
                                prisoner["fullname"],
                                prisoner["date_of_birth"],
                                prisoner["gender"],
                                prisoner["nationality"],
                                prisoner["citizen_id"],
                                prisoner["hometown"],
                                prisoner["offense_type"],
                                prisoner["criminal_behaviors"]
                            ))
                            # Stop searching after finding the prisoner
                            break
                    else:
                        # Show a warning message if the prisoner is not found
                        messagebox.showwarning("Cảnh báo", f"Không tìm thấy phạm nhân với số CMND/CCCD: {citizen_id}")
            except FileNotFoundError:
                messagebox.showerror("Lỗi", "Không tìm thấy file JSON!")
            except json.JSONDecodeError:
                messagebox.showerror("Lỗi", "Lỗi khi đọc dữ liệu từ file JSON!")

    # Method to redirect the frame for LAWS API
    def viewLaws(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        laws.LawSession(self.root, self.name_user,  self.role)

    # Method to redirect to the login frame
    def logOut(self):
        confirm = messagebox.askokcancel("Xác nhận", "Bạn có chắc chắn muốn đăng xuất?")
        if confirm:
            self.entriesFrame.destroy()
            self.buttonsFrame.destroy()
            self.tableFrame.destroy()
            # messagebox.showinfo("Log out", "Đăng xuất thành công!")
            login.Login(self.root)

    """CTA Buttons Frame"""
    def userFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#5856a0")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        # Display List
        self.btnView = Button(self.buttonsFrame, command=self.viewPrisoners, text="Xem danh sách phạm nhân", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=22, font=("Arial", 15, "bold"))
        self.btnView.grid(row=0, column=0,  padx=10)

        # Refresh Form Prisoner
        self.btnRefresh = Button(self.buttonsFrame, command=self.resetForm, text="Reset Form", bd=0,
                             cursor="hand2",
                             bg="#EADDF7",
                             fg="#5856a0", width=15, font=("Arial", 15, "bold"))
        self.btnRefresh.grid(row=0, column=1, padx=10)

         # Search prisoner by CMND/CCCD
        self.btnSearch = Button(self.buttonsFrame, command=self.searchPrisonerByCitizenID, text="Tìm phạm nhân", bd=0, cursor="hand2",
                                bg="#009999",   
                                fg="white", width=15, font=("Arial", 15, 'bold'),
                                activebackground="#007777",
                                activeforeground='#FFFFFF')
        self.btnSearch.grid(row=0, column=2, padx=15, sticky="e")

        # View Laws from API
        self.btnViewLaws = Button(self.buttonsFrame, command=self.viewLaws, text="Tham khảo luật", bd=0,
                             cursor="hand2",
                             bg="#009999",
                              fg="white", width=15, font=("Arial", 15, "bold"),
                              activebackground="#007777",
                              activeforeground='#FFFFFF')
        self.btnViewLaws.grid(row=0, column=3, padx=10)



        # LogOut
        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log out", bd=0, cursor="hand2",
                                bg="#C94127",
                                fg="white", width=15, font=("Impact", 15),
                                activebackground="red")
        self.btnLogOut.grid(row=0, column=6, padx=15, sticky="e")

    
    """Table Frame using TreeView"""
    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=408, width=1400, height=400)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        # ttk style object to add configurations
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Tahoma', 13, "bold"), sticky="w")

        # Formatting the output table view
        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set,
                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), style="mystyle.Treeview")
     
        self.out.heading("1", text="STT")
        self.out.column("1", width=50, stretch=False)
        self.out.heading("2", text="Họ tên")
        self.out.column("2", width=30)
        self.out.heading("3", text="Ngày sinh")
        self.out.column("3", width=120, stretch=False)
        self.out.heading("4", text="Giới tính")
        self.out.column("4", width=90, stretch=False)
        self.out.heading("5", text="Quốc tịch")
        self.out.column("5", width=10)
        self.out.heading("6", text="Số CCCD/CMND")
        self.out.column("6", width=10)
        self.out.heading("7", text="Quê quán")
        self.out.column("7", width=5)
        self.out.heading("8", text="Loại tội phạm")
        self.out.column("8", width=5)
        self.out.heading("9", text="Hành vi phạm tội")
        self.out.column("9", width=20)   
        self.out['show'] = 'headings'

        # Đăng ký hàm displaySelectedPrisoner với sự kiện click chuột trái
        self.out.bind('<ButtonRelease-1>', self.displaySelectedPrisoner)

        # TreeView output layout configurations
        self.out.pack(fill=X)
        self.yScroll.config(command=self.out.yview)