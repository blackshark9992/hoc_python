import uuid
import json
from datetime import datetime
with open("baitapvn.json", "r") as f:
    users = json.load(f)
# user = []
while True:
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Sua thong tin nhan vien")
    print("4. Xoa nhan vien")
    print("5. Danh sách các nhân viên ở tỉnh")
    print("6. Hiển thị số nhân viên nam/nữ.")
    print("7. Hiển thị số nhân viên có chuc vu")
    lua_chon = int(input("Lựa Chọn Chức Năng: "))

# Số lượng user tối đa 20,  chỉ 1 giám đốc, tuổi > 18
#     print("1. Thêm User")
#     print("2. Xem thông tin User")
#     print("3. Sua thong tin nhan vien")
#     print("4. Xoa nhan vien")
#     print("5. Danh sách các nhân viên ở tỉnh:")
#     print("6. Hiển thị số nhân viên nam/nữ.")
#     print("7. Hiển thị số nhân viên có chuc vu (input)") # GD, TP, NV
#     print("8. Thoát")
    if lua_chon == 1:
        if len(user) == 20:
            print("Đã đủ nhân viên")
            continue
        email = input("email: ")
        duoi_emails = ['@gmail.com','@yahoo.com','@hotmail.com']
        flag = False
        for duoi_email in duoi_emails:
            if email.endswith(duoi_email) and len(email) > len(duoi_email):
                flag = True
                break
        if flag is False:
            print("Email không hợp lệ")
            continue
        ngay_sinh = input("Nhập Ngày Sinh(dd/mm/yy): ")
        date = datetime.now()




        mat_khau = input("Nhập Mật Khẩu: ")
        if len(mat_khau) < 8:
            print("mật khẩu phải lớn hơn 8 ký tự")
            continue
        name = str(input("Họ Và Tên: ")).lower()

        phone_number = input("Số Điện Thoại: ")
        if len(phone_number) != 10:
            print("Số điện thoại không hợp lệ")
            continue
        flag = True
        for number in phone_number:
            if number not in '0123456789':
                flag = False
                break
        if flag is False:
            print("Sđt không hợp lệ")
            continue
        address = input("Địa chỉ: ")

        genderr= input("Giới Tính: ")

        chuc_vu = input("Chức Vụ CV: ")
        if chuc_vu.lower() == "giám đốc":
            flag_chuc_vu = False
            for user in  users:
                if user["chuc_vu"].lower() == "giám đốc":
                    flag_chuc_vu = True
                    break
            if flag_chuc_vu is True:
                print("Đã có giám đốc")



        user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "birthday_date": ngay_sinh,
            "pass": mat_khau , # Tren 8 ky tu
            "name": name,
            "phone_number":phone_number ,
            "address": address,
            "gender" : genderr ,
            "chuc_vu" : chuc_vu,
            "ngay_tao" :""
        }




# if lua_chon == 2:
#
#
# if lua_chon == 3:
#
#
# if lua_chon == 4:
#
#
# if lua_chon == 5:
#
#
# if lua_chon == 6:
#
#
# if lua_chon == 7:


# Tạo id
# user_id = str(uuid.uuid4())

# # xác định email
# duoi_emails = ["@gmail.com", "@yahoo.com"]
#
# gmail = "@gmail.com"
#
# flag = False
# for duoi_email in duoi_emails:
#     if gmail.endswith(duoi_email) and len(gmail) > len(duoi_email):
#         flag = True
#         break
# if flag is False:
#     print("Email không hợp lệ")

# xác định sđt hợp lệ
# phone_number = "0a23456789"
#
# if len(phone_number) != 10:
#     print("Số điện thoại không hợp lệ")
#
#
# flag = True
# for number in phone_number:
#     if number not in '0123456789':
#         flag = False
#         break
# if flag is False:
#     print("Sđt không hợp lệ")


# gender = "nam"
# if gender not in  ["nam", "nu"]:
#     print("gioi tinh khong hop le")