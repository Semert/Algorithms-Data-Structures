S = "RLRRLLRLRRLL"
# LLRLRLRLRLRLRR
# ht = {}
# for i in range(len(S)):
#     ht[S[i]] = i
# print(ht)
# s = enumerate(S)
# # for index,item in enumerate(len(S)):
# #     print(item)
# s = list(s)
# print(s)
# print(s[0])
# print(s[0][0])
# print(s[0][1])
# count = 0
# newarr=[]
# for i in range(len(S)-1):
#     for j in range(1,len(S)):
#         if(S[i]!=S[j]):
#             newarr.append(S[i]!=S[j])
#             i += 1
#             break
#         if(S[i]==S[j]):

#
# s = "RLRRLLRLRRLLRLRL"
# s = "LLRLRLRLRR"
s = "RLLLRRRLLR"
# ht = {}
# for i in range(len(s)):
#     if s[i] in ht:
#         ht[s[i]] += 1
#     else:
#         ht[s[i]] = 1
#
#     if(ht['L'] != ht['L']):
#         print(ht[s[i]])
#     # print(ht)
# # print(ht)
# i = 0
# for k,v in ht.items():
#     print(k,v)

def next_number(s):
    result = []
    i = 0
    yenisayac = 0
    sayac = 0
    teksayac = 0
    flag = False
    sonuc2 =0
    sonuc1=0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
            if(count==3):
                i

        result.append(str(count) + s[i])
        print(count)

        if(count==sayac ):
            yenisayac += 1
            flag = True
        if(flag):
            teksayac +=1
        if(count>1):
            sayac = count
            flag = False
        # else:
        #     teksayac += 1
        i += 1
    # print(result)
    if(yenisayac>2):
        sonuc2 = ((yenisayac+1)//2)

    sonuc1 = ((teksayac+1)//2)
    return sonuc1+sonuc2

