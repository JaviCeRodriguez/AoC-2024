from typing import List


def read_data(file_path: str) -> List[List[int]]:
    data = []
    with open(file_path, 'rt') as file:
        for line in file.readlines():
            levels = [int(x) for x in line.split()]
            data.append(levels)
    return data


def get_reports(data: List[List[int]]) -> List[List[int]]:
    reports = []
    for levels in data:
        differences = []
        for idx in range(1, len(levels)):
            differences.append(levels[idx] - levels[idx - 1])
        reports.append(differences)
    return reports


def validate_differences(report: List[int]) -> bool:
    for diff in report:
        if not (abs(diff) >= 1 and abs(diff) <= 3):
            return False
    return True


def get_safe_reports(reports: List[List[int]]) -> int:
    safe_reports = 0
    for report in reports:
        # Check if all elements are positive or negative, not both
        if all(x > 0 for x in report) or all(x < 0 for x in report):
            # Check if all elements are between 1 and 3
            if validate_differences(report):
                safe_reports += 1
    return safe_reports

data = read_data('./day-02/input.txt')
reports = get_reports(data)
safe_reports = get_safe_reports(reports)
print(f"Safe reports: {safe_reports}")
