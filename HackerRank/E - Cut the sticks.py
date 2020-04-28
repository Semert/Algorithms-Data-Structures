# https://www.hackerrank.com/challenges / cut - the - sticks / problem


def cutTheSticks(arr):
    a = arr
    lengths = []
    # lengths = [len(a)]
    while len(a) != 0:

        lengths.append(len(a))
        cuted_length_arr = []
        sub = min(a)

        for i in a:
            cut = i - sub
            if cut != 0:
                cuted_length_arr.append(cut)

        a = cuted_length_arr

    return lengths