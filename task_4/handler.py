def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    else:
        return "Error."
    return "Contact changed."


def show_phone(args, contacts):
    if args[0] in contacts:
        return 'Phone number: ' + f"{contacts[args[0]]}"
    else:
        return "Name not found."


def show_all(contacts):
    return contacts