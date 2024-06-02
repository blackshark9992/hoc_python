# x = int(input("x:"))
# y = int(input("y:"))
# print("hiệu của 2 số là : ", x-y)
# x = 5
# y = 5
# # Tính Hiệu bằng
# print("Tổng của =", x+y)
# if x+y > 0:
#   print("Tổng lớn hơn 0")
# elif x+y ==0:
#   print("Tổng bằng 0")
# else:
#   print(" Tổng nhỏ hơn 0")


# # Tính Hiệu bằng
# print("Hiệu bằng =", x-y )
# if x-y > 0:
#   print("Hiệu lớn hơn 0")
# elif x-y ==0:
#   print("Hieu bằng 0")
# else:
#   print("Hiệu nhỏ hơn 0")

#  # Tính Thương bằng
# print("Thương bằng =", x/y )
# if x/y > 0:
#   print("Thương lớn hơn 0")
# elif x/y ==0:
#   print("Thương bằng 0")
# else:
#   print("Thương nhỏ hơn 0")
# # Tính Tích bằng
# print("Tích bằng =", x*y )
# if x*y > 0:
#   print("Tích lớn hơn 0")
# elif x*y ==0:
#   print("Tích bằng 0")
# else:
#   print("Tích nhỏ hơn 0")

# # List  :
# list_var = [ 1, "text", 0.0, True, 154, "avc"]
# print(list_var)
# print("Tìm Phần Từ Trong list: " , list_var[3] , list_var[1] , list_var[5])
# # Tìm vị trí trong list : list_var.index(giá trị)

# print("Vị Trí số muốn tìm" , list_var.index(0.0))

# # list.append(giá trị) : thêm giá trị vào cuối list
# list_var.append("abc")
# print(list_var)

# # list.insert(vị trí, giá trị) : thêm giá trị
# list_var.insert(2, 12344)
# print(list_var)
# list.coun(giá trị) : đếm số lượng giá trị trong list
# list.clear()  xóa phần tử trong list
# list_var.clear()
# print(list_var)

# list2 = list_var.copy()
# print(list2)
# print(list_var)
# list.pop() : xóa phần tử ở vị trí khỏi list.
# x = list_var.pop(3)
# print("phân tử được xóa: " , x)
# print(list_var)
# # list.remove(giá trị) : xóa giá trị trong list
# list_var = [ 1, "text", 0.0, True, 154, "avc"]
# print(list_var)
# list_var.remove("text")
# print(list_var)

# list_thutu = [653,2,9783,4,5,343,7,8,11,10]
# print(list_thutu)
# list_thutu.sort(reverse=True) sắp xếp list (True giảm dần ) Flase Tăng dần)
# print(list_thutu)
# list_1 = [8,2]
# list_2 = [9,4]
# list_3 = list_1 + list_1

# print(list_3)

# list1 = list_1 * 3
# print("list_1 " , list1)
# print("list_2 " , list_2)
# print("list_3 " , list_3)

# x = "thị"
# y = "ierq"
# z = x* 2
# print(z)


# Tạo 1 list [5,3,4,0,6, 15, 18]
# Lấy ra phần tử thứ 2.
# Thêm phần tử 7 vào cuối
# THêm phần tử 100 vào vị trị 1
# THêm phần tử 100 vào vị trị 2
# Xóa phần tử 5
# Đếm phần tử 100 trong list
# Lấy ra và xóa phần tử thứ 4.
# Sắp xếp lại list
# Clear list.

# # Bài làm


# list= [5,3,4,0,6, 15, 18]
# print("Phần Tử Thứ 2 là : " , list[2])
# list.append(7)
# print("Thêm Số Vào Cuối list" , list)
# list.insert(1,100)
# print("THêm phần tử 100 vào vị trị 1" , list)
# list.insert(2,100)
# print("THêm phần tử 100 vào vị trị 2" , list)
# list.remove(5)
# print(list)
# print(list.count(100))
# so_da_xoa =list.pop(4)
# print("Số Đã Xóa: " , so_da_xoa)
# list.sort()
# print(list)
# list.clear()
# print(list)

# list_goc = [54,48,22,1,0,87]
# print(list_goc)

# input = input("Nhập Số: ")
# list_goc.append(input)
# print(list_goc)


# x = "bai_tap_1"
# print(x[1])
# list_str = list(x)
# print(list_str)
# list_str.remove('1')
# print(list_str)
# list_str.append('2')
# print(list_str)
# #"text".join(list_str) chèn chuỗi các phần tử trong list vào 1 chuỗi
# a1 = "".join(list_str)
# print(a1)
# list_str = list(a1)
# print(list_str)
# list_str.insert(0,"Python")
# print(list_str)
# a2 = "".join(list_str)
# print(a2)

# list_str = list(a2)
# print(list_str)

# vi_tri_can_them = list_str.index("n") + 1
# # print(x + 1)
# list_str.insert(vi_tri_can_them,"_")
# print(list_str)
# a3 = "".join(list_str)
# print(a3)

# for vòng lặp thực hiện hành động code yêu cầu , vòng lặp qua thứ tự mình muốn.


# list_var = [54,482,63,18,13,7,2,78,12,54,63]
# # varible  in list  => True . False
# # flag : cờ ( so sánh)
# flag = "lfelfo" in list_var
# if flag:
#   print("list_var có phần tử: ")
# else:
#   print("Không tìm Thấy")

# for intem in list_var:
# # Nếu phần từ lớn hơn 5 thì print phần tử đó
#   if intem > 100:
#     print("Số lơn hơn 5" , intem)
#   elif intem == 100:
#     print("Số bằng 100" , intem)

# gia_ban = [50,100,150,170,352,98,76,78,35,48,82]
# # list_result = []
# # gia_goc = 50
# # for gia in gia_ban:
# #   so_them = gia - gia_goc
# #   list_result.append(so_them)
# # print(list_result)
# # print("Số Tiền Lãi: ", sum(list_result),"$")
# # in range ( vị trí bắt đầu - vị trí khết thúc )
# for index in range(0,11):
#   print(index)
#   print(gia_ban[index])
