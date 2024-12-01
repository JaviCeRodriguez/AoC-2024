from typing import List

def read_data(file_path):
    left, right = [], []
    with open(file_path, 'rt') as file:
        for line in file.readlines():
            line_parsed = [int(x) for x in line.split()]
            left.append(line_parsed[0])
            right.append(line_parsed[1])
    return sorted(left), sorted(right)


def distances(left: List[int], right: List[int]) -> List[int]:
    return [abs(x - y) for x, y in zip(left, right)]


left, right = read_data('./day-01/input.txt')
distances = distances(left, right)
print("Total sum of distances:", sum(distances))