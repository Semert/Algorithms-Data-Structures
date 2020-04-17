#  https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
# word = 'abc'
word = 'zaba'
# print(h.index())

# print(ord('a')-96)
def designerPdfViewer(h, word):
    index1 = []
    for a in word:
        index1.append(h[(ord(a)-97)])
    print(index1)

    return max(index1) * len(index1)
print(designerPdfViewer(h,word))

# test


