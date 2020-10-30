users = {'a':"abcd", 'b': 'bork', }



def accept_login(users, username, password):
    for i in users:
        if i == username:
            if users.get(i) == password:
                return True
        else:
            return False

print(accept_login(users, 'd', 'abcd'))
