import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME) as f:
        json_data = json.load(f)
    lst = sorted(json_data, key=lambda i: i["id"])
    return lst
    ...  # TODO отсортировать и вернуть список словарей


if __name__ == '__main__':
    # Необходимо для проверки
    data = task()
    print(json.dumps(data, indent=4))
