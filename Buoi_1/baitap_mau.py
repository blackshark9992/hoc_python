danh_sach_vong_lap = [2, 1]
for item in danh_sach_vong_lap:
    try:
        danh_sach = ["Mận","táo","Dưa","Táo","ổi","Mang Cụt",1,2,0.55,85,0.5,0.69,3,4,5,6,7,"Mang Cụt",
                     8,8,7,6,5,4,3,2,1,0.25,0.58,0.25,0.58,0.66,0.14,0.66,0.14,"Mận","táo","Dưa","Táo","ổi"]
        print("----->Danh Sách Lựa Chọn<------")
        print("1.Danh Sách Số Nguyên.")
        print("2.Danh Sách Chuỗi.")
        print("3.Danh Sách Số Thập Phân.")
        print("4.Danh Sách Mới Loại Bỏ Trùng Lặp.")
        print("5.Thoát")
        lc = int(input("Mời Nhập Lựa Chọn : ",))
        danh_sach_so_tu_nhien = []
        danh_sach_str= []
        danh_sach_fl = []
        danh_sach_khong_trung_lap = []
        for phan_tu in danh_sach:
            if type(phan_tu) == int:
                danh_sach_so_tu_nhien.append(phan_tu)
            elif type(phan_tu) == str:
                danh_sach_str.append(phan_tu)
            elif type(phan_tu) == float:
                danh_sach_fl.append(phan_tu)
            if phan_tu not in danh_sach_khong_trung_lap:
                danh_sach_khong_trung_lap.append(phan_tu)
        if lc == 1:
            print(danh_sach_so_tu_nhien)
        elif lc == 2:
            print(danh_sach_str)
        elif lc == 3:
            print(danh_sach_fl)
        elif lc == 4:
            bien = list(set(danh_sach))
            print(bien)
        elif lc == 5:
            break
        else:
            print("---------------chức năng không hợp lệ.---------------")
    except Exception as ex:
         print("Lỗi", ex)
    danh_sach_vong_lap.append(1)