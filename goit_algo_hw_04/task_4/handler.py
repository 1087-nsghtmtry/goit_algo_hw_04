def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name[0] in contacts:
        contacts[name[0]] = phone
    else:
        return "Error."
    return "Contact changed."


def show_phone(name, contacts):
    if name[0] in contacts:
        return 'Phone number: ' + f"{contacts[name[0]]}"
    else:
        return "Name not found."


def show_all(contacts):
    return contacts