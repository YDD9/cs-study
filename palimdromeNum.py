"""
Input two numbers X and Y from the keyboard.
Count of total palindrome numbers Z comes between X and Y (including X and Y)

Example of Palindrome Number
Palindromes: 5, 121, 11, 11411 
Not Palindromes: 122, 10
"""

class Solution():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def palimdrome(self):
        if self.x <= self.y:
            z = 0
            for num in range(self.x, self.y + 1):
                numStr = str(num)
                if numStr[::-1] == numStr:
                    z += 1
            return z
        else:
            self.x, self.y = self.y, self.x
            return self.palimdrome()


def palimdrome2(numStr):
    l = 0
    r = len(numStr)-1
    while l <= r:
        if numStr[l] == numStr[r]:
            l += 1
            r -= 1
        else:
            return False
    return True



if __name__=='__main__':
    sol = Solution(5, 5)
    print(sol.palimdrome())

    for i in range(100):
        if palimdrome2(str(i)):
            print i


# http://www.geeksforgeeks.org/check-number-palindrome-not-without-using-extra-space/