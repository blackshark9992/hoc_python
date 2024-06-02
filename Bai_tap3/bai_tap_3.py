x = {'Person_1': [10, 6, 5, 9, 4], 'Person_2': [7, 8, 2, 10, 3], 'Person_3': [0, 7, 0, 4, 6],
     'Person_4': [4, 4, 4, 10, 6], 'Person_5': [9, 8, 5, 3, 4], 'Person_6': [7, 4, 2, 6, 9],
     'Person_7': [1, 3, 0, 5, 3], 'Person_8': [3, 3, 2, 1, 8], 'Person_9': [3, 4, 3, 8, 5],
     'Person_10': [10, 7, 8, 3, 10], 'Person_11': [0, 1, 9, 3, 8], 'Person_12': [4, 10, 3, 4, 10],
     'Person_13': [7, 0, 6, 5, 6], 'Person_14': [7, 9, 9, 2, 6], 'Person_15': [9, 1, 0, 7, 8],
     'Person_16': [7, 8, 9, 7, 6], 'Person_17': [1, 4, 1, 10, 6], 'Person_18': [8, 9, 7, 0, 2],
     'Person_19': [1, 2, 5, 4, 6], 'Person_20': [9, 1, 6, 2, 10], 'Person_21': [4, 9, 0, 3, 10],
     'Person_22': [3, 3, 9, 3, 7], 'Person_23': [7, 4, 10, 7, 9], 'Person_24': [5, 9, 4, 8, 3],
     'Person_25': [1, 7, 10, 6, 5], 'Person_26': [5, 0, 3, 2, 10], 'Person_27': [9, 3, 6, 3, 8],
     'Person_28': [10, 7, 7, 8, 1], 'Person_29': [0, 5, 6, 3, 2], 'Person_30': [8, 2, 4, 3, 2],
     'Person_31': [9, 6, 9, 10, 4], 'Person_32': [1, 2, 7, 7, 8], 'Person_33': [5, 1, 5, 7, 3],
     'Person_34': [10, 3, 10, 8, 10], 'Person_35': [9, 0, 2, 0, 3], 'Person_36': [4, 3, 3, 4, 8],
     'Person_37': [2, 9, 2, 9, 8], 'Person_38': [5, 4, 1, 3, 5], 'Person_39': [5, 5, 3, 8, 6],
     'Person_40': [9, 3, 10, 10, 10]}

# Tìm những người có tổng điểm lớn hơn > 20,
# Tren 20 được học lực trung bình, trên 30 học lực khá, trên 40 học lực giỏi.
# #In ra danh sách những người đó format [{"Ten": ten, "Tong Diem": tong diem, "hoc_luc": hoc_loc}, {....
# ds_cantim = []
# for per,d in x.items():
#      moi = {
#           "Họ Tên" : per,
#           "Tổng Điểm": d
#      }
#      if sum(d) > 20 and sum(d) <= 30:
#           moi["Học Lực"] = "Trung Bình"
#           ds_cantim.append(moi)
#      elif sum(d) > 30 and sum(d) <= 40:
#           moi["Học Lực"] = "Khá"
#           ds_cantim.append(moi)
#      elif sum(d) > 40:
#           moi["Học Lực"] = "Giỏi"
#           ds_cantim.append(moi)
# print(ds_cantim)

# # Tìm những người có 3/5 đầu điểm > 5.
ds_cantim = []

for nguoi,ds_diem in x.items():
     dem = 0
     ds_tim = {
          "Tên" : nguoi,
          "Danh Sách Điểm" : ds_diem
     }
     for d in ds_diem:
          if d > 5:
               dem += 1
               if dem == 3:
                    break
               # print(dem)
     if dem == 3:
          ds_cantim.append(ds_tim)
print(ds_cantim)
