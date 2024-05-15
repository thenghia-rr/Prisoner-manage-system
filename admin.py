from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
import json
import login
import laws

PRIMARY_COLOR = '#5856a0'
file_json_prisoners = 'prisoners.json'

class AdminControls:
    def __init__(self, root, role):
        self.root = root
        self.name_user = StringVar()
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

        # self.txt = StringVar()
        # self.txt.set('Quá xinh đẹp')

        # self.fullname.set('Lisa Manonal')
        # self.date_of_birth.set('27/03/1997')
        # self.gender.set('Nữ')
        # self.nationality.set('Thái Lan')
        # self.citizen_id.set("012345678910")
        # self.hometown.set("Bangkok")
        # self.offense_type.set("Hình sự")

        
        self.adminControlsFrame()
        self.adminFrameButtons()
        self.tableOutputFrame()
        

    """Prisoner Info Entries Frame - Khung nhập thông tin phạm nhân"""
    def adminControlsFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#5856a0")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.admin_frame_title = Label(self.entriesFrame, text="Admin Control Panel", font=("Arial", 35, 'bold'),
                                       bg="#5856a0",
                                       fg="white")
        self.admin_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Admin image
        img_admin = PhotoImage(file='img/admin_icon.png')
        self.adminImg = Label(self.entriesFrame, image=img_admin, bg=PRIMARY_COLOR)
        self.adminImg.image = img_admin  # Giữ tham chiếu đến ảnh
        self.adminImg.grid(row=0, column=2, padx=1, pady=9)

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

        self.txtCriminalBehavior = Text(self.entriesFrame, font=("Calibri", 13), width=44, height=5)
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


     # Validate length of citizen ID
    def validateCitizenID(self, citizen_id):
        # Kiểm tra xem độ dài của số CCCD/CMND có ít nhất 12 ký tự không
        if len(citizen_id) < 12:
            return False
        else:
            return True
    """ All method to manipulations with file json """
    # Method auto update ID after have manipulation changed ID 
    def updateIDsAfterDeletion(self, deleted_id):
        try:
            with open(file_json_prisoners, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # Cập nhật lại ID cho tất cả các phạm nhân
            for prisoner in data:
                if prisoner.get("id") > deleted_id:
                    prisoner["id"] -= 1
            
            # Ghi lại dữ liệu đã cập nhật vào tệp JSON
            with open(file_json_prisoners, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật ID phạm nhân: {str(e)}")

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

    # Method add data new prisoner to json file
    def addPrisonerJson(self, prisoner_data):
        try:
            with open(file_json_prisoners, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Tìm id lớn nhất trong dữ liệu hiện có
                max_id = max([p.get("id", 0) for p in data], default=0)
                # Tăng id lên 1 để tạo id mới cho phạm nhân tiếp theo
                prisoner_data["id"] = max_id + 1
                data.append(prisoner_data)
            with open(file_json_prisoners, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm phạm nhân: {str(e)}")

    # Method to update prisoner data in the JSON file
    def updatePrisonerJson(self, prisoner_id, updated_data):
        try:
            with open(file_json_prisoners, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Tìm phạm nhân có ID tương ứng và cập nhật dữ liệu mới
            for prisoner in data:
                if prisoner.get("id") == int(prisoner_id):
                    prisoner.update(updated_data)
                    break

            # Ghi lại dữ liệu cập nhật vào tệp JSON
            with open(file_json_prisoners, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật thông tin phạm nhân: {str(e)}")

    # Method to delete prisoner data in the JSON file
    def deletePrisonerJson(self, prisoner_id):
        try:
            with open(file_json_prisoners, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # Tìm phạm nhân có ID tương ứng và xóa nó khỏi danh sách
            for idx, prisoner in enumerate(data):
                if prisoner.get("id") == int(prisoner_id):
                    del data[idx]
                    break

            # Ghi lại dữ liệu đã cập nhật vào tệp JSON
            with open(file_json_prisoners, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            # Cập nhật lại ID cho các phạm nhân còn lại
            self.updateIDsAfterDeletion(int(prisoner_id))                

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa phạm nhân: {str(e)}")

    """CTA Methods"""
    # Method to display all Prisoners in the Treeview Frame
    def viewPrisoners(self):
        self.loadPrisonersJson()
    
    # Method to add new prisoner 
    def addPrisoner(self):
        if self.txtName.get() == "" or self.txtDOB.get() == "" or self.comboGender.get() == "" or self.txtNationality.get() == "" or self.txtCitizenID.get() == "" or self.txtHometown.get() == "" or self.comboOffenseType.get() == "" or self.txtCriminalBehavior.get("1.0","end-1c") == "":
            messagebox.showerror("Lỗi!", "Vui lòng nhập đủ thông tin!")
            return

        # Kiểm tra độ dài của số CCCD/CMND
        if not self.validateCitizenID(self.txtCitizenID.get()):
            messagebox.showerror("Lỗi!", "Số CCCD/CMND phải có ít nhất 12 ký tự!")
            return

        prisoner_data = {
            "fullname": self.txtName.get(),
            "date_of_birth": self.txtDOB.get(),
            "gender": self.comboGender.get(),
            "nationality": self.txtNationality.get(),
            "citizen_id": self.txtCitizenID.get(),
            "hometown": self.txtHometown.get(),
            "offense_type": self.comboOffenseType.get(),
            "criminal_behaviors": self.txtCriminalBehavior.get("1.0", "end-1c")
        }
        self.addPrisonerJson(prisoner_data)
        messagebox.showinfo("Thông báo", "Thêm phạm nhân thành công!")
        # Cập nhật giao diện, load lại danh sách phạm nhân
        self.resetForm()
        self.viewPrisoners()

    # Method to update selected Prisoner details
    def updatePrisoner(self):
        # Kiểm tra xem có phạm nhân nào được chọn không
        if not self.out.selection():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn phạm nhân để cập nhật thông tin!")
            return

        # Lấy ID của phạm nhân được chọn
        selected_item = self.out.selection()[0]
        prisoner_id = self.out.item(selected_item, 'values')[0]

        # Thu thập dữ liệu mới từ các trường nhập liệu trên giao diện
        updated_prisoner_data = {
            "fullname": self.txtName.get(),
            "date_of_birth": self.txtDOB.get(),
            "gender": self.comboGender.get(),
            "nationality": self.txtNationality.get(),
            "citizen_id": self.txtCitizenID.get(),
            "hometown": self.txtHometown.get(),
            "offense_type": self.comboOffenseType.get(),
            "criminal_behaviors": self.txtCriminalBehavior.get("1.0", "end-1c")
        }

        try:
            # Cập nhật thông tin phạm nhân trong tệp JSON
            self.updatePrisonerJson(prisoner_id, updated_prisoner_data)

            messagebox.showinfo("Thông báo", "Cập nhật thông tin phạm nhân thành công!")
            # Cập nhật giao diện, load lại danh sách phạm nhân
            self.viewPrisoners()  # Gọi lại phương thức viewPrisoners để làm mới danh sách phạm nhân

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật thông tin phạm nhân: {str(e)}")

    # Method to delete selected Prisoner
    def deletePrionser(self):
        # Kiểm tra xem có phạm nhân nào được chọn không
        if not self.out.selection():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn phạm nhân để xóa!")
            return

        # Lấy ID của phạm nhân được chọn
        selected_item = self.out.selection()[0]
        prisoner_id = self.out.item(selected_item, 'values')[0]

        try:
            self.deletePrisonerJson(prisoner_id)

            messagebox.showinfo("Thông báo", "Xóa phạm nhân thành công!")

            # Cập nhật giao diện, load lại danh sách phạm nhân
            self.viewPrisoners()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa thông tin phạm nhân: {str(e)}") 
        
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

    # Method to redirect the frame for LAWS API
    def viewLaws(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        self.name_user.set('')
        laws.LawSession(self.root,self.name_user, self.role)

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
    def adminFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#5856a0")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        # Display List
        self.btnView = Button(self.buttonsFrame, command=self.viewPrisoners, text="Xem danh sách phạm nhân", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=22, font=("Arial", 15, "bold"))
        self.btnView.grid(row=0, column=0,  padx=10)

        # Add a new Prisoner
        self.btnAdd = Button(self.buttonsFrame, command=self.addPrisoner, text="Thêm phạm nhân", bd=0, cursor="hand2",
                             bg="#EADDF7",
                             fg="#5856a0", width=16, font=("Arial", 15, "bold"))
        self.btnAdd.grid(row=0, column=2, padx=10)

        # Update selected Prisoner
        self.btnUpdate = Button(self.buttonsFrame, command=self.updatePrisoner, text="Cập nhật thông tin", bd=0,
                                cursor="hand2",
                                bg="#EADDF7",
                                fg="#5856a0", width=18, font=("Arial", 15, "bold"))
        self.btnUpdate.grid(row=0, column=3, padx=10)

        # Delete Selected Prisoner
        self.btnDlt = Button(self.buttonsFrame, command=self.deletePrionser, text="Xóa phạm nhân", bd=0,
                             cursor="hand2",
                             bg="#EADDF7",
                             fg="#5856a0", width=15, font=("Arial", 15, "bold"))
        self.btnDlt.grid(row=0, column=4, padx=10)
        # Refresh Form Prisoner
        self.btnRefresh = Button(self.buttonsFrame, command=self.resetForm, text="Reset Form", bd=0,
                             cursor="hand2",
                             bg="#EADDF7",
                             fg="#5856a0", width=15, font=("Arial", 15, "bold"))
        self.btnRefresh.grid(row=0, column=5, padx=10)

        # View Laws from API
        self.btnViewLaws = Button(self.buttonsFrame, command=self.viewLaws, text="Tham khảo luật", bd=0,
                             cursor="hand2",
                             bg="#009999",
                              fg="white", width=15, font=("Arial", 15, "bold"),
                              activebackground="#007777",
                              activeforeground='#FFFFFF')
        self.btnViewLaws.grid(row=0, column=6, padx=10)


        # Search prisoner by CMND/CCCD
        self.btnSearch = Button(self.entriesFrame, command=self.searchPrisonerByCitizenID, text="Tìm phạm nhân", bd=0, cursor="hand2",
                                bg="#009999",   
                                fg="white", width=14, font=("Arial", 15, 'bold'),
                                activebackground="#007777",
                                activeforeground='#FFFFFF')
        self.btnSearch.grid(row=0, column=5, padx=15, sticky="e")
        # LogOut
        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log out", bd=0, cursor="hand2",
                                bg="#C94127",   
                                fg="white", width=12, font=("Impact", 15),
                                activebackground="red")
        self.btnLogOut.grid(row=0, column=6, padx=15, sticky="e")
       

    """Table Frame using TreeView"""
    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=405, width=1400, height=400)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        # ttk style object to add configurations
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=("Tahoma", 13, "bold"), sticky="w")

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