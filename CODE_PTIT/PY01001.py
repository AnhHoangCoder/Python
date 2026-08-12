# Cho một số nguyên dương N không quá 5 chữ số, hãy kiểm tra và in ra số đó chẵn hay lẻ. Nếu chẵn ghi ra chữ CHAN, nếu ngược lại ghi ra chữ LE.

# Input

# Chỉ có một dòng ghi số N

# Output

# Ghi ra kết quả trên một dòng.

# Ví dụ

# Input

# Output

# 2
	
# CHAN

# 9999

# LE

n = int(input())
print("CHAN" if n % 2 == 0 else "LE")