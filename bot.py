


# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# В якості прикладу додамо декоратор input_error для обробки помилки ValueError

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner



# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."



# Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.



# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
# Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог з ботом повинен бути схожим на цей.

# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command:


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2: 
        return "Try again. Add name and phone as parameters"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict):
    if len(args) < 2: 
        return "Try again. Add name and phone as parameters"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"change {name} {phone}"
    else:
        return f"contact {name} not found" 

def show_phone(args, contacts):
    if len(args) < 1: 
        return "Try again. Add name as parameter"
    name = args[0]
    if name in contacts:
        return f"{contacts[name]} {name}"
    else:
        return f"contact with name {name} not found"

def show_all(contacts): 
    for key in contacts:
        print(f"{key} {contacts[key]}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print("type exit or close to exit")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))           
        elif command == "all":
            show_all(contacts)               
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
