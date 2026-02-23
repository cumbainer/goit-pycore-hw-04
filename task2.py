from typing import List, Dict

file_path_task2 = "./cats.csv"


def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_info = []

    try:
        with open(path, mode="r") as file:
            for line in file.readlines():
                parts = line.strip().split(",")
                cat_id = str(parts[0])
                name = str(parts[1])
                age = int(parts[2])

                entry = {"id": cat_id, "name": name, "age": age}
                cats_info.append(entry)

        return cats_info
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path_task2}. Please enter a valid path.")

cats_info_result = get_cats_info(file_path_task2)
for cat in cats_info_result:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")