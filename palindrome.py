
def isPalindrome(x: int):
    x = str(x)
    for i in x:
        if x == x[::-1]:
            return True
        else:
            return False


x = 121
print(isPalindrome(x))
