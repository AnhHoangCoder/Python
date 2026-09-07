# Cho hai số nguyên N và X.

# Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.

# Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32

# Input

# Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)

# Output

# Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.

# Ví dụ

# Input

# Output

# 5 4

	
# 4 6 9 14 21 32

def sang_prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def main():
    n, x = map(int, input().split())
    #Get n so dau tien
    primes = sang_prime(10000)[:n]
    res = [x]
    cur = x

    for i in primes:
        cur += i
        res.append(cur)
    print(*res)

if __name__ == "__main__":
    main()