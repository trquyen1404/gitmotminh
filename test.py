
import matplotlib
matplotlib.use('Agg')  # Chuyển backend sang lưu file (phù hợp chạy trên Server SSH)
import matplotlib.pyplot as plt

# 1. Nhập số sinh viên nam, nữ trong 1 lớp
nam = int(input("Nhập số sinh viên Nam: "))
nu = int(input("Nhập số sinh viên Nữ: "))

# 2. Hiển thị biểu đồ cột số sinh viên nam nữ
categories = ['Nam', 'Nữ']
quantities = [nam, nu]

plt.figure(figsize=(6, 5))
plt.bar(categories, quantities, color=['#1f77b4', '#e377c2'], width=0.4)
plt.title('THỐNG KÊ SỐ LƯỢNG SINH VIÊN NAM NỮ')
plt.xlabel('Giới tính')
plt.ylabel('Số lượng (Sinh viên)')

# Hiển thị giá trị cụ thể trên đỉnh mỗi cột
for i, val in enumerate(quantities):
    plt.text(i, val + 0.1, str(val), ha='center', fontweight='bold')

# Lưu biểu đồ thành file ảnh
plt.savefig('bieudo_nam_nu.png', dpi=300)
print("Đã vẽ và lưu biểu đồ vào file bieudo_nam_nu.png thành công!")
