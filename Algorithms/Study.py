

def deneme(a):
    en_uzak = 0
    son_index = len(a)-1
    i=0
    while i < en_uzak and en_uzak < son_index:
        en_uzak = max(en_uzak, a[i] + i)
        i += 1

    return en_uzak >= son_index
