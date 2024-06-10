import random
import string
import unicodedata
import pandas as pd
from datetime import datetime, timedelta
import requests
import base64
import uuid
import os
from PIL import Image
import pytesseract

# Đặt đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def generate_password():
    password = ''.join(random.choices(string.ascii_lowercase, k=6))
    password += random.choice(string.ascii_uppercase)
    password += ''.join(random.choices(string.digits, k=2))
    special_characters = "@#$%*_"
    password += random.choice(special_characters)
    return password

def generate_username(full_name):
    name_parts = full_name.split()
    last_name = name_parts[0] if name_parts else ""
    first_name = name_parts[-1] if name_parts else ""
    random_number = random.randint(10, 999)
    username = f"{remove_accents(last_name.lower())}{remove_accents(first_name.lower())}{random_number}"
    return username

def generate_random_full_name():
    # Danh sách các họ và tên đệm, tên thật phổ biến
    last_names = [
       "PHAM","NGUYEN","TRAN","LE","HOANG","HUYNH","VU","VO","PHAN","TRUONG","BUI","DANG","DO","NGO",
        "HO","DUONG","DINH","THEN","LY","TA","TRINH","LY",
    ]
    middle_names = [
        "DINH", "THANH", "DUC", "MINH", "THINH", "HONG", "NGOC", "HAI",
        "HOANG", "QUOC", "XUAN", "HUU", "TRONG", "NHAN", "DUY", "THE", "DAT", "ANH",
        "BAO", "NGUYEN", "THINH", "HA", "TUNG", "CONG", "TUAN", "HUNG", "PHUONG", "TAM",
        "TAN", "VIET", "TRUNG", "LAM", "PHUC", "HUNG", "VAN", "THINH", "DUC", "THI",
        "TIEN", "THANH", "HAI", "THANH", "THI", "DUY", "TRUONG", "DUC", "THI", "NHAT",
        "QUANG", "HUY", "HA", "TAN", "TRI", "HONG", "MINH", "HOANG", "NGOC", "TUAN",
        "TAM", "ANH", "NGUYEN", "BAO", "TRUNG", "HUNG", "DUC", "DINH", "THANH", "THAI",
        "VAN", "CONG", "VIET", "NAM", "HOANG", "PHUONG", "HA", "DUC", "THINH", "HUY",
        "QUOC", "THAI", "THANH", "TRI", "TUNG", "DUY", "NHAT", "HUU", "TIEN", "HAI",
        "LAM", "TU", "VAN", "MINH", "NGOC", "HONG", "HUNG", "THANH", "TAM", "HOA",
        "ANH", "THINH", "TRONG", "THANG", "HOANG", "DUC", "BAO", "QUANG", "DUY", "THANH",
        "HUNG", "PHUC", "TUAN", "HAI", "NAM", "TIEN", "THI", "HUNG", "DINH", "VAN",
        "MINH", "TRUNG", "THANH", "DUC", "TAN", "QUOC", "HONG", "NGUYEN", "VIET", "HUY",
        "PHUONG", "TRONG", "HA", "HUU", "ANH", "BAO", "NGOC", "THANH", "DUC", "TAM",
        "TIEN", "THINH", "THANG", "TRUNG", "MINH", "HAI", "QUANG", "HOANG", "THANH", "TUAN",
        "HUNG", "THANH", "HUY", "DUC", "VAN", "TRI", "PHUC", "DINH", "THAI", "HONG",
        "BAO", "CONG", "DUY", "NHAT", "DUC", "NAM", "TUNG", "HOANG", "THINH", "TIEN",
        "HA", "ANH", "HAI", "HUNG", "THI", "TAM", "THANH", "VIET", "TRUNG", "MINH",
        "HUU", "THANH", "DINH", "PHUONG", "QUOC", "TUAN", "HUY", "DUC", "THANG",
        "HOANG"
    ]
    middle_names2 = [
        "AI", "AN", "ANH", "AO", "AU", "AU DUONG", "BA", "BAC", "BAN", "BACH", "BANG",
        "BANH", "BAO", "BE", "BI", "BIEN", "BINH", "BO", "CA", "CAI", "CAM", "CANH",
        "CAO", "CAP", "CAT", "CAN", "CHE", "CHAU", "CHU", "CHANG", "CHUNG", "CHUONG",
        "CO", "CONG", "CUNG", "CU", "DA", "DANH", "DIEM", "DIEP", "DOAN", "DU", "DUY",
        "DAI", "DAN", "DAM", "DAO", "DANG", "DAC", "DAU", "DEO", "DIEU", "DIEN", "DINH",
        "DOAI", "DON", "DONG", "DO", "DAI", "DUONG", "DUC", "GIA", "GIAO", "GIANG",
        "GIAN", "GIAP", "HUNG", "H'", "H'MA", "HAU", "HA", "HAN", "HANG", "HE",
        "HINH", "HOA", "HOAI", "HOANG PHU", "HONG", "HUA", "HUONG", "HY", "KINH", "KONG",
        "KIEU", "KHA", "KHAI", "KHAU", "KHIEU", "KHOA", "KHONG", "KHU", "KHUAT", "KHUC",
        "KHUONG", "KHUU", "KIM", "LY", "LA", "LANH", "LAC", "LAI", "LANG", "LAM", "LAU",
        "LENG", "LEU", "LIEN", "LIEP", "LIEU", "LINH", "LOAN", "LONG", "LO", "LOC", "LUYEN",
        "LUC", "LU", "LUONG", "LUU", "MA", "MAI", "MAN", "MANG", "ME", "MAC", "MACH", "MANH",
        "MAU", "MINH", "MOC", "MONG", "MUA", "MUC", "MIEU", "NGAC", "NGAN", "NGHIEM",
        "NGHI", "NGO", "NGOC", "NGON", "NGU", "NGUY", "NHAN", "NHAM", "NHU", "NINH", "NONG",
        "ONG", "PHI", "PHO", "PHONG", "PHU", "PHUNG", "PHUONG", "QUAN", "QUANG", "QUACH",
        "QUE", "QUOC", "QUYEN", "SAI", "SAM", "SON", "SU", "SUNG", "SY", "TAN", "TAO", "TA",
        "TANG", "TAT", "TE", "THANG", "THANH", "THAI", "THAO", "THACH", "THAN", "THAM",
        "THAP", "THE", "THI", "THIEU", "THINH", "THIEM", "THOA", "THOI", "THONG", "THUC",
        "TIEU", "TIET", "TIEP", "TINH", "TONG", "TO", "TON", "TON NU", "TON THAT", "TRANG",
        "TRAC", "TRA", "TRAU", "TRI", "TRIEU", "TRINH", "TRUNG", "TUAN", "TU", "TUONG", "TY",
        "UONG", "UAN", "UNG", "VANG", "VAN", "VI", "VINH", "VIEM", "VIEN", "VIET", "VONG",
        "VU", "VUONG", "VUU", "XA", "XUNG", "YEN"
    ]
    first_names = [
        "DINH", "THANH", "DUC", "MINH", "THINH", "HONG", "NGOC", "HAI",
        "HOANG", "QUOC", "XUAN", "HUU", "TRONG", "NHAN", "DUY", "THE", "DAT", "ANH",
        "BAO", "NGUYEN", "THINH", "HA", "TUNG", "CONG", "TUAN", "HUNG", "PHUONG", "TAM",
        "TAN", "VIET", "TRUNG", "LAM", "PHUC", "HUNG", "VAN", "THINH", "DUC", "THI",
        "TIEN", "THANH", "HAI", "THANH", "THI", "DUY", "TRUONG", "DUC", "THI", "NHAT",
        "QUANG", "HUY", "HA", "TAN", "TRI", "HONG", "MINH", "HOANG", "NGOC", "TUAN",
        "TAM", "ANH", "NGUYEN", "BAO", "TRUNG", "HUNG", "DUC", "DINH", "THANH", "THAI",
        "VAN", "CONG", "VIET", "NAM", "HOANG", "PHUONG", "HA", "DUC", "THINH", "HUY",
        "QUOC", "THAI", "THANH", "TRI", "TUNG", "DUY", "NHAT", "HUU", "TIEN", "HAI",
        "LAM", "TU", "VAN", "MINH", "NGOC", "HONG", "HUNG", "THANH", "TAM", "HOA",
        "ANH", "THINH", "TRONG", "THANG", "HOANG", "DUC", "BAO", "QUANG", "DUY", "THANH",
        "HUNG", "PHUC", "TUAN", "HAI", "NAM", "TIEN", "THI", "HUNG", "DINH", "VAN",
        "MINH", "TRUNG", "THANH", "DUC", "TAN", "QUOC", "HONG", "NGUYEN", "VIET", "HUY",
        "PHUONG", "TRONG", "HA", "HUU", "ANH", "BAO", "NGOC", "THANH", "DUC", "TAM",
        "TIEN", "THINH", "THANG", "TRUNG", "MINH", "HAI", "QUANG", "HOANG", "THANH", "TUAN",
        "HUNG", "THANH", "HUY", "DUC", "VAN", "TRI", "PHUC", "DINH", "THAI", "HONG",
        "BAO", "CONG", "DUY", "NHAT", "DUC", "NAM", "TUNG", "HOANG", "THINH", "TIEN",
        "HA", "ANH", "HAI", "HUNG", "THI", "TAM", "THANH", "VIET", "TRUNG", "MINH",
        "HUU", "THANH", "DINH", "PHUONG", "QUOC", "TUAN", "HUY", "DUC", "VAN", "THANG",
        "HOANG"
    ]
    additional_names = [
        "DINH", "THANH", "DUC", "MINH", "THINH", "HONG", "NGOC", "HAI",
        "HOANG", "QUOC", "XUAN", "HUU", "TRONG", "NHAN", "DUY", "THE", "DAT", "ANH",
        "BAO", "NGUYEN", "THINH", "HA", "TUNG", "CONG", "TUAN", "HUNG", "PHUONG", "TAM",
        "TAN", "VIET", "TRUNG", "LAM", "PHUC", "HUNG", "VAN", "THINH", "DUC", "THI",
        "TIEN", "THANH", "HAI", "THANH", "THI", "DUY", "TRUONG", "DUC", "THI", "NHAT",
        "QUANG", "HUY", "HA", "TAN", "TRI", "HONG", "MINH", "HOANG", "NGOC", "TUAN",
        "TAM", "ANH", "NGUYEN", "BAO", "TRUNG", "HUNG", "DUC", "DINH", "THANH", "THAI",
        "VAN", "CONG", "VIET", "NAM", "HOANG", "PHUONG", "HA", "DUC", "THINH", "HUY",
        "QUOC", "THAI", "THANH", "TRI", "TUNG", "DUY", "NHAT", "HUU", "TIEN", "HAI",
        "LAM", "TU", "VAN", "MINH", "NGOC", "HONG", "HUNG", "THANH", "TAM", "HOA",
        "ANH", "THINH", "TRONG", "THANG", "HOANG", "DUC", "BAO", "QUANG", "DUY", "THANH",
        "HUNG", "PHUC", "TUAN", "HAI", "NAM", "TIEN", "THI", "HUNG", "DINH", "VAN",
        "MINH", "TRUNG", "THANH", "DUC", "TAN", "QUOC", "HONG", "NGUYEN", "VIET", "HUY",
        "PHUONG", "TRONG", "HA", "HUU", "ANH", "BAO", "NGOC", "THANH", "DUC", "TAM",
        "TIEN", "THINH", "THANG", "TRUNG", "MINH", "HAI", "QUANG", "HOANG", "THANH", "TUAN",
        "HUNG", "THANH", "HUY", "DUC", "VAN", "TRI", "PHUC", "DINH", "THAI", "HONG",
        "BAO", "CONG", "DUY", "NHAT", "DUC", "NAM", "TUNG", "HOANG", "THINH", "TIEN",
        "HA", "ANH", "HAI", "HUNG", "THI", "TAM", "THANH", "VIET", "TRUNG", "MINH",
        "HUU", "THANH", "DINH", "PHUONG", "QUOC", "TUAN", "HUY", "DUC", "VAN", "THANG",
        "HOANG"
    ]
    last_name = random.choice(last_names)
    middle_name = random.choice(middle_names + middle_names2)
    first_name = random.choice(first_names)

    if random.choice([True, False]):
        full_name = f"{last_name} {middle_name} {first_name}"
    else:
        additional_name = random.choice(middle_names + middle_names2)
        full_name = f"{last_name} {middle_name} {first_name} {additional_name}"

    return full_name


def random_birthday(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    end_date = datetime.strptime(end_date, '%Y/%m/%d')
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')


def demo_imagetotext(path: str):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    text = text.replace('/', '').replace("\n", '')
    return text[:4]


def generate_phone_number():
    phone_numbers = ["843", "843", "843", "843", "843"]
    prefix = random.choice(phone_numbers)  # Chọn một đầu số ngẫu nhiên
    suffix = ''.join(random.choices(string.digits, k=8))  # Tạo 8 số ngẫu nhiên còn lại
    phone_number = prefix + suffix  # Kết hợp đầu số và 8 số ngẫu nhiên
    return phone_number


def create_accounts(num_accounts):
    accounts = []
    for _ in range(num_accounts):
        full_name = generate_random_full_name()
        username = generate_username(full_name)
        password = generate_password()

        # URL của API
        url = "https://www.8kbbb.com/api/0.0/Home/GetCaptchaForRegister"
        response = requests.post(url)

        # Kiểm tra xem yêu cầu có thành công hay không
        if response.status_code == 200:
            data = response.json()
            image_base64 = data.get("image")
            value_key = data.get("value")

            if image_base64:
                # Giải mã base64 thành nhị phân
                image_data = base64.b64decode(image_base64)

                # Lưu ảnh dưới dạng file với đường dẫn tương đối
                image_path = f"{uuid.uuid4()}.png"
                with open(image_path, "wb") as file:
                    file.write(image_data)

                # Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối
                absolute_image_path = os.path.abspath(image_path)

                # OCR
                text = demo_imagetotext(absolute_image_path)
                os.remove(absolute_image_path)
                phone_number = generate_phone_number()

                payload = {
                    "moneyPassword": None,
                    "dealerAccount": None,
                    "parentAccount": None,
                    "adInfo": None,
                    "email": None,
                    "sex": None,
                    "idNumber": None,
                    "qqAccount": None,
                    "groupBank": None,
                    "bankName": None,
                    "bankProvince": None,
                    "bankCity": None,
                    "bankAccount": None,
                    "account": username,
                    "password": password,
                    "confirm_Password": password,
                    "name": full_name,
                    "countryCode": "84",
                    "mobile": phone_number,
                    "birthday": random_birthday("1950/01/01", "2005/12/29"),
                    "checkCodeEncrypt": value_key,
                    "checkCode": text,
                    "isRequiredMoneyPassword": False,
                }

                api_login = "https://www.8kbbb.com/api/1.0/member/register"
                response_register = requests.post(api_login, json=payload)
                if response_register.status_code == 200:
                    data = response_register.json()
                    if data.get('Result') is not None and data.get('Result') != {}:
                        print(f"Đăng ký thành công tài khoản", payload["mobile"], payload["name"], payload["account"],
                              payload["password"], payload["birthday"])
                        accounts.append({
                            "Mobile": payload["mobile"],
                            "Name": payload["name"],
                            "Username": payload["account"],
                            "Password": payload["password"],
                            "Birthday": payload["birthday"]
                        })
                    else:
                        print("Đăng ký không thành công", payload)
                else:
                    print("Đăng ký không thành công", response_register)
            else:
                
                print("Không thể giải mã captcha.")
        else:
            print("Failed to retrieve captcha. Status code:", dangthi372)

    if accounts:
        df = pd.DataFrame(accounts)
        excel_file = 'registered_accounts.xlsx'
        try:
            existing_df = pd.read_excel(excel_file)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_excel(excel_file, index=False)
        print("Thông tin tài khoản đã được lưu vào file Excel.")


# Số lượng tài khoản muốn tạo
num_accounts = int(input("Số Tài Khoản Muốn Tạo: "))
create_accounts(num_accounts)