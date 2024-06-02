var_dict = {'An': 25, 'Binh': 30, 'Cuong': 28, 'Dung': 22, 'Hai': 35, 'Hoa': 20, 'Hung': 45, 'Khanh': 18, 'Lan': 40,
            'Linh': 15, 'Mai': 32, 'Minh': 50, 'Nam': 27, 'Nga': 33, 'Nhan': 55, 'Phong': 38, 'Quan': 42, 'Quyen': 23,
            'Son': 11, 'Tam': 47, 'Thang': 36, 'Thanh': 29, 'Thao': 16, 'Thuy': 52, 'Tung': 21, 'Tuyen': 58,
            'Tuyet': 14, 'Van': 26, 'Vy': 34, 'Xuan': 19, 'Yen': 37, 'Khoa': 44, 'Khuong': 49, 'Lam': 24, 'Le': 31,
            'Long': 39, 'My': 56, 'Nghia': 53, 'Nhung': 9}

# Lấy ra tuổi của "An", "Minh", "Nam"

print("Tuổi Của An ,Minh, Nam Là: " ,var_dict["An"],var_dict["Minh"],
      var_dict["Nam"])
# Thêm 1 cặp  Tên: tuổi mới chưa có trong dict
var_dict["Pham_Long"] = 15
# print(var_dict)
# Sửa tuổi của 'Van' là 10
var_dict["Van"] = 10
# print(var_dict)
# Lấy ra tuổi của 'Thang', nếu không có thì trả ra 10.
print(var_dict.get("Thang", 10))
# Xóa thông tin của 'Nga' ra khỏi dict
var_dict.pop("Nga")
print(var_dict)
# Tạo 1 var_new mới bằng var_dict
var_new = var_dict.copy()
print(var_new)
# Clear var_new
var_new.clear()
# print(var_new)
# Sử dụng Setdefault cho 'Thuan' có tuổi là 50.
var_dict.setdefault("Thuan", 50)
# print(var_new)
# Sử dụng update với dict khác là: {'Vy': 34, 'XuanHinh': 18, 'Yen': 35, 'Khoa': 40, 'Khuong': 55}
new2 ={'Vy': 34, 'XuanHinh': 18 , 'Yen': 35,'Khoa': 40, 'Khuong': 55 }
var_dict.update(new2)
# print(var_dict)
# # In ra list key của dict
# for a in var_dict.keys():
#     print(a)
# # In ra list value của dict
# for b in var_dict.values():
#     print(b)
# # In ra list key-value của dict
# for c,d in var_dict.items():
#     # print(c,d)
# #       # print(ten, tuoi)
#     # elif tuoi >= 21 and tuoi <= 40:
#     #     print(ten,tuoi)
#     # elif tuoi >= 41 and tuoi <= 60:
#     #     print(ten,tuoi)
# # Tạo 1 list mới gồm những người 0- 20 tuổi
#
# # Tạo 1 list mới gồm những người từ 20-40 tuổi
# # Tạo 1 list mới gồm những người từ 40-60 tuổi
danh_sach_0_20 =[]
danh_sach_21_40 = []
danh_sach_41_60 = []
for ten,tuoi in var_dict.items():
    x = {
        "Họ Tên": ten,
        "Số Tuổi": tuoi
    }
    if tuoi <= 20 :
        x["Độ Tuổi"] = "Người Trẻ"
        # # x.setdefault(do_tuoi)
        danh_sach_0_20.append(x)
    elif tuoi >= 21 and tuoi <= 40:
        x["Độ Tuổi"] = "Trung Niên"
        danh_sach_21_40.append(x)
    elif tuoi >= 41 and tuoi <= 60:
        x["Độ Tuổi"] = "Người Già"
        danh_sach_41_60.append(x)
print(danh_sach_0_20)
print(danh_sach_21_40)
print(danh_sach_41_60)


