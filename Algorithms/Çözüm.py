# Happy number LeetCode
# n=19
# def isHappy(n):
#     arr = [int(x) for x in str(n)]
#     toplama = 0
#     count = 0
#     while toplama != 1:
#         for i in arr:
#             toplama += i ** 2
#         count += 1
#         arr = [int(x) for x in str(toplama)]
#         if(toplama <= 1):
#             return True
#         toplama = 0
#         if(count>15):
#             return False
#
#
# print(isHappy(n))