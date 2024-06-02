users = [
    ['cuong@gmail.com', '12345678'],
    ['cuong1@gmail.com', '1234567890'],
    ['nguyenminh@yahoo.com', 'password1'],
    ['lethibao@yahoo.com', 'password2'],
    ['tranthanhtu@gmail.com', 'password3'],
    ['huynhphuong@yahoo.com', 'password4'],
    ['ngoctrai@gmail.com', 'password5'],
    ['hoangmai@yahoo.com', 'password6'],
    ['thanhson@gmail.com', 'password7'],
    ['duongkhanh@yahoo.com', 'password8'],
    ['ngocanh@gmail.com', 'password9'],
    ['haiphuong@yahoo.com', 'password10'],
    ['vietanh@gmail.com', 'password11'],
    ['minhphuong@yahoo.com', 'password12'],
    ['khanhhoa@gmail.com', 'password13'],
    ['thuha@yahoo.com', 'password14'],
    ['leminh@gmail.com', 'password15'],
    ['phuonglinh@yahoo.com', 'password16'],
    ['hoangnam@gmail.com', 'password17'],
    ['anhthu@yahoo.com', 'password18']
]
# Đề bài:  Tương tác người dùng: Nhập user, password.
# Kiểm tra user có đúng format email không? Nếu sai thì trả ra : Sai email
# Kiểm tra mật khẩu > 8 kí tự. Nếu sai thì trả ra : Mật khẩu chưa đủ 8 kí tự
# Tìm trong list user có tài khoản, mật khẩu được đăng nhập.
# Đúng cả 2 thì trả ra: Đăng nhập thành công.
# Sai tài khoản : Tài khoản không tồn tại.
# Đúng tài khoản, sai mật khẩu : trả ra sai mật khẩu
#Demo cho đăng nhập
# user = ['cuong@gmail.com', '12345678']
#
# user_name = input("Mời nhập UserName:")
# password = input("Mời nhập Password:")
#
# if user_name == user[0] and password == user[1]:
#     print("Đăng nhập thành công")
# else:
#     print("Đăng nhập không thành công")

ten_dang_nhap = input("Nhập Tài Khoản: ")
mat_khau = input("Nhập Mật Khẩu: ")

if not (ten_dang_nhap[len(ten_dang_nhap) - len('@gmail.com'):] == '@gmail.com' or
        ten_dang_nhap[len(ten_dang_nhap) - len('@yahoo.com'):] == '@yahoo.com'):
    print("Sai User")
else:
    if len(mat_khau) < 8:
        print("Mật Khẩu Phải Lớn hơn 8 ký tự: ")
    flag = True
    for user in users:
        # print(user[0],user[1])
        if ten_dang_nhap == user [0] and mat_khau == user[1]:
            print("Đăng Nhập Thành Công: ")
            flag = False
        elif ten_dang_nhap == user [0] and mat_khau != user[1]:
            print("Sai Mật Khẩu: ")
            flag = False
    if flag:
        print("Đăng Nhập Không Thành Công.")
