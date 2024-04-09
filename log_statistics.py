import sys

def parse_log_line(line: str) -> dict:
    try:
        data, time, level, message = line.split(" ", 3)
        return {"data": data, "time": time, "level": level, "message": message.replace("\n", "")}
    except Exception as e:
        print(f"error {e}")
        print("can't parse line:")
        print(line)
        exit(1)

def load_logs(file_path: str) -> list:
    result = []
    try: 
        with open(file_path, "r") as file:
            while True: 
                line = file.readline()                
                if not line:
                    break
                result.append(parse_log_line(line))
        return result
    except Exception as e:
        print(f"error {e}")
        print(f"check file {file_path}")
        exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    result = [element for element in logs if element["level"] == level.upper()]
    return result

def count_logs_by_level(logs: list) -> dict:
    result = {}
    for item in logs:
        level = item["level"]
        if level in result:
            result[level] = result[level] + 1
        else:
            result[level] = 1
    return result

def print_statistics(logs: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for item in logs:
        print(f"{item.ljust(17)}|{str(logs[item]).center(10)}")

def print_logs_by_level(logs: list, level: str):
    print()
    print()
    print(f"# Деталі логів для рівня '{level}':")
    for item in logs: 
        print(f"{item['data']} {item['time']} - {item['message']}")


if __name__ == "__main__":
    log_list = []
    if len(sys.argv) == 1:
        print("add path to logfile as argument")
    elif len(sys.argv) > 1:
        log_list = load_logs(sys.argv[1])
        print_statistics(count_logs_by_level(log_list))
        if len(sys.argv) > 2:
            filtered_logs = filter(lambda log: log["level"] == sys.argv[2].upper(), log_list)
            print_logs_by_level(filtered_logs, sys.argv[2])