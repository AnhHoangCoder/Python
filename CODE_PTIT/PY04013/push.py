class Rainfall:
    def __init__(self, name, start, end, rain):
        self.name = name
        hours1, minutes1 = map(int, start.split(":"))
        hours2, minutes2 = map(int, end.split(":"))
        self.duration = (hours2 - hours1) * 60 + minutes2 - minutes1
        self.rain = float(rain)
    
    def __add__(self, other):
        self.duration += other.duration
        self.rain += other.rain
        return self

    def average(self):
        if(self.duration == 0):
            return 0
        return self.rain / self.duration * 60

    def __str__(self):
        return f"{self.name} {self.average():.2f}"

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