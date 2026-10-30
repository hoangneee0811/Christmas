def tinh_tong(n):
    if n ==1:
        return 1
    else:
        ket_qua = tinh_tong(n-1)
        tong = n +ket_qua
        return tong
print(f"ket qua cuoi cung la:", tinh_tong(4))