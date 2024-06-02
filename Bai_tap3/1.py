import random

# Danh sách tên người
names = ["Cương", "Tú", "An", "Bình", "Chi", "Đức", "Hương", "Hải", "Thắng", "Mai",
         "Nga", "Phúc", "Quỳnh", "Sơn", "Trang", "Vân", "Xuân", "Yến", "Tâm", "Hoa",
         "Duy", "Trường", "Lan", "Nam", "Nhung", "Quân", "Thảo", "Vũ", "Ngọc", "Hùng",
         "Quang", "Hoa", "Thu", "Hải", "Hạnh", "Tâm", "Hoàng", "Hạnh", "Thịnh", "Mỹ"]

# Tạo danh sách điểm số ngẫu nhiên
scores = [random.uniform(1, 10) for _ in range(40)]

# Ghép tên và điểm số vào danh sách
data = [[name, score] for name, score in zip(names, scores)]

print(data)