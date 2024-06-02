
# Tạo 1 list 40 phần tử ( bao gồm số tự nhiên, số thập phân, chuỗi)
# Viết chương trình tương tác với người dùng:
#  3 chức năng :
# 1) Lọc danh sách số tự nhiên
# 2) Lọc danh sách chuỗi
# 3) Lọc danh sách số thập phân
# 4)  Danh sách mới loại bỏ thành phần tử trùng lặp
# Tương tác với người dùng thì dùng input cho người dùng chọn 1 trong 4 chức năng nhé.  Nếu chọn chức năng không có thì print ra : chức năng không hợp lệ.

danh_sach = ("Mận","táo","Dưa","Táo","ổi","Mang Cụt",1,2,0.55,85,0.5,0.69,3,4,5,6,7,"Mang Cụt",8,8,7,6,5,4,3,2,1,0.25,0.58,0.25,0.58,0.66,0.14,0.66,0.14,"Mận","táo","Dưa","Táo","ổi")
print("----->Danh Sách Lựa Chọn<------")
print("1.Danh Sách Số Nguyên.")
print("2.Danh Sách Chuỗi.")
print("3.Danh Sách Số Thập Phân.")
print("4.Danh Sách Mới Loại Bỏ Trùng Lặp.")
lc = int(input("Mời Nhập Lựa Chọn : ",))
if lc == 1:
    print("DS Số Nguyên: ",)
elif lc == 2:
    print("DS Chuỗi: ")
elif lc == 3:
    print("DS số Thập Phân")
elif lc == 4:
    print("DS Mới Bỏ Trùng Lặp: ")
else:
    print("Nhập Sai Mời Bạn Chọn Lại.")
