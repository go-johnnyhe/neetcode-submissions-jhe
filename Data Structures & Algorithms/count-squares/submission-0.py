class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        result = 0
        for x, y in self.points:
            if x == px or y == py or abs(x-px) != abs(y-py):
                continue
            result += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]

        return result
