
def get_user_by_id(id):
    return User("czf", "fish")

class User(object):
    def __init__(self, user, password):
        self.id = 5
        self.name = user
        self.password = password
        pass

def validate_user(username, password):
    if username == "czf" and password == "fish":
        return User(username, password)
    else:
        return None

def get_fish_by_user_id(id):
    if id == 5:
        return ["Trout", "Salmon", "Ichthyosaur"]
    else:
        return []
