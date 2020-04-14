x = 1
y = 2
z = 3

def catAndMouse(x, y, z):
    if(abs(x-z) == abs(y-z)):
        return "Mouse C"
    if(abs(x-z) < abs(y-z)):
        return "Cat A"
    else:
        return "Cat B"

print(catAndMouse(x,y,z))