import pathlib
from salaries import total_salary


current_path = pathlib.Path(__file__).parent
total, average = total_salary(current_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
