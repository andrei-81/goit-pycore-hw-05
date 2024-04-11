
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Give me name and phone please."
        except KeyError: 
            return "Contact not found"

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else: 
        return f"Contact {name} already exists"


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"change {name} {phone}"
    else:
        return f"contact {name} not found" 

@input_error
def show_phone(args, contacts):
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
    print("type exit or close to exit")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
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
