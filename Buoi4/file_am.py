import os

import pygame
from datetime import datetime

# Khởi tạo pygame
pygame.init()

file_name = "123.mp3"
while True:
    # hen_gio = input("Hẹn Giờ: ")
    gio = input("Giờ: ")
    phut = input("phut: ")
    gio_hen = f"{gio}:{phut}"
    date = datetime.now()
    hen_gio_date = f"{date.year}/{date.month}/{date.day} {gio_hen}"
    hen_gio_date_time = datetime.strptime(hen_gio_date, "%Y/%m/%d %H:%M")
    if hen_gio_date_time < date:
        print("Mời nhập lại!")
    else:
        break
while True:
    date = datetime.now()
    date_time = datetime.strftime(date, "%H:%M")
    if date_time == gio_hen:
        print("Dậy Thôi Ông Cháu ơi")

        # Đường dẫn đến file âm thanh (đường dẫn tuyệt đối)
        file_goc = os.getcwd()
        sound_file = f"{file_goc}/{file_name}"
        # Phát âm thanh
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        # Đợi cho đến khi âm thanh kết thúc
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        break