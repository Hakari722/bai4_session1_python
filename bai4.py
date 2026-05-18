# MODULE TIẾP NHẬN VÀ CHUẨN HÓA SINH HIỆU
# Input:
# - Mã bệnh nhân (str)
# - Nhiệt độ (input -> ép kiểu float)
# - Nhịp tim (input -> ép kiểu int)
# Giải pháp:
# 1. Ép kiểu trực tiếp:
#    float(input()), int(input())
# 2. Lưu chuỗi rồi ép kiểu
#    -> dễ debug hơn
#    -> phù hợp môi trường bệnh viện
# Thuật toán:
# 1. Nhập dữ liệu
# 2. Ép kiểu dữ liệu
# 3. Kiểm tra kiểu dữ liệu
# 4. Hiển thị kết quả


print("===== HỆ THỐNG TIẾP NHẬN SINH HIỆU =====")
patient_id = input("Nhập mã bệnh nhân: ")
temperature_str = input("Nhập nhiệt độ cơ thể: ")
heart_rate_str = input("Nhập nhịp tim: ")
temperature = float(temperature_str)
heart_rate = int(heart_rate_str)
print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_id)
print("Nhiệt độ cơ thể:", temperature, "độ C")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")