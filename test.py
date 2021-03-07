
def edit_a_contact(firstname, key_to_edit, new_value):
    keys = ['lastname', 'phone', 'email']
    max_match = 0
    for key in keys:
        x = fuzz.ratio(key, key_to_edit)
        if x >= max_match:
            key_to_edit = key
            max_match = x
    with open("feature_files/data/user_contacts.json", "r") as readfile:
        read = dict(json.load(readfile))
        readfile.close()
    if firstname.lower() in read.keys():
        if key_to_edit!='lastname':
            read[firstname.lower()] = list(dict(read[firstname.lower()])[key_to_edit]).append(new_value)
        else:
            read[firstname.lower()] = dict(read[firstname.lower()])[key_to_edit] = new_value
        x = open("feature_files/data/user_contacts.json", "w")
        json.dump(read, x)
        x.close()
        return "Contact edited."
    else:
        return "That contact doesn't exist."