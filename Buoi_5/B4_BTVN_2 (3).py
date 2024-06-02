import json
import random
data_users = [
    {
        "name": "Nguyễn Văn A",
        "age": 30,
        "address": "Hà Nội",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "bố",
            "mẹ",
            "em gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Trần Thị B",
        "age": 45,
        "address": "TP. Hồ Chí Minh",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Lê Văn C",
        "age": 25,
        "address": "Đà Nẵng",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "bố",
            "mẹ",
            "anh trai"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phạm Thị D",
        "age": 35,
        "address": "Hải Phòng",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "chồng",
            "con gái",
            "cháu"
        ],
        "dang_vien": 1
    },
    {
        "name": "Đặng Quang E",
        "age": 50,
        "address": "Cần Thơ",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "vợ",
            "con trai",
            "con gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Hoàng Thị F",
        "age": 28,
        "address": "Huế",
        "job": "Kỹ sư phần mềm",
        "nguoi_than": [
            "bố",
            "mẹ",
            "chị gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Vũ Văn G",
        "age": 40,
        "address": "Quảng Ninh",
        "job": "Giáo viên",
        "nguoi_than": [
            "vợ",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phùng Thị H",
        "age": 55,
        "address": "Nghệ An",
        "job": "Giáo viên",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Bùi Văn I",
        "age": 60,
        "address": "Bình Định",
        "job": "Giáo viên",
        "nguoi_than": [
            "vợ",
            "con trai",
            "cháu"
        ],
        "dang_vien": 0
    },
    {
        "name": "Đỗ Thị J",
        "age": 32,
        "address": "Nam Định",
        "job": "Giáo viên",
        "nguoi_than": [
            "bố",
            "mẹ",
            "em trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Nguyễn Thị K",
        "age": 27,
        "address": "Hà Giang",
        "job": "Giáo viên",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Trần Văn L",
        "age": 50,
        "address": "Hà Nam",
        "job": "Giáo viên",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Lê Thị M",
        "age": 33,
        "address": "Bắc Ninh",
        "job": "Bác sĩ",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Phạm Văn N",
        "age": 28,
        "address": "Bắc Giang",
        "job": "Bác sĩ",
        "nguoi_than": [
            "bố",
            "mẹ",
            "em gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Đặng Thị O",
        "age": 45,
        "address": "Quảng Nam",
        "job": "Bác sĩ",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Hoàng Văn P",
        "age": 50,
        "address": "Quảng Ngãi",
        "job": "Bác sĩ",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Vũ Thị Q",
        "age": 36,
        "address": "Bến Tre",
        "job": "Bác sĩ",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phùng Văn R",
        "age": 40,
        "address": "Tây Ninh",
        "job": "Bác sĩ",
        "nguoi_than": [
            "vợ",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Bùi Thị S",
        "age": 37,
        "address": "Tiền Giang",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Đỗ Văn T",
        "age": 29,
        "address": "Vĩnh Long",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "bố",
            "mẹ",
            "em trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Nguyễn Thị U",
        "age": 31,
        "address": "Long An",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Trần Văn V",
        "age": 42,
        "address": "Kiên Giang",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Lê Thị W",
        "age": 34,
        "address": "Đồng Tháp",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phạm Văn X",
        "age": 38,
        "address": "An Giang",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "vợ",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Đặng Thị Y",
        "age": 44,
        "address": "Cà Mau",
        "job": "Nhân viên văn phòng",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 1
    },
    {
        "name": "Hoàng Văn Z",
        "age": 41,
        "address": "Sóc Trăng",
        "job": "Doanh nhân",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Vũ Thị AA",
        "age": 50,
        "address": "Bạc Liêu",
        "job": "Doanh nhân",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phùng Văn BB",
        "age": 53,
        "address": "Hậu Giang",
        "job": "Doanh nhân",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 0
    },
    {
        "name": "Bùi Thị CC",
        "age": 48,
        "address": "Trà Vinh",
        "job": "Doanh nhân",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Đỗ Văn DD",
        "age": 55,
        "address": "Ninh Bình",
        "job": "Doanh nhân",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Nguyễn Thị EE",
        "age": 47,
        "address": "Thái Bình",
        "job": "Doanh nhân",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 0
    },
    {
        "name": "Trần Văn FF",
        "age": 29,
        "address": "Thanh Hóa",
        "job": "Luật sư",
        "nguoi_than": [
            "vợ",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    },
    {
        "name": "Lê Thị GG",
        "age": 31,
        "address": "Quảng Trị",
        "job": "Luật sư",
        "nguoi_than": [
            "chồng",
            "con trai",
            "con gái"
        ],
        "dang_vien": 0
    },
    {
        "name": "Phạm Văn HH",
        "age": 34,
        "address": "Hòa Bình",
        "job": "Doanh nhân",
        "nguoi_than": [
            "chồng",
            "con gái",
            "con trai"
        ],
        "dang_vien": 1
    }
]
ket_qua = {}
# # Chữa bài
ket_qua_bai_1 = [data_user for data_user in data_users if data_user['age'] > 30]

ket_qua["bai_1"] = ket_qua_bai_1
with open("tinh_trang.json", "w") as f:
    json.dump(ket_qua, f, indent=4)

ket_qua_bai_2 = [data_user for data_user in data_users if data_user['job'] == "Doanh nhân"]
ket_qua["bai_2"] = ket_qua_bai_2
with open("tinh_trang.json", "w") as f:
    json.dump(ket_qua, f, indent=4)
#
# # Lọc ra danh sách những người đang làm Luật Sư và Kỹ sư phần mềm
ket_qua_bai_3 = [data_user for data_user in data_users if data_user['job'] == "Luật sư"
                 or data_user['job'] == "Kỹ sư phần mềm"]
ket_qua["bai_3"] = ket_qua_bai_3
with open("tinh_trang.json", "w") as f:
    json.dump(ket_qua, f, indent=4)

# for data_user in  data_users:
#     if data_user['job'] == "Luật sư" or data_user['job'] == "Kỹ sư phần mềm":
#         print(data_user)
# Hiển thị thông tin của chị "Lê Thị GG"
# for data_user in  data_users:
#     if data_user["name"] == "Lê Thị GG":
#         print(data_user['name'],"\n","Tuổi: ",data_user['age'],"\n","Nơi ở: ",
#               data_user["address"],"\n","Nghề Nghiệp: ",data_user['job'])
ket_qua_bai_4 = [data_user for data_user in data_users if data_user["name"] == "Lê Thị GG"]
ket_qua["bai_4"] = ket_qua_bai_4
with open("tinh_trang.json", "w") as f:
    json.dump(ket_qua, f, indent=4)
# Hiển thị người thân của Phùng Văn BB
# for data_user in  data_users:
#     if data_user["name"] == "Phùng Văn BB":
#         print(data_user['name'],"\n","Người Thân Có: ",data_user['nguoi_than'])
ket_qua_bai_5 = [data_user for data_user in data_users if data_user["name"] == "Phùng Văn BB"]
ket_qua["bai_5"] = ket_qua_bai_5
with open("tinh_trang.json", "w") as f:
    json.dump(ket_qua, f, indent=4)
# Hiển thị thông tin của người là đảng viên ( "dang_vien": 1)
# for data_user in  data_users:
#     if data_user["dang_vien"] == 1:
#         print(data_user['name'],"\n","Người Thân Có: ",data_user['nguoi_than'])
# Hiển thị danh sách những người đã kết hôn ( có vợ hoặc có chồng hoặc có  con gái/ con trai).
                # nếu người đó đã kết hôn thêm key "da_ket_hon": 1, còn không thì  "da_ket_hon": 0.
                #  Ví dụ
                # {
                #         "name": "Phạm Văn HH",
                #         "age": 34,
                #         "address": "Hòa Bình",
                #         "job": "Doanh nhân",
                #         "nguoi_than": [
                #             "chồng",
                #             "con gái",
                #             "con trai"
                #         ],
                #         "dang_vien": 1,
                #         "da_ket_hon": 1
                #     }

for data_user in  data_users:
    ds_tinh_trang = data_user["nguoi_than"]
    for ng_than in ds_tinh_trang:
        if ng_than in ["chồng","vợ","con gái", "con trai"]:
            data_user["da_ket_hon"] = 1
            break
        else:
            data_user["da_ket_hon"] = 0
# print(data_users)
# # Lưu thông tin vừa sửa vào file json có tên là data_uses.json

with open("tinh_trang.json", "w") as f:
    json.dump(data_users, f )

print(data_users)