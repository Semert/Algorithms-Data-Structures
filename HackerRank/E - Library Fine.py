# https://www.hackerrank.com/challenges/library-fine/problem
def libraryFine(d1, m1, y1, d2, m2, y2):

    if(m1==m2 and y1==y2 and d1>d2):
        return(15*(d1-d2))
    elif(y1==y2 and m1>m2):
        return(500*(m1-m2))
    elif(y1>y2):
        return 10000
    return 0

    if (y2 == y1):
        if (m2 == m1):
            if (d2 >= d1):
                return 0
            else:
                return (d1 - d2) * 15
        elif (m2 > m1):
            return 0
        else:
            return (m1 - m2) * 500
    elif (y2 > y1):
        return 0
    else:
        return 10000