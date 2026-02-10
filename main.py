from datetime import datetime, timedelta, date
import random
import re
from random import sample
from typing import Dict, List


#SRART TASK 1
TASK1_BIRTHDAY_PATTERN = "%Y-%m-%d"
def get_days_from_today(date_str:str) -> int:
    today = datetime.today().date()
    try:
        input_date = datetime.strptime(date_str, TASK1_BIRTHDAY_PATTERN).date()
    except ValueError as exc:
        raise ValueError("Expected date in YYYY-MM-DD format (e.g. 2026-02-05).") from exc
    return (input_date - today).days

input_string = "2026-02-04"
task1_result = get_days_from_today(input_string)
print(f"Number of days between today {input_string} is: {task1_result}")
#END TASK 1


#START TASK 2
def get_numbers_ticket(min_input:int, max_input:int, quantity_input:int) -> list[int]:
    def validate_input(min_param, max_param, quantity_param):
        if min_param < 1:
            raise ValueError("Min must be greater than 0")
        if max_param > 1000:
            raise ValueError("Max must be less than 1000")
        if (quantity_param < min_param) or (quantity_param > max_param):
            raise ValueError("Quantity must be between min and max")

    validate_input(min_input, max_input, quantity_input)

    input_range = list(range(min_input, max_input + 1))
    numbers = random.sample(input_range, k=quantity_input)
    return sorted(numbers)

task2_min_input = 4
task2_max_input = 100
task2_quantity_input = 8
task2_result = get_numbers_ticket(task2_min_input, task2_max_input, task2_quantity_input)
print(f"Number of tickets between {task2_min_input} and {task2_max_input} is: {task2_result}")
#END TASK 2


#START TASK 3
# Checks if input string (with possible spaces leftwards) starts with "+"
RE_STARTS_WITH_PLUS = r"^\s*\+"

# Removes all symbols except number and "+" sign
RE_KEEP_DIGITS_AND_PLUS_ONLY = r"[^\d+]"
RE_NON_DIGIT = r"\D"

def normalize_phone(phone_number: str) -> str:
    has_plus_prefix = bool(re.match(RE_STARTS_WITH_PLUS, phone_number))

    digits = re.sub(RE_NON_DIGIT, "", phone_number)

    if digits.startswith("380"):
        return "+" + digits

    if has_plus_prefix:
        return "+" + digits

    return "+38" + digits

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
#END TASK 3



#TASK 4
TASK4_BIRTHDAY_PATTERN = "%Y.%m.%d"
TASK4_DAYS_AHEAD = 7

def _safe_replace_year(d: date, year: int) -> date:
    try:
        return d.replace(year=year)
    except ValueError:
        return date(year, 2, 28)

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today = date.today()
    end_date = today + timedelta(days=TASK4_DAYS_AHEAD)

    out: List[Dict[str, str]] = []

    for user in users:
        bday = datetime.strptime(user["birthday"], TASK4_BIRTHDAY_PATTERN).date()

        next_bday = _safe_replace_year(bday, today.year)
        if next_bday < today:
            next_bday = _safe_replace_year(bday, today.year + 1)

        if not (today <= next_bday <= end_date):
            continue

        congrat = next_bday
        if congrat.weekday() == 5:
            congrat += timedelta(days=2)
        elif congrat.weekday() == 6:
            congrat += timedelta(days=1)

        out.append({
            "name": user.get("name", ""),
            "congratulation_date": congrat.strftime(TASK4_BIRTHDAY_PATTERN),
        })

    return out

users_input = [
    {"name": "Dendi Pudge", "birthday": "2002.02.13"},
    {"name": "Jane Smith", "birthday": "2007.02.10"}
]
task4_result = get_upcoming_birthdays(users_input)
print("Cписок привітань на цьому тижні:", task4_result)
#END TASK 4