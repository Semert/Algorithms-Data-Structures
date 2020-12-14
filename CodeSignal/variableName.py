# https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
def variableName(name):
    if not name[0].isdigit():
        for n in name:
            if n != '_' and not n.isalpha() and not n.isdigit():
                return False
        return True
    return False
