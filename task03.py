from collections import Counter
from pathlib import Path
import re
import sys


def parse_log_line(line: str) -> dict:
    # check if log in assumed format
    pattern = r'(\S+)\s+(\S+)\s+(\w+)\s+(.+)'
    keys = ['date', 'time', 'type', 'message']
    match = re.match(pattern, line)
    if (match):
        log_dict = dict(zip(keys, match.groups()))
        # make type uppercae to filter later
        log_dict['type'] = log_dict['type'].upper()
    else:
        # create invalid row log dict
        log_dict = dict(zip(keys, ["", "", "invalid_log", ""]))
        print('--Wrong Log line format--')
    return log_dict


def load_logs(file_path: str) -> list[str]:
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except:
        print(f'Read file {file_path} error')
    pass


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    # two cases
    # [log for log in logs if log['type'] == level]
    return list(filter(lambda log: log['type'] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    log_types = [log['type'] for log in logs]
    log_counts = Counter(log_types)
    return dict(log_counts)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for log_type, count in counts.items():
        print(f"{log_type.ljust(16)} | {count}")


def display_filtered_logs(logs: list):
    if logs:
        for log in logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print('No logs with this type')


def main():
    if (len(sys.argv) > 1):
        path = Path(sys.argv[1])
        # check path
        if (path.is_file()):
            logs = load_logs(path)
            if (logs):
                # pars file line by line
                parsed_logs = [parse_log_line(log) for log in logs]
                counted_logs = count_logs_by_level(parsed_logs)
                display_log_counts(counted_logs)
                # check if filtering needed
                if (len(sys.argv) > 2):
                    filter_level = sys.argv[2]
                    print(f"\nДеталі логів для рівня '{
                          filter_level}':")
                    filtered_logs = filter_logs_by_level(
                        parsed_logs, filter_level)
                    display_filtered_logs(filtered_logs)
        else:
            print('Wrong path')


if __name__ == "__main__":
    main()
