#  https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    turns = 0
    # if page to be turned to <= half of total number of pages
    # we turn the pages from the start of the book
    if p <= n / 2:
        for i in range(p // 2):
            turns += 1

    # else we turn the pages from the end of the book
    else:
        # added below if because the last page can be even or odd
        if n % 2 == 0: n += 1
        for i in range((n - p) // 2):
            turns += 1

print(ord("a")-96)