import json


FILENAME = "input.json"


def task() -> dict:
     #TODO считать содержимое JSON файла
    with open(FILENAME) as f:
        json_data = json.load(f)
    return max(json_data, key = lambda s: s["score"])
     #TODO найти максимальный элемент по ключу score


if __name__ == '__main__':
    print(task())
