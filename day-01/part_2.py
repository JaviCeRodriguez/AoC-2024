from typing import List

def read_data(file_path):
    left, right = [], []
    with open(file_path, 'rt') as file:
        for line in file.readlines():
            line_parsed = [int(x) for x in line.split()]
            left.append(line_parsed[0])
            right.append(line_parsed[1])
    return left, right


def similarity_scores(left: List[int], right: List[int]) -> List[int]:
    return [x * right.count(x) for x in left]


left, right = read_data('./day-01/input.txt')
distances = similarity_scores(left, right)
print("Total sum of similarity scores:", sum(distances))