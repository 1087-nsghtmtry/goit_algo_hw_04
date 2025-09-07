
from pathlib import Path



def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total, average, full_entry = 0, 0, 0
            salaries = ()
            lines = file.readlines()

            for line in lines:
                line_part = line.strip().split(",")
                
                if len(line_part) > 1 and line_part[0] != "" and line_part[1] != "":
                    total += float(line_part[1]) 
                    full_entry += 1
                    average = round(total/full_entry, 2)
                else:
                    print("Entry seems to be uncomplete, skip calculation")

            salaries = total, average
            print("Only complete entries will be calculated!")

        return salaries
        
    except FileNotFoundError as e:
        print(f"File not found, {e}")
        return 0,0
    

current_path = Path(__file__).parent / "employees.txt"

total, average = total_salary(current_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")