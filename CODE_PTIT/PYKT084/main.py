def main():
    res = {}
    flag = False

    current = ""
    for _ in range(int(input().strip())):
        line = input().strip()
        if len(line) == 0:
            flag = False
            continue

        
        if flag:
            res[current] += 1
        else:
            res[line] = 0
            current = line
            flag = True

    for key, value in res.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()