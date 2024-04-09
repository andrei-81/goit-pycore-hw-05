from typing import Callable

def generator_numbers(text: str):
    text_array = text.split(" ")
    float_array = [float(item) for item in text_array if item.replace(".", "").isdigit()]
    for result in float_array:
        yield result

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    sum = float(0)
    for element in generator_numbers(text):
        sum = sum + element
    return sum
        

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")