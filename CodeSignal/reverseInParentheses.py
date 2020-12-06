
# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    return s


