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
