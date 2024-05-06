from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f"Value Error: {str(error)}"
        except KeyError as error:
            return f"Key Error: {str(error)}"

    return inner

def require_two_args(func):
    @wraps(func)
    def inner(args, contacts):
        if (len(args) != 2):
            raise ValueError('Operation Requires 2 args: name and phone')
        return func(args, contacts)
    
    return inner


def name_min_length(func):
    @wraps(func)
    def inner(args, contacts):
        if (len(args[0])<= 3):
            raise ValueError('Name should be more the 3 symbols')
        return func(args, contacts)

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
@require_two_args
@name_min_length
def add_contact(args, contacts):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')

    if (exists(name, contacts)):
        raise KeyError('The user is already exsist')

    contacts[name] = phone
    return "Contact added."

@input_error
@require_two_args
@name_min_length
def change_contact(args, contacts):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')

    if (not exists(name, contacts)):
        raise KeyError('The user is not exsist')
    
    contacts[name] = phone
    return "Contact updated."
    
@input_error
def get_contact_phone(args, contacts):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    if (not name):
        raise ValueError('Name shouldn\'t be empty')
    
    if (not exists(name, contacts)):
        raise KeyError('The user is not exsist')
    
    return contacts[name]


def get_all(contacts):
    res = ''
    for name, phone in contacts.items():
        res += f"{name} {phone}\n"
    return res


def exists(name, contacts):
    return name in contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
