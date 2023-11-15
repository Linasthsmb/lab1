import json


def task() -> float:
    s = 0.0
    with open("input.json", 'r') as f:
        data = json.load(f)
        for i in data:
            s += i["score"] * i["weight"]
    return round(s, 3)


print(task())
