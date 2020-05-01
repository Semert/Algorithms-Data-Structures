# https://www.hackerrank.com/challenges/taum-and-bday/problem
def taumBday(b, w, bc, wc, z):
    diff=abs(bc-wc)
    if diff<=z:
        return b*bc+w*wc
    else:
        if bc>wc:
            return (b+w)*wc+b*z
        else:
            return (b+w)*bc+w*z