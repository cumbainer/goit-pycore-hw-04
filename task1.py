from plistlib import InvalidFileException
from typing import Tuple


def parse_salary_info(file_path: str) -> Tuple[int, float]:
   try:
       with open(file_path, mode="r") as file:
           total_salary = 0
           employees_count = 0
           while True:
               line = file.readline()
               if not line:
                   break

               try:
                   parts = line.split(",")
                   salary = int(parts[1])
                   total_salary += salary
                   employees_count += 1
               except ValueError as e:
                   raise InvalidFileException(f"Invalid file format at line: {employees_count + 1}. "
                                              f"Expected name(str),salary(int) ") from e

           average_salary = total_salary / employees_count
           return total_salary, average_salary
   except FileNotFoundError:
       raise FileNotFoundError(f"File not found at path: {file_path}. Please enter a valid path.")

file_path_task1 = "./usefrs.csv"
total_salary_r, average_salary_r = parse_salary_info(file_path_task1)
print(f"Total salary: {total_salary_r}")
print(f"Average salary: {average_salary_r}")