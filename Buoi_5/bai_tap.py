import json
import os
import random
# Lưu data vào JSON và Đọc ra gán vào biến : data_users
# with open("baimoi.json", "w") as f:
#     json.dump(data_original, f, indent=4)
with open("baimoi.json", "r") as f:
    data= json.load(f)
# print(data)

# Viết thành chương trình các chức năng.

# 1. Lọc ra danh sách những người > sổ tuổi nhập. ( Dùng input)
#2.  Lọc ra danh sách những người đang làm .... Dùng input
#3.  Hiển thị thông tin của
# 4. Hiển thị người thân của  Dùng input nhập tên người nào đó.
#5.  Hiển thị thông tin của người là đảng viên ( "dang_vien": 1)
#6.  Hiển thị danh sách những người đã kết hôn
while True:
    print("1. Danh sách những người > sổ tuổi")
    print("2. Danh sách những người đang làm")
    print("3. Hiển thị thông tin của")
    print("4. Hiển thị người thân của")
    print("5. Hiển thị thông tin của người là đảng viên")
    print("6. Hiển thị danh sách những người đã kết hôn")
    print("7. Thêm Thông Tin Người Dùng")
    print("8. Thoát")

    cn = int(input("Lựa Chọn: "))
    if cn == 1:
        os.system('cls')
        so_tuoi = int(input("Nhập Số Tuổi Cần Tìm: "))
        ds_tuoi = [ds for ds in data if ds['age'] > so_tuoi]
        print(ds_tuoi)
        break
    elif cn == 2:
        os.system('cls')
        dang_lam = input("Đang Làm Công Việc nào: ")
        cv = [ds for ds in data if ds['job'] == dang_lam]
        print(cv)
        break
    elif cn == 3:
        os.system('cls')
        ds_ten = input("Tìm Thông tin Của: ")
        ten = [ds for ds in data if ds['name'] == ds_ten]
        print(ten)
        break
    elif cn == 4:
        os.system('cls')
        nguoi_than = input("Người Thân Của là: ")
        ng_th = [ds for ds in data if ds['name'] == nguoi_than]
        print(ng_th[0]['nguoi_than'])
        break
    elif cn == 5:
        os.system('cls')
        print("----Lựa Chọn Danh Sách Đảng Viên----")
        print("0. Chưa Là Đảng Viên",   "1. Đã Là Đảng Viên")
        so = int(input("Danh Sách Đảng Viên : "))
        d_v = [ds for ds in data if ds['dang_vien'] == so]
        print(d_v)
        break
    elif cn == 6:
        os.system('cls')
        for user in data:
            user['Đã Kết Hôn'] = 2
            ds_tinh_trang = user["nguoi_than"]
            for ng_than in ds_tinh_trang:
                if ng_than in ["chồng","vợ","con gái", "con trai"]:
                    user['Đã Kết Hôn'] = 1
                    break
        print("----Lựa Chọn Tình Trạng Két Hôn----")
        print("1. Đã Kết Hôn",   "2. Chưa Kết Hôn")
        so = int(input("Tình Trạng Hôn Nhân : "))
        d_v = [ds for ds in data if ds['Đã Kết Hôn'] == so]
        print(d_v)
        break
    elif cn == 7:
        ten = input('Tên :')
        tuoi = int(input('Tuổi: '))
        noi_o = input('Nơi ở: ')
        cv = input('Công Việc: ')
        print("Định dạng danh sách nhập người thân cách nhau bởi _ ")
        ng_than = input('Người Thân: ').lower()
        ds_nguoi_than = ng_than.split('_')
        print("Chưa vào đảng nhập 0, Là Đảng Viên nhập 1 ")
        d_vien = int(input('Đảng Viên: '))
        newuser = {
            'name': ten,
            'age' : tuoi,
            'address': noi_o,
            'job' : cv,
            'nguoi_than': ds_nguoi_than,
            'dang_vien': d_vien,
        }
        data.append(newuser)
        print(data)
        break

    elif cn == 8:
        break
    else:
        print("Nhập Sai Số nhập lại")

# with open("baimoi.json", "w") as f:
#     json.dump(data, f, indent=4)

