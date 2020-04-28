# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    if(len(s)==1 and s[0]=="a"):
        return(n)
    else:
        div=n//len(s)
        rem=n%len(s)
        acount=s.count("a")
        remaincount=s[:rem]
        rc=remaincount.count("a")
        return(acount*div+rc)