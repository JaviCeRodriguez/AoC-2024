from typing import List


def read_data(file_path: str) -> List[List[int]]:
    data = []
    with open(file_path, 'rt') as file:
        for line in file.readlines():
            levels = [int(x) for x in line.split()]
            data.append(levels)
    return data


def get_diff_removing_level(report: List[int], idx: int) -> List[int]:
    differences = []
    new_report = report[:idx] + report[idx + 1:]
    for idx in range(1, len(new_report)):
        differences.append(new_report[idx] - new_report[idx - 1])
    return differences


def validate_differences(report: List[int]) -> bool:
    for diff in report:
        if not (abs(diff) >= 1 and abs(diff) <= 3):
            return False
    return True


def is_increasing(report: List[int]) -> bool:
    return all(x > 0 for x in report)


def is_decreasing(report: List[int]) -> bool:
    return is_increasing([-x for x in report])


def is_safe(report: List[int]) -> bool:
    return (is_increasing(report) or is_decreasing(report)) and validate_differences(report)


def get_safe_reports(reports: List[List[int]]) -> int:
    safe_reports = 0
    for report in reports:
        # Check if all elements are positive or negative, not both. And check if all elements are between 1 and 3
        if is_safe(report):
            safe_reports += 1
        else:
            # Check if removing one level makes the report safe
            for idx in range(len(report)):
                if is_safe(get_diff_removing_level(report, idx)):
                    safe_reports += 1
                    break
        
    return safe_reports


reports = read_data('./day-02/input.txt')
safe_reports = get_safe_reports(reports)
print(f"Safe reports: {safe_reports}")
