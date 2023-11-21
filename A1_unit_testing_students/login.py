import json


# Login as a user
def login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    # Look for user in database
    with open('users.json', "r") as file:
        data = json.load(file)
        for entry in data:
            if entry["username"] == username and entry["password"] == password:
                print("Successfully logged in")
                return {"username": entry["username"], "wallet": entry["wallet"]}
        #print("Either username or password were incorrect")
    ############# added code
    answer = input("No user found, Would you like to register?: ")
    if answer == "yes":
        password_answer = input("Please input password: ")
        if len(password_answer) < 8:
            print("Length too short")
            return None
        uppercase = False
        special_character = False
        for char in password_answer:
            if char.isupper():
                uppercase = True
            elif not char.isalnum():
                special_character = True
        if uppercase and special_character:
            with open('users.json', "r") as file:
                data = json.load(file)
                new_user = {
                    "username": username,
                    "password": password_answer,
                    "wallet": 0
                }
                data.append(new_user)
            with open('users.json', "w") as file:
                json.dump(data, file, indent=1)
                return new_user
    ############# added code
    return None
