var_dict = {
    "key": "value",
    "key_1": 3,
    "Cuong": ["Cuong", 18, "Hung Yen"],
    "Long": "Bi",
    "thong_tin_2_ae": {
        "Tu": 1992,
        "Long": 2003
    }
}
# Sửa/ thêm value của key bất kì var_dict[key] = value
# var_dict["abcde"] = "value_2"
# var_dict["key"] = "số 1"
# print(var_dict)

# Lấy value của key:  var_dict[key]
# print(var_dict["Long"])

# Sửa/ thêm value của key bất kì var_dict[key] = value
# var_dict["abcd"] = "value_2"

# Lấy 1 list key của var_dict
# print(var_dict.keys())

# lấy 1 list value của var_dict
# print(var_dict.values())

# lấy value của key, nhưng an toàn hơn  var_dict[key]
# print(var_dict.get("thong_tin_3_ae", "khong_co"))

# Lấy ra value của key và xóa cặp key-value khỏi dict
# x = var_dict.pop("abcde")

# Lấy và xóa phần tử ở cuối dict
# var_dict.popitem()

# Biến var_dict thành 1 dict trống
# var_dict.clear()

# giống list, tạo  dict mới giống dict cũ.
# x = var_dict.copy()

# lấy ra 1 list các list [key, value]
# print(var_dict.items())
# for phan_tu in var_dict.items():

# Cập nhật dict cũ theo dict mới: trùng key thì thay đổi value ( value theo dict_2), không có thì thêm mới.
# var_dict_2 = {"key": 5, "key1": 6}
# var_dict.update(var_dict_2)
# print(var_dict)

# Gán key mặc định value mới nếu chưa có. CÒn nếu trong dict có thì để nguyên
# var_dict.setdefault("thong_tin_2_ae", "abc")
# print(var_dict.pop())

#  Đếm phần tử trong 1 list
# a = [4, 7 , 8,9 , 10]
#
# dem = 0
# for phan_tu in a:
#     if phan_tu > 5:
#         dem += 1
#         print(dem)
#         if dem >=3:
#             print("A có 3/5 đầu điểm > 5")
#             break

# Cach 2: Dem
# dem = 0
# for phan_tu in a:
#     if phan_tu > 5:
#         dem += 1
# print(dem)
# if dem >= 3:
#     print("oke")


#
# Cách 1: Tìm max thông qua list
# list_so_tu_ban = []
# for danh_sach in danh_sach_hoa_don:
#     list_so_tu_ban.append(danh_sach['tu'])
# max_so_tu_ban = max(list_so_tu_ban)
# for danh_sach in danh_sach_hoa_don:
#     if danh_sach['tu'] == max_so_tu_ban:
#         print(danh_sach['Time'])

# Cach 2: Tìm max thông qua thuật toán nổi bọt:
# max_so_ban_tu = danh_sach_hoa_don[0]['tu']
# danh_sach_ngay_ban_tu = [danh_sach_hoa_don[0]['Time']]
# for danh_sach in danh_sach_hoa_don:
#     if max_so_ban_tu < danh_sach['tu']:
#         max_so_ban_tu = danh_sach['tu']
#         danh_sach_ngay_ban_tu.clear()
#         danh_sach_ngay_ban_tu.append(danh_sach['Time'])
#     elif max_so_ban_tu == danh_sach['tu']:
#         danh_sach_ngay_ban_tu.append(danh_sach['Time'])
