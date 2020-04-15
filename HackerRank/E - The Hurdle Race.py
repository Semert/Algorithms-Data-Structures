k = 4
height = [1, 6, 3, 5, 2]

def hurdleRace(k, height):
    jump = []
    for i in height:
        if(i>k):
            jump.append(i)
    if(len(jump)==0):
        return 0
    return max(jump)-k

# def hurdleRace(k, height):
#     if max(height)<k:
#             return(0)
#     return(max(height)-k)

print(hurdleRace(k,height))
