danh_sach = [0,1,2,3,4,5,6,7,8,9,10]

# try:
#     print("Danh sách mới:", danh_sach[3:9])
# #  Cách lấy phần từ từ tứ 3 - 10
#     print("Danh Sách Mới 2: ", danh_sach[3:])
#     print("Danh Sách Mới 2: ", danh_sach[3:len(danh_sach)])
#     print("Phần tử Cuối danh sách 1:", danh_sach[len(danh_sach)-1])
#     print("Phần tử Cuối danh sách 2:", danh_sach[-1])
#     print("Phần tử Ngoài danh sách:", danh_sach[13])
# except Exception as ex:
#     print("Lỗi: ",ex)
# print("Oke")

# try:
#     pass
# except Exception as  ex:
#     print("Lỗi: ", ex)
# Bien_False = False
# Bien_None  = None
# Bien_True = True
# if Bien_True:
#     print(Bien_True, "True")
# else:
#     print(Bien_True, "False")
# if Bien_False:
#     print(Bien_False, "True")
# else:
#     print(Bien_False, "False")
# if Bien_None:
#     print(Bien_None, "True")
# else:
#     print(Bien_None, "False")
# Đúng và đúng : True
# Đúng và SAi : Flase
# Đúng hoặc sai : False
# Sai hoặc sai : False
# not True = False -> not in
# not False = True
# b

x = 1
y = 2
z = 3

if x not in danh_sach:

    print("Không có x Trong Danh Sach")

else:
    print("Có x Trong Danh Sach")

if y in danh_sach:

    print("Có y Trong Danh Sach")

else:
    print("Không Có y Trong Danh Sach")