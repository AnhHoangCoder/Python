#Pipeline phan tich log

def analyze_log(filepath):
    def read_lines():
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                yield line.strip()

    error_lines = (
        line for line in read_lines()
        if " ERROR " in line
    )

    result = {}

    for line in error_lines:
        date = line.split()[0]
        result[date] = result.get(date, 0) + 1

    return result

with open("server.log", "w", encoding="utf-8") as f:
    f.write("""2024-01-01 ERROR ket noi that bai
    2024-01-01 INFO Khoi dong server
    2024-01-02 ERROR het bo nho
    2024-01-02 INFO Request thanh cong
    2024-01-02 ERROR Timeout
    2024-01-03 INFO  Xong
    """)

print(analyze_log("server.log"))