def main():
    for _ in range(int(input().strip())):
        s = input()
        n = input()
    
        cnt = 0
        l = len(n)

        i = 0
        while i <= len(s) - 3:
            if s[i] == n[0]:
                tmp = s[i : i + l]
                if tmp == n:
                    cnt += 1
                    i += l
                    continue
            i += 1
            
        print(cnt)
            

if __name__ == "__main__":
    main()