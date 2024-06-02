import sys
import requests
import threading
import time
import os
import re
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QWidget, QGridLayout, QVBoxLayout, QWidget,QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject
from selenium import webdriver
from PyQt5.QtGui import QIcon, QPixmap
from selenium.webdriver.chrome.service import Service
from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

android_versions = ['7.0', '8.0', '9', '10', '11', '12', '12.2', '12.4', '13', '13.1', '14', '15']
ios_versions = ['12.1', '13.3', '14.0', '14.4', '15.0', '15.1.1', '15.2.1', '15.2.2']
devices_android = [
    'Nexus 5 Build/KTU84P', 'Nexus 7 Build/JOP40D', 'Nexus 10 Build/JOP40D',
    'SM-G920V Build/LMY47X', 'SAMSUNG SM-G900A Build/KOT49H', 'HTC One M8 Build/KOT49H',
    'HTC One A9 Build/MMB29M', 'SAMSUNG SM-N960F Build/PPR1.180610.011',
    'OnePlus A5010 Build/RP1A.200720.012', 'Google Pixel 4a Build/RP1A.200720.012',
    'Sony Xperia 1 II Build/55.0.A.6.16', 'Xiaomi Mi 11 Build/RP1A.200720.012',
    'Huawei P40 Pro Build/HUAWEIELS-NX9', 'LG G8 ThinQ Build/RP1A.200720.012',
    'Motorola Moto G8 Plus Build/PPIS29.65-23-11', 'Nokia 7.2 Build/RP1A.200720.012',
    'ASUS ROG Phone 3 Build/RP1A.200720.012', 'Oppo Find X2 Pro Build/RP1A.200720.012',
    'Xiaomi Redmi Note 10 Build/RP1A.200720.011', 'Xiaomi Poco X3 Build/RKQ1.200826.002',
    'Xiaomi Mi 10 Build/QKQ1.190825.002', 'Xiaomi Mi 9T Build/PKQ1.190302.001',
    'Xiaomi Mi 10 Pro Build/QKQ1.190825.002', 'Xiaomi Mi 10T Build/RP1A.200720.012',
    'Xiaomi Mi 10T Pro Build/RP1A.200720.012', 'Xiaomi Mi 11 Ultra Build/RP1A.200720.012',
    'Xiaomi Mi 11 Lite Build/RP1A.200720.012', 'Xiaomi Mi 9 Build/PKQ1.190302.001',
    'Xiaomi Mi 9T Pro Build/PKQ1.190302.001', 'Xiaomi Redmi Note 10 Pro Build/RP1A.200720.011',
    'Xiaomi Redmi Note 9 Build/PKQ1.190302.001', 'Xiaomi Redmi Note 9 Pro Build/PKQ1.190302.001',
    'Xiaomi Redmi 9 Build/PKQ1.190302.001', 'Xiaomi Redmi 9A Build/PKQ1.190302.001',
    'Xiaomi Poco X3 Pro Build/RKQ1.200826.002', 'Xiaomi Poco F2 Pro Build/RP1A.200720.012',
    'Xiaomi Poco M3 Build/QKQ1.200830.002','Huawei Y6 Build/HUAWEIMRD-LX1F','Huawei Y7 Build/HUAWEIDUB-LX1',
    'Samsung Galaxy S21 Build/RP1A.200720.012', 'Samsung Galaxy S21+ Build/RP1A.200720.012',
    'Samsung Galaxy S21 Ultra Build/RP1A.200720.012', 'Samsung Galaxy S20 Build/QKQ1.190825.002',
    'Samsung Galaxy S20+ Build/QKQ1.190825.002', 'Samsung Galaxy S20 Ultra Build/QKQ1.190825.002',
    'Samsung Galaxy Note 20 Build/RP1.200720.012', 'Samsung Galaxy Note 20 Ultra Build/RP1A.200720.012',
    'Samsung Galaxy S10 Build/PKQ1.190302.001', 'Samsung Galaxy S10+ Build/PKQ1.190302.001',
    'Samsung Galaxy S10e Build/PKQ1.190302.001', 'Samsung Galaxy Note 10 Build/QKQ1.190825.002',
    'Samsung Galaxy Note 10+ Build/QKQ1.190825.002', 'Samsung Galaxy A51 Build/RP1A.200720.012',
    'Samsung Galaxy A71 Build/RP1A.200720.012', 'Samsung Galaxy A31 Build/QKQ1.190825.002',
    'Samsung Galaxy A21s Build/QKQ1.190825.002', 'Samsung Galaxy A12 Build/RP1A.200720.012',
    'Samsung Galaxy M31 Build/QKQ1.190825.002', 'Samsung Galaxy M51 Build/QKQ1.190825.002',
    'HTC One M8 Build/KOT49H', 'HTC One M9 Build/LRX22G', 'HTC One A9 Build/MMB29M',
    'HTC One X10 Build/NRD90M', 'HTC U11 Build/NRD90M', 'HTC U11+ Build/OPR6.170623.013',
    'HTC U12+ Build/OPR6.170623.013', 'HTC Desire 20 Pro Build/QKQ1.200825.002',
    'HTC Desire 19+ Build/PPR1.180610.011', 'HTC Desire 12+ Build/OPM1.171019.011',
    'Nokia 7.2 Build/RP1A.200720.012', 'Nokia 8.3 Build/RP1A.200720.012', 'Nokia 5.4 Build/RP1A.200720.012',
    'Nokia 3.4 Build/RP1A.200720.012', 'Nokia 2.4 Build/RP1A.200720.012', 'Nokia 6.1 Build/RP1A.200720.012',
    'Nokia 6.2 Build/RP1A.200720.012', 'Nokia 7.1 Build/RP1A.200720.012', 'Nokia 8.1 Build/RP1A.200720.012',
    'Nokia 9 PureView Build/RP1A.200720.012', 'Sony Xperia 5 II Build/RP1A.200720.012',
    'Sony Xperia 10 II Build/RP1A.200720.012',    'Sony Xperia Z5 Build/RP1A.200720.012',
    'Sony Xperia 1 Build/RP1A.200720.012', 'Sony Xperia XZ3 Build/RP1A.200720.012',
    'Sony Xperia XZ2 Build/RP1A.200720.012','Huawei Mate 20 Pro Build/HUAWEILYA-L29',
    'Sony Xperia XZ1 Build/RP1A.200720.012', 'Sony Xperia XA2 Build/RP1A.200720.012',
    'Sony Xperia L4 Build/RP1A.200720.012', 'Huawei P30 Build/HUAWEIVOG-L29', 'Huawei Mate 40 Pro Build/HUAWEIANA-NX9',
    'Huawei Nova 7 Build/HUAWEIJEF-NX9', 'Huawei Y9s Build/HUAWEISTK-L22', 'Huawei P20 Build/HUAWEIEML-L29',
    'Huawei P20 Pro Build/HUAWEICLT-L29', 'Huawei Mate 20 Build/HUAWEIHMA-L29',
    'Huawei Y7a Build/HUAWEIPPA-LX2', 'Huawei P40 Pro Build/HUAWEIELS-NX9',    'Huawei P30 Build/HUAWEIELE-L29',
    'Huawei P30 Lite Build/HUAWEIMAR-LX1A','Huawei P50 Pro Build/HUAWEIJAD-AL50','Huawei Mate 30 Build/HUAWEITAS-L29',
    'Huawei P40 Build/HUAWEIANA-NX9', 'Huawei Mate 20 Build/HUAWEIHMA-L29', 'Huawei Mate 30 Pro Build/HUAWEILIO-L29',
    'Huawei P40 Pro Build/HUAWEIELS-NX9', 'Huawei Mate 20 Pro Build/HUAWEILYA-L29','Huawei Mate 40 Pro Build/HUAWEINOP-AN00',
    'Huawei P50 Build/HUAWEIABR-AL00','Huawei Mate 40 Build/HUAWEIOCE-AN00', 'Huawei Nova 5T Build/HUAWEIYAL-L21',
    'Huawei Nova 7i Build/HUAWEIJNY-LX1', 'Huawei Enjoy 20 Plus Build/HUAWEIFRL-AN00a', 'Huawei Enjoy 20 Build/HUAWEIWKG-AN00',
    'Huawei Nova 8 Build/HUAWEIANG-AN00','Huawei Enjoy 10 Build/HUAWEIART-TL00x', 'Huawei Honor X10 Build/HUAWEITEL-AN10',
    'Huawei Nova 9 Build/HUAWEINAM-AL00','Huawei Honor 50 Build/HUAWEINTH-AN00', 'Huawei Honor 20 Build/HUAWEIYAL-L21',
    'Huawei Nova 10 Build/HUAWEINCO-AL00',  'Huawei Honor 30 Build/HUAWEIBMH-AN10', 'Huawei Y9 Prime Build/HUAWEISTK-L21',
    'Huawei Y5 Build/HUAWEIAMN-LX9',  'Huawei Y9 Build/HUAWEIJKM-LX1','Huawei Enjoy Z Build/HUAWEIDVC-AN20'
]

devices_ios = [
    'iPhone 6', 'iPhone 6s', 'iPhone 7'
]

operating_systems = [
    'Windows NT 10.0; Win64; x64',
    'Windows NT 11.0; Win64; x64',
    'Windows NT 11.1.0; Win64; x64',
    'Windows NT 11.2.9; Win64; x64',
]

trinh_duyet = ['Opera', 'Edge', 'Safari', 'Firefox', 'Chrome']

def random_version():
    return f"{random.randint(50, 99)}.{random.randint(0, 999)}.{random.randint(0, 999)}.{random.randint(0, 999)}"

def random_safari_version():
    major_version = random.randint(14, 15)
    minor_version = random.randint(0, 2)
    patch_version = random.randint(0, 2)
    webkit_version = f"605.1.{random.randint(1, 999)}"
    return f"{major_version}.{minor_version}.{patch_version}/{webkit_version}"

browsers = {
    'Chrome': [random_version() for _ in range(10)],
    'Firefox': [f"{random.randint(50, 99)}.{random.randint(0, 999)}" for _ in range(10)],
    'Safari': [random_safari_version() for _ in range(10)],
    'Edge': [random_version() for _ in range(10)],
    'Opera': [random_version() for _ in range(10)]
}

def generate_random_user_agent():
    os = random.choice(operating_systems)
    browser_name = random.choice(trinh_duyet)
    browser_version = random.choice(browsers[browser_name])

    if browser_name == 'Chrome' or browser_name == 'Opera':
        user_agent = f'Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) {browser_name}/{browser_version} Safari/537.36'
    elif browser_name == 'Firefox':
        user_agent = f'Mozilla/5.0 ({os}; rv:{browser_version}) Gecko/20100101 Firefox/{browser_version}'
    elif browser_name == 'Safari':
        version, safari = browser_version.split('/')
        user_agent = f'Mozilla/5.0 ({os}) AppleWebKit/{safari} (KHTML, like Gecko) Version/{version} Safari/{safari}'
    elif browser_name == 'Edge':
        user_agent = f'Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Edg/{browser_version}'

    return user_agent

web_user_agents = [generate_random_user_agent() for _ in range(10000)]

user_agents_mobile = []

for i in range(100000):
    version = random.choice(android_versions)
    webkit_version = f"{random.randint(100, 999)}.{random.randint(100, 999)}"
    chrome_version = f"{random.randint(10, 99)}.{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)}"
    device = random.choice(devices_android)
    user_agent = f"Mozilla/5.0 (Linux; Android {version}; {device}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/{webkit_version}"
    user_agents_mobile.append(user_agent)

def get_random_user_agent(mobile=True):
    if mobile:
        return random.choice(user_agents_mobile)
    else:
        return random.choice(web_user_agents)

class SignalHandler(QObject):
    message_signal = pyqtSignal(str)

class DtProxyApp(QWidget):
    def __init__(self, index, install_crx, use_mobile_user_agent):
        super().__init__()
        self.index = index
        self.install_crx = install_crx
        self.use_mobile_user_agent = use_mobile_user_agent
        self.browsers = []
        self.stop_flag = False
        self.thread = None
        self.signals = SignalHandler()
        self.signals.message_signal.connect(self.show_message_box)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.api_key_entry = QLineEdit()
        layout.addWidget(QLabel("Proxy ĐT:"))
        layout.addWidget(self.api_key_entry)

        self.url_entry = QLineEdit()
        layout.addWidget(QLabel("Web:"))
        layout.addWidget(self.url_entry)

        self.account_entry = QLineEdit()
        layout.addWidget(QLabel("Thông Tin:"))
        layout.addWidget(self.account_entry)

        button_layout = QHBoxLayout()

        # Create the "Đăng Nhập" button
        self.login_button = QPushButton("Đăng Nhập")
        self.login_button.clicked.connect(self.on_login_button_click)
        button_layout.addWidget(self.login_button)

        # Create the "Đăng Ký" button
        self.register_button = QPushButton("Đăng Ký")
        self.register_button.clicked.connect(self.on_register_button_click)
        button_layout.addWidget(self.register_button)

        # Add the horizontal button layout to the main layout
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setWindowTitle("Proxy Dt")
        pixmap = QPixmap("crx_extensions/icon.png")
        scaled_pixmap = pixmap.scaled(100, 100)
        self.setWindowIcon(QIcon(scaled_pixmap))
        self.position_window()

    def position_window(self):
        window_width = 230
        window_height = 180
        x_offset = self.index * (window_width + 10)
        y_offset = 900
        self.setGeometry(x_offset, y_offset, window_width, window_height)

    def show_message_box(self, title, message):
        QMessageBox.information(self, title, message)

    def get_current_ip(self):
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            return response.json()["ip"]
        else:
            raise Exception("Không thể lấy địa chỉ IP hiện tại.")

    def get_proxy(self, api_key, authen_ips):
        url = f"https://app.proxydt.com/api/public/proxy/get-new-proxy?license={api_key}&authen_ips={authen_ips}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        while True:
            response = requests.get(url, headers=headers)
            print(f"API Response: {response.text}")

            if response.status_code == 200:
                data = response.json()
                if data['code'] == 1 and 'data' in data:
                    proxy_info = data['data']
                    if 'http_ipv4' in proxy_info:
                        proxy = proxy_info['http_ipv4']
                        return proxy, None
                    else:
                        self.signals.message_signal.emit("Lỗi", "Proxy không có thông tin 'http_ipv4'.")
                        return None, None
                elif data['code'] == 0:
                    wait_time = data.get('next_request', 60)
                    print(f"Thao tác đổi IP quá nhanh. Vui lòng đợi {wait_time} giây.")
                    time.sleep(wait_time)
                    continue
                else:
                    self.signals.message_signal.emit("Lỗi", f"API phản hồi thất bại:Chờ Tải Lại")
                    return None, None
            elif response.status_code == 429:
                wait_time = response.headers.get("Retry-After", 60)
                print(f"API trả về lỗi 429. Vui lòng đợi {wait_time} giây.")
                time.sleep(int(wait_time))
                continue
            else:
                self.signals.message_signal.emit("Lỗi", f"API trả về lỗi: {response.status_code} - {response.text}")
                return None, None

    def start_browser(self, proxy, crx_dir, url, action, account, password, capcha, key_capcha):
        driver = None
        try:
            if proxy.startswith("http://") or proxy.startswith("https://"):
                proxy = proxy.split("://")[1]
            proxy_host, proxy_port = proxy.split(":")
        except ValueError:
            raise Exception(f"Proxy không đúng định dạng 'IP:Port': {proxy}")

        try:
            user_agent = get_random_user_agent(self.use_mobile_user_agent)

            chrome_options = Options()
            chrome_options.add_argument(f'user-agent={user_agent}')
            chrome_options.add_argument(f'--proxy-server=http://{proxy_host}:{proxy_port}')
            chrome_options.add_argument("--window-size=504,940")
            chrome_options.add_argument("--mute-audio")
            x_offset = self.index * (504 + 1)
            y_offset = 0
            chrome_options.add_argument(f"--window-position={x_offset},{y_offset}")

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.geolocation": 2
            }
            chrome_options.add_experimental_option("prefs", prefs)

            if self.install_crx:
                for file in os.listdir(crx_dir):
                    if file.endswith(".crx"):
                        chrome_options.add_extension(os.path.join(crx_dir, file))

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(url)
            self.browsers.append(driver)

            try:
                wait = WebDriverWait(driver, 60)  # Đợi tối đa 10 giây để đảm bảo các phần tử đã sẵn sàng
                base64 = ""  # lay tu web

                if action == "login":
                    # Dán vào các trường account và password
                    account_field = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='account']")))
                    password_field = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='password']")))

                    account_field.send_keys(account)
                    password_field.send_keys(password)

                    text_capcha = demo_imagetotext(Base64=base64, url="https:....",
                                                   dst_path = "C:/Users/dang thao\Desktop\hoc\hoc_python\Buoi_6\New folder")

                    # Gửi biểu mẫu đăng nhập
                    password_field.send_keys(Keys.RETURN)

                elif action == "register":
                    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@_ngcontent-serverapp-c98='' and text()='×']")))
                    close_button.click()
                    x_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@_ngcontent-serverapp-c95='' and contains(@class, 'close absolute top-[15px] right-[15px] flex h-6 w-6 items-center justify-center text-sm') and text()='X']")))
                    x_button.click()
                    pass

            except Exception as e:
                pass
        except Exception as e:
            self.signals.message_signal.emit("Lỗi", f"Đã xảy ra lỗi: {e}")

    def main(self, api_key, url, action, account, password):
        crx_dir = "crx_extensions"

        if self.install_crx and not os.path.exists(crx_dir):
            os.makedirs(crx_dir)
            self.signals.message_signal.emit("Thông báo", f"Đã tạo thư mục '{crx_dir}'. đặt các tệp .crx vào thư mục này và chạy lại.")
            return
        elif self.install_crx and not crx_dir:
            self.signals.message_signal.emit("Thông báo", f"Thư mục '{crx_dir}' rỗng. đặt các tệp .crx vào thư mục này và chạy lại.")
            return

        try:
            authen_ip = self.get_current_ip()
        except Exception as e:
            self.signals.message_signal.emit("Lỗi", f"Đã xảy ra lỗi khi lấy địa chỉ IP: {e}")
            return

        while not self.stop_flag:
            try:
                proxy, wait_time = self.get_proxy(api_key, authen_ip)
                if proxy:
                    print(f"Proxy mới nhận được: {proxy}")

                    driver = self.start_browser(proxy, crx_dir, url, action, account, password)

                    while not self.stop_flag:
                        time.sleep(1)
                    driver.quit()
                    self.browsers.remove(driver)
                elif wait_time:
                    print(f"Thao tác đổi IP quá nhanh. Vui lòng đợi {wait_time} giây.")
                    time.sleep(wait_time)
                    print("\nBắt đầu thử lại...")
                else:
                    raise Exception("Không nhận được proxy và không có thời gian chờ.")
            except Exception as e:
                if not self.stop_flag:
                    self.signals.message_signal.emit("Lỗi", f"Đã xảy ra lỗi: {e}")
                break


    def on_login_button_click(self):
        api_key = self.api_key_entry.text()
        url = self.url_entry.text()
        account_data = self.account_entry.text()
        if not api_key or not url or not account_data:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ API Key, URL, Account và Password.")
            return

        try:
            account, password = account_data.split()
        except ValueError:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập Account và Password phân chia bởi dấu cách.")
            return

        # Cập nhật URL để thêm Account/Login
        url = self.update_url(url)

        self.login_button.setDisabled(True)
        self.thread = threading.Thread(target=self.main, args=(api_key, url, "login", account, password))
        self.thread.start()

        QTimer.singleShot(30000, self.enable_login_button)

    def update_url(self, url):
        # Xóa khoảng trắng ở cuối của URL
        url = url.rstrip()

        # Các đuôi tên miền cần kiểm tra
        domain_suffixes = ['.com', '.vn', '.org', '.vip', '.in', '.info', '.club', '.games']

        # Tạo biểu thức chính quy để kiểm tra các đuôi tên miền
        pattern = re.compile(r'(\.com|\.vn|\.org|\.vip|\.in|\.info|\.club|\.games)$')

        # Tìm kiếm các đuôi tên miền trong URL
        match = pattern.search(url)

        if match:
            base_url = url[:match.end()]
        else:
            base_url = url[:url.rfind('/')] if '/' in url else url[:-1]  # Xóa ký tự cuối cùng nếu không tìm thấy

        return f"{base_url}/Account/Login"

    def on_register_button_click(self):
        api_key = self.api_key_entry.text()
        url = self.url_entry.text()
        if not api_key or not url:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ API Key và URL.")
            return

        self.register_button.setDisabled(True)
        self.thread = threading.Thread(target=self.main, args=(api_key, url, "register", None, None))
        self.thread.start()

        QTimer.singleShot(30000, self.enable_register_button)

    def enable_login_button(self):
        self.login_button.setDisabled(False)

    def enable_register_button(self):
        self.register_button.setDisabled(False)

    def close_browsers(self):
        for browser in self.browsers:
            browser.quit()
        self.browsers = []

    def closeEvent(self, event):
        self.stop_flag = True
        for browser in self.browsers:
            browser.quit()
        if self.thread is not None:
            self.thread.join()
        event.accept()

class No1App(QWidget):
    def __init__(self, index, install_crx, use_mobile_user_agent):
        super().__init__()
        self.index = index
        self.install_crx = install_crx
        self.use_mobile_user_agent = use_mobile_user_agent
        self.browsers = []
        self.stop_flag = False
        self.thread = None
        self.signals = SignalHandler()
        self.signals.message_signal.connect(self.show_message_box)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.api_key_entry = QLineEdit()
        layout.addWidget(QLabel("No1 Proxy:"))
        layout.addWidget(self.api_key_entry)

        self.http_ipv4_entry = QLineEdit()
        layout.addWidget(QLabel("HTTP IPv4:"))
        layout.addWidget(self.http_ipv4_entry)

        self.url_entry = QLineEdit()
        layout.addWidget(QLabel("Web:"))
        layout.addWidget(self.url_entry)

        self.start_button = QPushButton("Nổ Máy")
        self.start_button.clicked.connect(self.on_start_button_click)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle("Proxy No1")
        self.position_window()

    def position_window(self):
        window_width = 230
        window_height = 180
        x_offset = self.index * (window_width + 10)
        y_offset = 800
        self.setGeometry(x_offset, y_offset, window_width, window_height)

    def show_message_box(self, title, message):
        QMessageBox.information(self, title, message)

    def get_proxy(self, api_key):
        url = f"https://app.proxyno1.com/api/change-key-ip/{api_key}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        print(f"API Response: {response.text}")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 0:
                self.signals.message_signal.emit("Thông báo", data['message'])
                time.sleep(random.randint(5, 10))
                return True
            else:
                self.signals.message_signal.emit("Lỗi", f"API phản hồi lỗi: {data.get('message', 'Không có thông tin lỗi')}")
                return False
        elif response.status_code == 429:
            wait_time = response.headers.get("Retry-After", 10)
            print(f"API trả về lỗi 429. Vui lòng đợi {wait_time} giây.")
            time.sleep(int(wait_time))
            return self.get_proxy(api_key)
        else:
            self.signals.message_signal.emit("Lỗi", f"API trả về lỗi: {response.status_code} - {response.text}")
            return False

    def start_browser(self, proxy, crx_dir, url):
        try:
            if proxy.startswith("http://") or proxy.startswith("https://"):
                proxy = proxy.split("://")[1]
            proxy_host, proxy_port = proxy.split(":")
        except ValueError:
            raise Exception(f"Proxy không đúng định dạng 'IP:Port': {proxy}")

        user_agent = get_random_user_agent(self.use_mobile_user_agent)

        chrome_options = Options()
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_argument(f'--proxy-server=http://{proxy_host}:{proxy_port}')
        chrome_options.add_argument("--window-size=504,940")
        chrome_options.add_argument("--mute-audio")
        x_offset = self.index * (504 + 1)
        y_offset = 0
        chrome_options.add_argument(f"--window-position={x_offset},{y_offset}")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.geolocation": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)

        if self.install_crx:
            for file in os.listdir(crx_dir):
                if file.endswith(".crx"):
                    chrome_options.add_extension(os.path.join(crx_dir, file))

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(url)
        except Exception as e:
            print(f"Không thể truy cập trang web: {e}")
            driver.quit()
            return None

        self.browsers.append(driver)
        return driver

    def main(self, api_key, url, http_ipv4):
        crx_dir = "crx_extensions"

        if self.install_crx and not os.path.exists(crx_dir):
            os.makedirs(crx_dir)
            self.signals.message_signal.emit("Thông báo", f"Đã tạo thư mục '{crx_dir}'. Vui lòng đặt các tệp .crx vào thư mục này và chạy lại chương trình.")
            return
        elif self.install_crx and not os.listdir(crx_dir):
            self.signals.message_signal.emit("Thông báo", f"Thư mục '{crx_dir}' rỗng. Vui lòng đặt các tệp .crx vào thư mục này và chạy lại chương trình.")
            return

        self.close_browsers()

        while not self.stop_flag:
            try:
                if self.get_proxy(api_key):
                    proxy = http_ipv4

                    if proxy:
                        print(f"Proxy mới nhận được: {proxy}")

                        driver = self.start_browser(proxy, crx_dir, url)
                        if driver:
                            while not self.stop_flag:
                                time.sleep(1)
                            driver.quit()
                            self.browsers.remove(driver)
                        else:
                            print("Thử lại với proxy khác...")
                    else:
                        raise Exception("Không nhận được proxy.")
            except Exception as e:
                if not self.stop_flag:
                    self.signals.message_signal.emit("Lỗi", f"Đã xảy ra lỗi: {e}")
                break

    def on_start_button_click(self):
        api_key = self.api_key_entry.text()
        url = self.url_entry.text()
        http_ipv4 = self.http_ipv4_entry.text()

        if not api_key or not url or not http_ipv4:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập API Key, URL và HTTP IPv4.")
            return
        self.start_button.setDisabled(True)
        self.thread = threading.Thread(target=self.main, args=(api_key, url, http_ipv4))
        self.thread.start()

        QTimer.singleShot(30000, self.enable_start_button)

    def enable_start_button(self):
        self.start_button.setDisabled(False)

    def close_browsers(self):
        for browser in self.browsers:
            browser.quit()
        self.browsers = []

    def closeEvent(self, event):
        self.stop_flag = True
        for browser in self.browsers:
            browser.quit()
        if self.thread is not None:
            self.thread.join()
        event.accept()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        layout.addWidget(QLabel("       --------->Chọn Binh Khí<---------"))

        button_layout = QHBoxLayout()

        self.button1 = QPushButton("Proxy Dt")
        self.button1.clicked.connect(self.start_dtproxy_app)
        button_layout.addWidget(self.button1)

        self.button2 = QPushButton("Proxy No1")
        self.button2.clicked.connect(self.start_no1_app)
        button_layout.addWidget(self.button2)

        layout.addLayout(button_layout)

        button_layout = QHBoxLayout()

        layout.addWidget(QLabel("Số lượng:"))
        self.num_instances_entry = QLineEdit("1")
        button_layout.addWidget(self.num_instances_entry)

        layout.addLayout(button_layout)


        self.install_crx_checkbox = QCheckBox("Cài đặt crx_extensions")
        layout.addWidget(self.install_crx_checkbox)

        self.use_mobile_user_agent_checkbox = QCheckBox("Fake Di Động")
        self.use_mobile_user_agent_checkbox.setChecked(True)
        layout.addWidget(self.use_mobile_user_agent_checkbox)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("Fake Id--Ip")
        pixmap = QPixmap("crx_extensions/icon.png")
        scaled_pixmap = pixmap.scaled(100, 100)
        self.setWindowIcon(QIcon(scaled_pixmap))
        self.instances = []

    def start_dtproxy_app(self):
        num_instances = int(self.num_instances_entry.text())
        for index in range(num_instances):
            instance = DtProxyApp(index, self.install_crx_checkbox.isChecked(), self.use_mobile_user_agent_checkbox.isChecked())
            self.instances.append(instance)
            instance.show()

    def start_no1_app(self):
        num_instances = int(self.num_instances_entry.text())
        for index in range(num_instances):
            instance = No1App(index, self.install_crx_checkbox.isChecked(), self.use_mobile_user_agent_checkbox.isChecked())
            self.instances.append(instance)
            instance.show()

    def closeEvent(self, event):
        if QMessageBox.question(self,"Thoát", "Lượn À!!!!!!!!!", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            for instance in self.instances:
                instance.stop_flag = True
            for instance in self.instances:
                if instance.thread is not None:
                    instance.thread.join()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())