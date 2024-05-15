from tkinter import *
from tkinter import ttk, messagebox
import requests
import admin
import user
import json
import os

law_json_file = "laws_api.json"

class LawSession():
    
    def __init__(self, root, name_user, role):
        self.root = root
        self.name_user = name_user
        self.role = role


        self.tree = None

        self.lawHeader()
        self.lawFrameButtons()
        self.lawFrameTable()

    def lawHeader(self):
        self.sessionFrame = Frame(self.root, bg="#5856a0")
        self.sessionFrame.pack(side=TOP, fill=X)
        self.session_frame_title = Label(self.sessionFrame, text="THAM KHẢO LUẬT CHXHCN VIỆT NAM", font=("Arial", 35, 'bold'),
                                         bg="#5856a0",
                                         fg="white")
        self.session_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.law_title = Label(self.sessionFrame, text="Chọn danh mục luật cần xem: ", font=("Courier", 25, "bold"),
                                       bg="#5856a0",
                                       fg="white")
        self.law_title.grid(row=1, columnspan=2, padx=10, pady=20, sticky="w")

    """ CTA METHOD """
    def viewCriminal(self):
        self.loadLaws("Hình sự")
    
    def viewCivil(self):
        self.loadLaws("Dân sự")

    def viewLabor(self):
        self.loadLaws("Lao động")

    def viewTax(self):
        self.loadLaws("Thuế")

    def viewEnterprise(self):
        self.loadLaws("Doanh nghiệp")

    def viewAdministrative(self):
        self.loadLaws("Hành chính")

    def viewLawsSaved(self):
         # Tên file JSON để đọc dữ liệu
        law_json_file = "laws_api.json"

        try:
            # Đọc dữ liệu từ tệp JSON
            with open(law_json_file, "r", encoding='utf-8') as file:
                # Load dữ liệu từ tệp JSON
                data = json.load(file)
            
            # Xóa dữ liệu cũ trong Treeview
            self.tree.delete(*self.tree.get_children())

            # Hiển thị dữ liệu từ tệp JSON trên Treeview
            law_id_counter = 1
            for law in data:
                law_id = law.get('ID', '')
                law_name = law.get('Tên luật', '')
                law_desc = law.get('Mô tả', '')
                law_category = law.get('Danh mục', '')
                enacted_date = law.get('Ngày phát hành', '')
                effective_date = law.get('Ngày hiệu lực', '')

                # Thêm dữ liệu vào Treeview
                self.tree.insert('', 'end', values=(law_id_counter, law_name, law_desc, law_category, enacted_date, effective_date))
                law_id_counter += 1

        except FileNotFoundError:
            # Nếu tệp không tồn tại, hiển thị thông báo
            messagebox.showinfo("Thông báo", "Không có luật nào được lưu trong tệp JSON.")

    # Method to redirect to the previous frame
    def GoBack(self):
        self.sessionFrame.destroy()
        self.tableFrame.destroy()

        # Check role được truyển từ login.py -> admin/user.py -> laws.py
        if self.role == "admin":
            admin.AdminControls(self.root, self.role)
        elif self.role == "user":
            user.UserControls(self.root, self.name_user, self.role)

    def lawFrameButtons(self):
        # Law Buttons Frame Configurations
        self.buttonsFrame = Frame(self.sessionFrame, bg="#5856a0")
        self.buttonsFrame.grid(row=7, column=0, padx=10, pady=10, sticky="w", columnspan=8)

      
        # Criminal, Civil, Labor,Tax, Enterprise, Administrative
        # Luật Hình sự
        self.btnCriminal = Button(self.buttonsFrame, command=self.viewCriminal, text="Hình sự", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=15, font=("Arial", 15, "bold"))
        self.btnCriminal.grid(row=1, column=0,  padx=10)

        # Luật dân sự
        self.btnCivil = Button(self.buttonsFrame, command=self.viewCivil, text="Dân sự", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=14, font=("Arial", 15, "bold"))
        self.btnCivil.grid(row=1, column=1,  padx=10)

        # Luật lao động
        self.btnLabor = Button(self.buttonsFrame, command=self.viewLabor, text="Lao động", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=14, font=("Arial", 15, "bold"))
        self.btnLabor.grid(row=1, column=2,  padx=10)
        
        # Luật Thuế
        self.btnTax = Button(self.buttonsFrame, command=self.viewTax, text="Thuế", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=12, font=("Arial", 15, "bold"))
        self.btnTax.grid(row=1, column=3,  padx=10)

        # Luật doanh nghiệp
        self.btnEnterprise = Button(self.buttonsFrame, command=self.viewEnterprise, text="Doanh nghiệp", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=14, font=("Arial", 15, "bold"))
        self.btnEnterprise.grid(row=1, column=4,  padx=10)

        # Luật hành chính
        self.btnAdministrative = Button(self.buttonsFrame, command=self.viewAdministrative, text="Hành chính", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=14, font=("Arial", 15, "bold"))
        self.btnAdministrative.grid(row=1, column=5,  padx=10)

        # Các luật đã lưu vào json file: laws_api.json
        self.btnLawsSave = Button(self.buttonsFrame, command=self.viewLawsSaved, text="Đã lưu", bd=0,
                              cursor="hand2",
                              bg="#EADDF7",
                              fg="#5856a0", width=13, font=("Arial", 15, "bold"))
        self.btnLawsSave.grid(row=1, column=6,  padx=10)

        img_quochuy_vn = PhotoImage(file='img/quochuy_vn.png')
        self.quochuyVN = Label(self.sessionFrame, image=img_quochuy_vn, bg='#5856a0')
        self.quochuyVN.image = img_quochuy_vn  # Giữ tham chiếu đến ảnh
        self.quochuyVN.grid(row=0, column=2, columnspan=2, padx=10, pady=9)

        # GoBack
        self.btnGoBack = Button(self.sessionFrame, command=self.GoBack, text="Go Back", bd=0, cursor="hand2",
                                bg="#C94127",
                                fg="white", width=15, font=("Impact", 15),
                                activebackground="red")
        self.btnGoBack.grid(row=0, column=7, padx=10, sticky="e")

    
    """Table Frame using TreeView"""
    def lawFrameTable(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=280, width=1400, height=560)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        # ttk style object to add configurations
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=40)
        self.style.configure("mystyle.Treeview.Heading", font=('Arial', 14, 'bold'), sticky="w")

        self.tree = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set, columns=(1,2,3,4,5,6),
                                selectmode='browse', style="mystyle.Treeview")
        self.tree.heading("#1", text="STT")  # Đặt tiêu đề cho cột ID
        self.tree.heading("#2", text="Tên luật")
        self.tree.heading("#3", text="Mô tả")
        self.tree.heading("#4", text="Danh mục")
        self.tree.heading("#5", text="Ngày phát hành")
        self.tree.heading("#6", text="Ngày hiệu lực")
        
        # Đặt các chỉ số cột
        self.tree.column("1", width=50, stretch=False)
        self.tree.column("2", width=200)
        self.tree.column("3", width=200)
        self.tree.column("4", width=170, stretch=False)
        self.tree.column("5", width=180, stretch=False)
        self.tree.column("6", width=180, stretch=False)

        self.tree['show'] = 'headings'
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

        self.yScroll.config(command=self.tree.yview)

        # Bind double click event to show details popup
        self.tree.bind("<Double-1>", self.showLawDetails)

    # METHOD LOAD DATA LAWS FROM API: https://laws-api.vercel.app/api/law
    def loadLaws(self, category):
        # Clear existing data
        self.tree.delete(*self.tree.get_children())

        # Fetch laws based on category from API and populate the treeview
        url = "https://laws-api.vercel.app/api/law"
        params = {"category": category}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            laws_data = data.get('data', [])

            if laws_data:
                law_id_counter = 1

                for law in laws_data:
                    name = law.get('name', '')
                    desc = '\n'.join(law.get('desc', []))
                    law_category = law.get('category', '')  # Lấy danh mục của luật
                    enacted_date = law.get('enactedDate', '')
                    effective_date = law.get('effectiveDate', '')

                    # Kiểm tra xem luật có thuộc danh mục được chọn không
                    if law_category == category:
                        self.tree.insert('', 'end', values=(law_id_counter, name, desc, law_category, enacted_date, effective_date))
                        law_id_counter += 1
            else:
                print("No laws found for the selected category")
        else:
            print("Failed to fetch laws from the API")

    # METHOD SAVE A LAW TO JSON FILE
    def saveLawToJSON(self, law_id, law_name, law_desc, law_category, enacted_date, effective_date):
        # Tạo một dictionary từ thông tin luật
        law_data = {
            "ID": law_id,
            "Tên luật": law_name,
            "Mô tả": law_desc,
            "Danh mục": law_category,
            "Ngày phát hành": enacted_date,
            "Ngày hiệu lực": effective_date
        }

        try:
            # Đọc dữ liệu hiện có từ tệp JSON
            with open(law_json_file, "r", encoding='utf-8') as file:
                # Kiểm tra xem tệp JSON có dữ liệu không
                if os.stat(law_json_file).st_size == 0:
                    # Nếu tệp trống, tạo một danh sách rỗng
                    data = []
                else:
                    # Nếu tệp không trống, đọc dữ liệu từ tệp
                    data = json.load(file)
        except FileNotFoundError:
            # Nếu tệp không tồn tại, tạo một danh sách rỗng
            data = []

        # Thêm dữ liệu của luật mới vào danh sách này
        data.append(law_data)

        # Mở file JSON và ghi lại toàn bộ dữ liệu vào đó
        try:
            with open(law_json_file, "w", encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Success", "Lưu luật vào file json thành công")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi lưu luật: {str(e)}")



    # METHOD DISPLAY POPOP TO SHOW LAW DETAIL
    def showLawDetails(self, event):
        # Lấy ID của dòng được chọn trong Treeview
        selected_item = self.tree.selection()[0]
        law_id = self.tree.item(selected_item, "values")[0]  # STT là cột đầu tiên

        # Lấy thông tin chi tiết từ Treeview
        law_name = self.tree.item(selected_item, "values")[1]
        law_desc = self.tree.item(selected_item, "values")[2]
        law_category = self.tree.item(selected_item, "values")[3]
        enacted_date = self.tree.item(selected_item, "values")[4]
        effective_date = self.tree.item(selected_item, "values")[5]

        # Tạo popup hiển thị thông tin chi tiết
        popup = Toplevel()
        popup.title(f"Chi tiết luật {law_name}")
        # popup.geometry("600x400")
        popup.geometry("700x450")

        # Tạo nút Save để lưu dữ liệu luật vào tệp JSON
        save_button = Button(popup, text="Lưu luật", command=lambda: self.saveLawToJSON(law_id, law_name, law_desc, law_category, enacted_date, effective_date))
        save_button.pack(pady=10)

        # Hiển thị thông tin chi tiết trong popup
        detail_label = Label(popup, text=f"ID: {law_id}\nTên luật: {law_name}\nDanh mục: {law_category}\nNgày phát hành: {enacted_date}\nNgày hiệu lực: {effective_date}",
                             font=("Arial", 12), justify=LEFT)
        detail_label.pack(pady=10, padx=20)


        # Tạo một cửa sổ cuộn để chứa mô tả
        desc_title = Label(popup, text="Nội dung chi tiết", font=('Arial', 16, 'bold')).pack()

        desc_scroll = Scrollbar(popup)
        desc_scroll.pack(side=RIGHT, fill=Y)

        desc_text = Text(popup, wrap=WORD, font=("Arial", 12), yscrollcommand=desc_scroll.set, state=NORMAL)
        desc_text.insert(END, law_desc)
        desc_text.pack(pady=10, padx=20, fill=BOTH, expand=True)

        desc_scroll.config(command=desc_text.yview)

