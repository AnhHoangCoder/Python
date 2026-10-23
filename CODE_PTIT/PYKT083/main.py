def main():
    t = int(input().strip())

    bang_gia = {
        ("Xe_con", "5"): 10000,
        ("Xe_con", "7"): 15000,
        ("Xe_tai", "2"): 20000,
        ("Xe_khach", "29"): 50000,
        ("Xe_khach", "45"): 70000
    }

    tong_tien = {}

    for _ in range(t):
        s = input().strip()
        a = s.split()

        loai_xe, count, di_chuyen, ngay = a[1], a[2], a[3], a[4]
        
        if di_chuyen == "OUT":
            phi = 0
        else:
            phi = bang_gia[(loai_xe, count)]

        tong_tien[ngay] = tong_tien.get(ngay, 0) + phi

    for day, money in tong_tien.items():
        print(f"{day}: {money}")

if __name__ == "__main__":
    main()