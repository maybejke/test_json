import json

file_name = "../../../data_2.json"


def r_json(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.loads(read_file.read())
        dt = []
        for el in data:
            if el['DIM_2955'] == 2.0:
                dt.append(el)
            elif el['DIM_2955'] == 3.0:
                dt.append(el)
        print(dt)


def main():
    r_json(file_name)


if __name__ == '__main__':
    main()
