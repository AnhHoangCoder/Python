from collections import Counter

def main():
    res = []
    t = int(input().strip())
    for i in range(1, t + 1):
        s1 = input().strip()
        s2 = input().strip()

        if Counter(s1) == Counter(s2):
            res.append(f"Test {i}: YES")
        else:
            res.append(f"Test {i}: NO")

    print("\n".join(res))

if __name__ == "__main__":
    main()