try:
    danh_sach = ["Mận","táo","Dưa","Táo","ổi","Mang Cụt",1,2,0.55,85,0.5,0.69,3,4,5,6,7,"Mang Cụt",
                 8,8,7,6,5,4,3,2,1,0.25,0.58,0.25,0.58,0.66,0.14,0.66,0.14,"Mận","táo","Dưa","Táo","ổi"]
    print("----->Danh Sách Lựa Chọn<------")
    print("1.Danh Sách Số Nguyên.")
    print("2.Danh Sách Chuỗi.")
    print("3.Danh Sách Số Thập Phân.")
    print("4.Danh Sách Mới Loại Bỏ Trùng Lặp.")
    lc = int(input("Mời Nhập Lựa Chọn : ",))
# break : Ngắt Vòng lặp for /white -> chú ý  1 break ngắt 1 for/ white gần nhất

    if lc == 1:
        # 1) Lọc danh sách số tự nhiên#
        danh_sach_so_tu_nhien = []
        for phan_tu in danh_sach:
            if type(phan_tu) == int:
                danh_sach_so_tu_nhien.append(phan_tu)
        print(danh_sach_so_tu_nhien)
    elif lc == 2:
        danh_sach_chuoi = []
        for phan_tu in danh_sach:
            if type(phan_tu) == str:
                danh_sach_chuoi.append(phan_tu)
        print(danh_sach_chuoi)
    elif lc == 3:
        danh_sach_tp = []
        for phan_tu in danh_sach:
            if type(phan_tu) == float:
                danh_sach_tp.append(phan_tu)
        print(danh_sach_tp)
    elif lc == 4:
        # bien = set(danh_sach))
        # print(bien)
        bien = list(set(danh_sach))
        print(bien)
        # danh_sach_khong_trung = []
        #
        # for phan_tu in danh_sach:
        #     if phan_tu not in danh_sach_khong_trung:
        #         danh_sach_khong_trung.append(phan_tu)
        # print(danh_sach_khong_trung)
    else:
        print("chức năng không hợp lệ.")
except Exception as ex:
     print("Lỗi", ex)

