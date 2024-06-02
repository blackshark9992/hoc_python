danh_sach_hoa_don = [{'Time': '08/05/2024', 'ban': 4, 'ghe': 11, 'tu': 19},
                     {'Time': '09/05/2024', 'ban': 1, 'ghe': 16, 'tu': 3},
                     {'Time': '10/05/2024', 'ban': 12, 'ghe': 18, 'tu': 13},
                     {'Time': '11/05/2024', 'ban': 12, 'ghe': 19, 'tu': 11},
                     {'Time': '12/04/2024', 'ban': 19, 'ghe': 12, 'tu': 16},
                     {'Time': '13/05/2024', 'ban': 18, 'ghe': 18, 'tu': 3},
                     {'Time': '14/05/2024', 'ban': 8, 'ghe': 14, 'tu': 19},
                     {'Time': '15/05/2024', 'ban': 19, 'ghe': 10, 'tu': 4},
                     {'Time': '16/05/2024', 'ban': 18, 'ghe': 18, 'tu': 14},
                     {'Time': '17/05/2024', 'ban': 454, 'ghe': 4, 'tu': 18},
                     {'Time': '18/05/2024',  'ban': 150, 'ghe': 20, 'tu': 2},
                     {'Time': '19/05/2024', 'ban': 18, 'ghe': 16, 'tu': 2},
                     {'Time': '20/05/2024', 'ban': 1, 'ghe': 7, 'tu': 14},
                     {'Time': '21/04/2024', 'ban': 1, 'ghe': 14, 'tu': 18},
                     {'Time': '22/05/2024', 'ban': 3, 'ghe': 20, 'tu': 6},
                     {'Time': '23/05/2024', 'ban': 6, 'ghe': 11, 'tu': 16},
                     {'Time': '24/05/2024', 'ban': 15, 'ghe': 20, 'tu': 2},
                     {'Time': '25/04/2024', 'ban': 16, 'ghe': 8, 'tu': 4},
                     {'Time': '26/05/2024', 'ban': 1, 'ghe': 17, 'tu': 14},
                     {'Time': '27/05/2024', 'ban': 16, 'ghe': 20, 'tu': 2}]
from datetime import datetime

     # Cách 1
# Hiển Thị Thông tin hóa đơn sau ngày 14/05/2024 và trước 24/05/2024:
# Cách làm tuy đổi chuỗi ra biến Date
# ngay = datetime.now()
# print(ngay)
# print(ngay.year)
# print(ngay.month)
# print(ngay.day)
# print(ngay.hour)
# print(ngay.minute)
# print(ngay.microsecond
# ngay_goc = '20/05/2024'
# ngay_gio = datetime.strptime(ngay_goc, "%d/%m/%Y")
# so_san_pham_ban = []
# for hoa_don in danh_sach_hoa_don:
#     ngay_tim = hoa_don['Time']
#     ngay_tim_datime = datetime.strptime(ngay_tim,"%d/%m/%Y")
#     if ngay_tim_datime > ngay_gio:
#
#         # print(hoa_don['Time']
#
#
# # Hiển thị tổng số sản phẩm sau ngày 20/05/2024
# #         print("Tổng số sản phẩm: ",hoa_don['Time'] ,
# #               hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
# # Hiển thị Tổng số sản phẩm bản nhiều nhất
#
#         tong_sp = hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu']
#         so_san_pham_ban.append(tong_sp)
# max_sp = max(so_san_pham_ban)
# for hoa_don in danh_sach_hoa_don:
#     ngay_tim = hoa_don['Time']
#     ngay_tim_datime = datetime.strptime(ngay_tim,"%d/%m/%Y")
#     tong_sp = hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu']
#     if ngay_tim_datime > ngay_gio:
#         if tong_sp == max_sp:
#             print(hoa_don['Time'],tong_sp)
# Cách 2:
ngay_goc_start = '14/05/2024'
ngay_goc_end = '24/05/2024'
ngay_gio_start = datetime.strptime(ngay_goc_start, "%d/%m/%Y")
ngay_gio_end = datetime.strptime(ngay_goc_end, "%d/%m/%Y")
danh_sach_hoa_don_new = []
for hoa_don in danh_sach_hoa_don:
    ngay_tim = hoa_don['Time']
    ngay_tim_datime = datetime.strptime(ngay_tim,"%d/%m/%Y")
    if ngay_tim_datime > ngay_gio_start and ngay_tim_datime < ngay_gio_end:
        danh_sach_hoa_don_new.append(hoa_don)
print(danh_sach_hoa_don_new)
# # Cách 1: Tìm max thông qua list
list_so_tu_ban = []
for hoa_don in danh_sach_hoa_don_new:
    list_so_tu_ban.append(hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
max_so_tu_ban = max(list_so_tu_ban)
for hoa_don in danh_sach_hoa_don_new:
    if hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'] == max_so_tu_ban:
        print(hoa_don['Time'], ":", hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
