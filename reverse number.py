'''write a program to fing the reverse of the given number'''
def reverse(num):
    rev = 0
    while num>0:
        rev = rev *10+num%10
        num//=10
    return rev
def ispalindrome(num):
    return num==reverse(num)
print(reverse(123))
print(ispalindrome(123))
print(reverse(121))
print(ispalindrome(121))
 
