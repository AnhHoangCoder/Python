import sys

def main():
    tokens = sys.stdin.buffer.read().split()

    n = int(tokens[0])
    a = list(map(int, tokens[1: 1 + n]))


    a.sort()
    min1 = a[0]
    max1 = a[-1]

    maxValue = -(10 ** 3)
    if max1 <= 0:
        maxValue = max(maxValue, a[0] * a[1])
    else:
        if min1 >= 0:
            maxValue = max(maxValue, a[-1] * a[-2] * a[-3])
        else:
            maxValue = max(maxValue, a[-1] * a[-2])
            maxValue = max(maxValue, a[0] * a[1])

            maxValue = max(maxValue, a[0] * a[1] * a[-1])
            maxValue = max(maxValue, a[-1] * a[-2] * a[0])
            maxValue = max(maxValue, a[-1] * a[-2] * a[-3])

    print(maxValue)

if __name__ == "__main__":
    main()