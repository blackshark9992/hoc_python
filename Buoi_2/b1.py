gmail = [
    "nguyenanh@gmail.com1",  # Đúng
    "leminhthu@gmail.com1",  # Đúng
    "hoanganh@ymail.com",  # Sai
    "thanhnam@gmail.com1",  # Đúng
    "bichlien@hotmail.com",  # Sai
    "giang.nguyen@gmail.com",  # Đúng
    "kimlien@gmail.com1",  # Đúng
    "minh.tu@gmail",  # Sai
    "viet.anh.pham@gmail.com",  # Đúng
    "thuha@gmail.com",  # Đúng
    "phuonglinh@gmailcom",  # Sai
    "minhhue@gmail.com",  # Đúng
    "ducanh.email@gmail.com",  # Đúng
    "huyen.my@gmail.com",  # Đúng
    "tranthanh@gmail.com",  # Đúng
    "huongthao@gmail.com",  # Đúng
    "ngocthuy@gmail.com",  # Đúng
    "tuan.kiet@gmail.com",  # Đúng
    "sonlam@gmail.com",  # Đúng
    "linhchi@gmail.com",  # Đúng
    "quang.vu@gmail.com",  # Đúng
    "tampham@gmail.com",  # Đúng
    "minh.quan@gmail",  # Sai
    "thanh.hoa@gmail.com",  # Đúng
    "linh@gmail.com",  # Đúng
    "trung@gmail.com",  # Đúng
    "khanhhoa@gmail.com",  # Đúng
    "phuongnam@gmail.com",  # Đúng
    "tuongvy@gmailcom",  # Sai
    "haiphong@gmail",  # Sai
    "trungvu@gmail.com",  # Đúng
    "linhdan@live.com",  # Sai
    "duy.khoi@outlook.com",  # Sai
    "thuyhang@gmail.com",  # Đúng
    "hai.tran@gmail",  # Sai
    "lananh@yahoo.com",  # Sai
    "anhthu@gmail.com",  # Đúng
    "manhtri@gmail.com",  # Đúng
    "cuongvulive@gmail",  # Sai
    "lanphuong@icloud.com"  # Sai
]
yahoo = [
    "nguyenminh@yahoo.com",  # Đúng
    "lethibao@yahoo.com",  # Đúng
    "tranthanhtu@yahoo.com",  # Đúng
    "huynhphuong@yahoo.com",  # Đúng
    "ngoctrai@yahoo.com",  # Đúng
    "hoangmai@yahoo.com",  # Đúng
    "thanhson@yahoo.com",  # Đúng
    "duongkhanh@yahoo.com",  # Đúng
    "ngocanh@yahoo.com",  # Đúng
    "haiphuong@yahoo.com",  # Đúng
    "vietanh@yahoo,com",  # Sai
    "minhphuong@yahoocom",  # Sai
    "khanhhoa@yahoo-com",  # Sai
    "thuha@ yahoo.com",  # Sai
    "leminh@yahoo. com",  # Sai
    "phuonglinh@yahoo.com1",  # Sai
    "hoangnam@yahoo.comabc",  # Sai
    "anhthu@yahoo,com",  # Sai
    "minhvu@yahoo,com",  # Sai
    "baolinh@yhoo.com"  # Sai
]
duoi_email_can_lay = ['@gmail.com', 'yahoo.com']
mail_tong = gmail + yahoo
mail_dung = []
for mail in mail_tong :
    # if "@gmail.com" in mail:        # Chỉ nhận giá trị có trong chuỗi
    #     mail_dung.append(mail)
                 # Gộp 2 mail
    # if mail[len(mail)-len('@gmail.com'):] == '@gmail.com':    # bắt chuỗi kết thúc bằng @gmail.com
    #     mail_dung.append(mail)
    # elif mail[len(mail)-len('yahoo.com'):] == 'yahoo.com':
    #     mail_dung.append(mail)
                      # Cách 2
    #  if mail[len(mail)-len('gmail.com'):] == 'gmail.com' or mail[len(mail)-len('yahoo.com'):] == 'yahoo.com':
    #      mail_dung.append(mail)
    #                       Cách 3 : tạo thêm 1 list duôi mail cần lấy
    for duoi_email_can_lay in  mail
print(mail_dung)
duoi_emails = ['@yahoo.com', '@gmail.com', '@icloud.com']

emails = ['cuong@gmail.com', 'cuong@yahoo.com', 'cuong@icloud.com', 'cuong@fake.com']

mail_dung = []

for email in emails:
    for duoi_email in duoi_emails:
        if email[len(email) - len(duoi_email):] in duoi_emails:
            mail_dung.append(email)
            break
print(mail_dung)
# mail = 'okhokre@gmail.com'
#
# if mail[len(mail)-len('@gmail.com'):] == '@gmail.com' :
#     print("Mail Đúng")
# else:
#     print("Mail Sai.")

 # không break
# for email in emails:
#     for duoi_email in duoi_emails:
#         x = email[len(email) - len(duoi_email):]
#         if email[len(email) - len(duoi_email):] in duoi_emails:
#             mail_dung.append(email)
# print(list(set(mail_dung)))

# for email in emails:
# #     for duoi_email in duoi_emails:
# #         x = email[len(email) - len(duoi_email):]
# #         if email[len(email) - len(duoi_email):] in duoi_emails:
# #             mail_dung.append(email)
# # print(list(set(mail_dung)))


