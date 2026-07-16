import json
import os


FILE = "ContactBook.json"


def load_contacts():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)



def save_contacts(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)



def add_contact(name, phone, email):

    contacts = load_contacts()

    if name in contacts:
        return False


    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)

    return True



def get_contacts():

    return load_contacts()



def update_contact(name, phone, email):

    contacts = load_contacts()


    if name not in contacts:
        return False


    contacts[name]["phone"] = phone
    contacts[name]["email"] = email


    save_contacts(contacts)

    return True




def delete_contact(name):

    contacts = load_contacts()


    if name not in contacts:
        return False


    del contacts[name]

    save_contacts(contacts)

    return True




def search_contact(query):

    contacts = load_contacts()

    result = {}


    for name,data in contacts.items():

        if query.lower() in name.lower():

            result[name] = data


    return result