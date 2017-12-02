class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 < x < 2**31-1:
            strx = str(x)
            if abs(x) == x:
                reversedx = ''
                for i in xrange(1, len(strx)+1):
                    reversedx += strx[-i]
            else:
                reversedx = '-'
                for i in xrange(1, len(strx)):
                    reversedx += strx[-i]
            return int(reversedx)
        else:
            return 0


if __name__ == '__main__':

    test=Solution()
    print test.reverse(-123)
