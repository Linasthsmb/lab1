import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='\n')
        data = [row for row in reader]
        with open(OUTPUT_FILENAME, 'w') as o:
            json.dump(data, o, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
