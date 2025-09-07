import pathlib

cats = []

def get_cats_info(path):
    try:
        with open(path, "r", encoding='utf-8') as fh:
            for line in fh.readlines():
                line = line.strip().split(",")
                if len(line) == 3 and line[0] != "" and line[1] !="" and line[2].isdigit():
                    cats_dict = {
                    "id": line[0],
                    "name" : line[1],
                    "age": line[2]
                        }
                    
                else:
                    print("Uncomplete entry, will be ignored in the printed list")
                    continue
                cats.append(cats_dict)
            
    except FileNotFoundError:
        return "File not found"
    return cats


def main():
    current_path = pathlib.Path(__file__).parent/"cats_file.txt"
    cats_info = get_cats_info(current_path)
    print(cats_info)


main()