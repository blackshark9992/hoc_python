import requests
import base64
import pytesseract
from PIL import Image
import os
import uuid
import time

# URL của API
url_captcha = "https://www.8kbbb.com/api/0.0/Home/GetCaptchaForLogin"
api_login = "https://www.8kbbb.com/api/0.0/Login/login"
tien = "https://m.8kbbb.com/api/0.0/Account/GetMyBalance"
get_red_envelop_list = "https://m.8kbbb.com/api/0.0/RedEnvelope/GetRedEnvelopList"
red_envelope_received = "https://m.8kbbb.com/api/1.0/redEnvelope/received"

# Đặt đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

user = input("Tài Khoản: ")
password = input("Mật Khẩu: ")

session = requests.Session()

def demo_imagetotext(path: str):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text.replace('/', '').replace("\n", '')[:4]

def get_captcha_and_login():
    while True:
        response = session.post(url_captcha)
        if response.status_code == 200:
            data = response.json()
            image_base64 = data.get("image")
            value_key = data.get("value")

            if image_base64:
                image_data = base64.b64decode(image_base64)
                image_path = f"{uuid.uuid4()}.png"
                with open(image_path, "wb") as file:
                    file.write(image_data)
                absolute_image_path = os.path.abspath(image_path)
                text = demo_imagetotext(absolute_image_path)
                os.remove(absolute_image_path)
                print("Recognized text:", text)

                payload = {
                    "account": user,
                    "checkCode": text,
                    "checkCodeEncrypt": value_key,
                    "fingerprint": str(uuid.uuid4()),
                    "password": password
                }

                response_login = session.post(api_login, json=payload)
                if response_login.status_code == 200:
                    login_data = response_login.json()
                    if login_data.get("IsSuccess"):
                        print(f"Tài Khoản: {user}|{password}")
                        access_token = login_data.get("LoginToken").get("AccessToken")
                        get_additional_info(access_token)
                        break
                    else:
                        error_message = login_data.get("ErrorMessage")
                        print("Đăng nhập không thành công:", error_message)
                        if error_message.strip() == "Tài khoản mật khẩu sai":
                            print("Stopping due to incorrect username/password.")
                            break
                else:
                    print("Lỗi trong quá trình đăng nhập:", response_login.status_code)
            else:
                print("No image data found.")
        else:
            print("Failed to retrieve captcha. Status code:", response.status_code)
        time.sleep(1)

def get_additional_info(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    def get_balance():
        response = session.post(tien, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print("Lỗi khi lấy số dư tài khoản:", response.status_code)
            return None

    balance_before = get_balance()
    if balance_before:
        print("Số Tiền Trước:", balance_before)

    response_get_red_envelop_list = session.post(get_red_envelop_list, headers=headers)
    if response_get_red_envelop_list.status_code == 200:
        red_envelop_list_data = response_get_red_envelop_list.json()
        if isinstance(red_envelop_list_data, list):
            for red_envelop in red_envelop_list_data:
                id_from_list = red_envelop.get("Id")
                if id_from_list:
                    red_envelope_payload = {"id": id_from_list}
                    response_red_envelope = session.post(red_envelope_received, headers=headers, json=red_envelope_payload)
                    if response_red_envelope.status_code == 200:
                        print(f"Số Tiền Trong Lixi: {response_red_envelope.request.headers.get('Content-Length')}")
                        try:
                            red_envelope_data = response_red_envelope.json()
                            if red_envelope_data.get("Code") == 500:
                                print("Error:", red_envelope_data.get("Error"))
                        except ValueError:
                            print("Non-JSON response:", response_red_envelope.text)
                    else:
                        print("Lỗi khi gọi API redEnvelope/received:", response_red_envelope.status_code)
        else:
            print("Dữ liệu trả về không phải là danh sách.")
    else:
        print("Lỗi khi gọi API GetRedEnvelopList:", response_get_red_envelop_list.status_code)

    balance_after = get_balance()
    if balance_after:
        print("Số Tiền Sau:", balance_after)

get_captcha_and_login()
