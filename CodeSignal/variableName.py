def variableName(name):
    if not name[0].isdigit():
        for n in name:
            if n != '_' and not n.isalpha() and not n.isdigit():
                return False
        return True
    return False
