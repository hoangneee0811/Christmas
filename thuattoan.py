diem_so = [7, 5, 9, 8, 4]
can_tim = 5

def linear_search(danh_sach, so_can_tim):
    for i in range(len(danh_sach)):
        print(f"Đang kiểm tra vị trí {i}, giá trị là {danh_sach[i]}")
        
        if danh_sach[i] == so_can_tim:
            return i 
    return 'Không tìm thấy' 

ket_qua = linear_search(diem_so, can_tim)
print(f"Tìm thấy số {can_tim} tại vị trí: {ket_qua}")






diem_so = [10, 22, 35, 40, 42, 55, 60, 70]
can_tim = 60

def binary_search(danh_sach, so_can_tim):
    trai = 0
    phai = len(danh_sach) - 1

    while trai <= phai:
        giua = (trai + phai) // 2 
        gia_tri_giua = danh_sach[giua]
        
        print(f"Đang xét đoạn từ {trai} đến {phai}, ở giữa là số {gia_tri_giua}")

        if gia_tri_giua == so_can_tim:
            return giua 
        elif gia_tri_giua < so_can_tim:
            trai = giua + 1 
        else:
            phai = giua - 1 
            
    return 'Không tìm thấy'

ket_qua = binary_search(diem_so, can_tim)
print(f"Số {can_tim} nằm ở vị trí: {ket_qua}")





chieu_cao = [170, 160, 180, 150]

def bubble_sort(arr):
    n = len(arr)
    # Cần lặp lại quy trình n lần
    for i in range(n):
        # Lần lượt so sánh các cặp liền kề
        for j in range(0, n - i - 1):
            # Nếu người đứng trước (j) cao hơn người đứng sau (j+1)
            if arr[j] > arr[j + 1]:
                print(f"Đổi chỗ {arr[j]} và {arr[j+1]}")
                # Cú pháp đổi chỗ siêu nhanh trong Python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

print("Danh sách ban đầu:", chieu_cao)
ket_qua = bubble_sort(chieu_cao)
print("Danh sách sau khi sắp xếp:", ket_qua)





def tinh_tong(n):
    print(f"Đang tính tổng cho n = {n}")
    
    # 1. Điểm dừng (Base case)
    if n == 1:
        print("Đã đến đáy (n=1), trả về 1")
        return 1
    
    # 2. Gọi lại chính nó (Recursive case)
    else:
        ket_qua_con = tinh_tong(n - 1)
        tong = n + ket_qua_con
        print(f"Tổng của {n} + tổng({n-1}) là: {tong}")
        return tong

print("Kết quả cuối cùng:", tinh_tong(3))