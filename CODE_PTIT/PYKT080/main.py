def main():
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    mark = [[0 for j in range(m)] for i in range(n)]
    s = 0
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        
                        ni = i + x
                        nj = j + y
                        
                        if 0 <= ni < n and 0 <= nj < m and mark[ni][nj] == 0:
                            s += a[ni][nj]
                            mark[ni][nj] = 1
                            
    print(s)

if __name__ == "__main__":
    main()