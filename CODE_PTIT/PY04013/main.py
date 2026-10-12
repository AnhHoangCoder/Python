from rainfall import Rainfall

def main():
    stations = {}
    for _ in range(int(input())):
        name = input().strip()
        start = input().strip()
        end = input().strip()
        rain = float(input())

        r = Rainfall(name, start, end, rain)
        if name in stations:
            stations[name] += r
        else:
            stations[name] = r

    for i, (name, st) in enumerate(stations.items(), start=1):
        print(f"T{i:02d} {st}")

if __name__ == "__main__":
    main()