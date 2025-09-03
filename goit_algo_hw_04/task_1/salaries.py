def total_salary(path):
    try:
        with open(path/"employees.txt", "r", encoding="utf-8") as file:
            try:
                sum, average = 0, 0
                salaries = {}
                lines = file.readlines()
                for line in lines:
                    line = line.split(",")
                    if not line[0] =="":
                        sum += int(line[1])
                        average = sum//len(lines)
                        salaries = sum, average
                    else:
                        print("Damaged file: missing employee's key")
                        return 0, 0
                return salaries
            except ValueError:
                print("Damadged file: missing value for salary")
                return 0, 0
    except FileNotFoundError:
        print("File not found")
        return 0, 0

