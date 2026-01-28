'''write a program to fing the reverse of the given number'''
def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev

def ispalindrome(n):
    return n==reverse(n)

print(reverse(123))
print(ispalindrome(123))
print(reverse(121))
print(ispalindrome(121))

def getPalindromes(start,end):
    res=""
    for i in range(1,end+1):
        if ispalindrome(i):
            res=res+str(i)+","
    return res
print(getPalindromes(1,10000))
