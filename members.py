library_members = []

def register_member(name):
    while name not in library_members:
        library_members.append(name)
        return f'{name}, you are now registered!'
        break
    else:
        return f"{name}, it seems that you are already registered."

def find_member(name):
    for member in library_members:
        if name == member:
            return f"{name} is a member."
        else:
            return f"{name} is not a member."

