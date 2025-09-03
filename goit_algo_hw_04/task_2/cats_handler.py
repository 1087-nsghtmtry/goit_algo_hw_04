cats = []

def get_cats_info(path):
    try:
        with open(path/"cats_file.txt", "r", encoding='utf-8') as fh:
            for line in fh.readlines():
                line = line.strip().split(",")
                if len(line) == 3 and (field.strip() != '' for field in line) and line[2].isdigit():
                    cats_dict = {
                    "id": line[0],
                    "name" : line[1],
                    "age": line[2]
                        }
                    cats.append(cats_dict)
                else:
                    return "File error"
    except IndexError:
        return "Missing values"
    except FileNotFoundError:
        return "File not found"
    return cats