import json
import random

# í dụ 1 người dùng:
# {
#     "tên": "Nguyễn Ngọc Cương",
#     "tuổi": 18,   # Tuyển nhân viên >= 18 tuổi
#     "địa chỉ": "HY", # Giới hạn chỉ chọn HN, HY, HD, QN, HP, LC, YB, BN, HB ( Còn nếu ngoài các tỉnh sau thì print
#                      # Không tuyển người ở {tỉnh nhập}
#
#     "giới tính": True, # True: nam, False: Nữ
#     "chiều cao": 171,   # Yêu cầu chiều cao > 160
#     "vị trí": "Nhân Viên",  # Giám đốc / Trưởng Phòng / Nhân Viên   # Chỉ có 1 giám đốc. Nếu đã có giám đốc thì
#     # không thể thêm user mới và print Đã có giám đốc
#     "tình trạng hôn nhân": False,  #True: đã kết hôn, False: chưa kết hôn.
#     "lương": 100,
#     "tài khoản": "cuong123",
#     "mật khẩu": "1234567"
# }

with open("baitapvn.json", "r") as f:
    user = json.load(f)
# user = []
while True:
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Danh sách các nhân viên ở tỉnh đã nhập")
    print("4. Tăng/ giảm lương người dùng")
    print("5. Danh sách nhân viên có lương")
    print("6. Hiển thị tổng lương phải trả hàng tháng cho mọi người")
    print("7. Hiển thị tổng số tiền phải trả trong 1 năm cho mọi người")
    print("8. Hiển thị tổng lương phải trả hàng tháng cho Nhân Viên")
    print("9. Hiển thị tổng lương phải trả hàng tháng cho Trưởng Phòng")
    print("10. Hiển thị số nhân viên nam, số nhân viên nữ.")
    print("11.Xoa nhan vien")
    print("12. Thoát")
    danh_sach = int(input("Lựa Chọn Chức Năng: "))

    if danh_sach == 1:
        if len(user) == 20:
            print("Đã đủ nhân viên")
            break
        ten = str(input("tên: ")).lower()

        # Validate tên
        for nguoi_dung in user:
            if nguoi_dung["tên"].lower() == ten:
                print("Người dùng đã tồn tại")
                break

        tuoi = int(input("Tuổi: "))
        if tuoi < 18:
            print("Bạn Chưa Đủ Tuôi")
            break
        dia_chi = str(input("Địa Chỉ: ")).upper()
        dc_tuyen = ["HN", "HY", "HD", "QN", "HP", "LC", "YB", "BN", "HB"]
        if dia_chi in dc_tuyen:
            pass
        else:
            print("Không Tuyển Người Ngoại Tỉnh")
            break
        gioi_tinh = str(input("Giới Tính: ")).lower()
        if gioi_tinh == "true":
            gioi_tinh = True
            gioi_tinh2 = "Nam"
        elif gioi_tinh == "false":
            gioi_tinh = False
            gioi_tinh2 = "Nữ"
        chieu_cao = int(input("Chiều Cao: "))
        if chieu_cao < 160:
            print("Bạn Chưa Chiều Cao")
            break
        vi_tri = str(input("Vị Trí: ")).lower()

        tinh_trang_hon_nhan = str(input("Tình Trạng Hôn Nhân true hoặc false: : ")).lower()
        if tinh_trang_hon_nhan == "true":
            tinh_trang_hon_nhan = True
            hon_nhan2 = "Đã Kết Hôn"
        elif tinh_trang_hon_nhan == "false":
            tinh_trang_hon_nhan = False
            hon_nhan2 = "Chưa Kết Hôn"

        luong = int(input("Lương: "))

        ten_dang_nhap = input("Nhập Tài Khoản : ")
        mat_khau = input("mật Khẩu: ")

        users = {
                "tên": ten,
                "tuổi": tuoi,
                "địa chỉ": dia_chi, # Giới hạn chỉ chọn HN, HY, HD, QN, HP, LC, YB, BN, HB ( Còn nếu ngoài các tỉnh sau thì print
                                 # Không tuyển người ở {tỉnh nhập}

                "giới tính": gioi_tinh2 , # True: nam, False: Nữ
                "chiều cao": chieu_cao,   # Yêu cầu chiều cao > 160
                "vị trí": vi_tri ,  # Giám đốc / Trưởng Phòng / Nhân Viên   # Chỉ có 1 giám đốc. Nếu đã có giám đốc thì
                # không thể thêm user mới và print Đã có giám đốc
                "tình trạng hôn nhân": hon_nhan2,
                "lương": luong,
                "tài khoản": ten_dang_nhap,
                "mật khẩu": mat_khau,

        }

        user.append(users)
        with open("baitapvn.json", "w") as f:
            json.dump(user, f, indent=4)
        break

    # 2) Xem thông tin User ( Nhập input tên)
    elif danh_sach == 2:
        dsten = input(" Nhầm Tên Muốn Tìm : ").lower()
        for ds_ten in  user:
            if ds_ten['tên'] == dsten:
                print(ds_ten)
                break
        else:
            print("Không Có Tên Trong Công Ty")
        break
    elif danh_sach == 3:
        dia_chi2 = input(" Nhầm Tỉnh Muốn Tìm : ").upper()
        for ds_dc in  user:
            if ds_dc['địa chỉ'] == dia_chi2:
                print("Các Nhân Viên Thuộc Tỉnh",dia_chi2,"Là: ",ds_dc['tên'])
        break
    # 4) Tăng/ giảm lương người dùng : (Nhập input tên để chọn người.)
    elif danh_sach == 4:
        dsten = input(" Nhầm Tên Muốn Tìm : ").lower()
        for ds_ten in  user:
            if ds_ten['tên'] == dsten:
                luong_sua = int(input("Số lương muốn sửa: "))
                ds_ten['lương'] = luong_sua
                with open("baitapvn.json", "w") as f:
                    json.dump(user, f, indent=4)
                break
        else:
            print("Không Có Tên Trong Hồ Sơ")
        break

    elif danh_sach == 5:
        dstien = int(input("Tiền Lương Muốn Tìm: "))
        for ds_tien in  user:
            if ds_tien['lương'] > dstien:
                print(ds_tien)
        break
    elif danh_sach == 6:
        luongthang = 0
        for ds_tien in user:
            luongthang += ds_tien['lương']

        # luongthang = sum([ds_tien['lương'] for ds_tien in user])


        print("Tổng Số Lương Phải Trả Trong Tháng là :", luongthang , "VND")
        break
    elif danh_sach == 7:
        luong_ca_nam = 0
        for ds_tien_cn in  user:
            luong_ca_nam += ds_tien_cn['lương'] * 12

        # luong_ca_nam = sum([ds_tien['lương'] for ds_tien in user])*12
        print("Tổng Số Lương Phải Trả Trong Năm là :", luong_ca_nam , "VND")
        break
    elif danh_sach == 8:
        l_nv = 0
        for ds_tien_nv in user:
            if ds_tien_nv['vị trí'] == 'nhân viên':
                l_nv += ds_tien_nv['lương']

        # l_nv = sum([ds_tien_nv['lương'] for ds_tien_nv in user if ds_tien_nv['vị trí'] == 'nhân viên'])
        print("Tổng Số Lương Phải Trả cho nhân viên :", l_nv , "VND")
        break
    elif danh_sach == 9:
        l_tp = 0
        for ds_tien in  user:
            if ds_tien['vị trí'] == 'trưởng phòng':
                l_tp += ds_tien['lương']

        # Tương tự
        print("Tổng Số Lương Phải Trả cho trưởng phòng :", l_tp , "VND")
        break
    elif danh_sach == 10:
        print("1.Số Nhân Viên Nam     2. Số Nhân Viên Nữ")
        gioi_tinh = int(input("Số Nhân Viên: "))
        # if gioi_tinh == 1:
        #     for gioi_tinh in user:
        #         if gioi_tinh['giới tính'] == 'Nam':
        #             print(gioi_tinh)
        # elif gioi_tinh == 2:
        #     for gioi_tinh in user:
        #         if gioi_tinh['giới tính'] == 'Nữ':
        #             print(gioi_tinh)
        so_nhan_vien_nam = len([gioi_tinh for gioi_tinh in user if gioi_tinh['giới tính'] == 'Nam'])
        so_nhan_vien_nu = len(user) - so_nhan_vien_nam
        if gioi_tinh == 1:
            print(so_nhan_vien_nam)
        else:
            print(so_nhan_vien_nu)
        break
    elif danh_sach == 11:
        xoa_nv = input("Nhập tên nhân viên cần xóa: ")
        flag = False
        for nguoi_dung in user:
            if nguoi_dung['tên'] == xoa_nv:
                user.pop(user.index(nguoi_dung))
                flag = True
                print("Đã Xóa Thành Công")
        if flag is False:
            print("Không Thể Xóa không tìm thấy người dùng")
        with open("baitapvn.json", "w") as f:
            json.dump(user, f, indent=4)

        break

    #     #     with open("baitapvn.json", "w") as f:
    #     #         json.dump(user, f, indent=4)
    #     # break
    # # elif danh_sach == 12:
    # #         break