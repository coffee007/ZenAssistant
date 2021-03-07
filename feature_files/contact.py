import json
from fuzzywuzzy import fuzz


class Contact:
    def __init__(self, firstname, lastname='', phone=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        if phone is None:
            phone = []
        if email is None:
            email = []
        self.phone = phone
        self.email = email

    def give_phone_numbers(self):
        return "Phone numbers of {}: \n {}".format(self.firstname, "\n".join(str(x) for x in list(self.phone)))

    def give_emails(self):
        return "Email addresses of {}: \n {}".format(self.firstname, "\n".join(str(x) for x in list(self.email)))

    def details(self):
        return "\nName: {} {}\n\nPhone numbers:\n {}\n\nEmails:\n {}".format(self.firstname, self.lastname, "\n".join(str(x) for x in list(self.phone)), "\n".join(str(x) for x in list(self.email)))


def create_new_contact(firstname='', lastname='', phone_nums=None, emails=None):
    with open("feature_files/data/user_contacts.json", "r") as readfile:
        read = dict(json.load(readfile))
        readfile.close()
    new_contact = Contact(firstname.lower(), lastname.lower(), phone_nums, emails)
    if firstname in read.keys():
        return "This contact already exists"
    read.update({new_contact.firstname: {
        "lastname":new_contact.lastname,
        "phone": new_contact.phone,
        "email": new_contact.email}})
    x = open("feature_files/data/user_contacts.json", "w")
    json.dump(read, x, indent=4)
    x.close()
    return "Contact {} created.".format(firstname.capitalize())


def del_contact(firstname=''):
    with open("feature_files/data/user_contacts.json", "r") as readfile:
        read = dict(json.load(readfile))
        readfile.close()
    if firstname.lower() in read.keys():
        read.pop(firstname.lower())
        x = open("feature_files/data/user_contacts.json", "w")
        json.dump(read, x, indent=4)
        x.close()
        return "Contact {} deleted.".format(firstname.capitalize())
    else:
        return "That contact doesn't exist. Please use the correct spelling. Use 'show my contacts' or 'show one of my contacts' to see the name of the contact you wish to delete."


def show_all_the_contacts():
    with open("feature_files/data/user_contacts.json", "r") as readfile:
        read = dict(json.load(readfile))
        readfile.close()
    return str('\n\n'.join(["Name: {} {}\nPhone numbers: {}\nEmails: {}\n".format(x, read.get(x).get("lastname"), ', '.join(list(read.get(x).get("phone"))), ', '.join(list(read.get(x).get("email")))) for x in read.keys()]))


def show_one_contact(firstname=''):
    with open("feature_files/data/user_contacts.json", "r") as readfile:
        read = dict(json.load(readfile))
        readfile.close()
    max_ratio = 0
    for i in read.keys():
        x = fuzz.ratio(i, firstname)
        if x >= max_ratio:
            max_ratio = x
            firstname = i
    if max_ratio == 0:
        return "That contact doesn't exist."
    return "Name: {} {}\nPhone numbers: {}\nEmails: {}".format(firstname, read.get(firstname).get("lastname"), ', '.join(list(read.get(firstname).get("phone"))), ", ".join(list(read.get(firstname).get("email"))))
