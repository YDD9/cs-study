# https://en.wikipedia.org/wiki/Flood_fill
# https://leetcode.com/contest/weekly-contest-60/problems/flood-fill/
# http://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/

def floodfill(screen, x, y, oldColor, newColor):
    if x > len(screen)-1 or y > len(screen[0])-1 or x<0 or y < 0:
        return screen
    if screen[x][y] != oldColor or oldColor == newColor:
        return screen
    screen[x][y] = newColor
    floodfill(screen, x, y+1, oldColor, newColor)
    floodfill(screen, x, y-1, oldColor, newColor)
    floodfill(screen, x-1, y, oldColor, newColor)
    floodfill(screen, x+1, y, oldColor, newColor)
    return screen
    
screen = [[ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 1.,  0.,  0.,  0.,  0.]]
screen = [[1,1,1],[1,1,0],[1,0,1]]
screen = [[0,0,0],[0,1,1]]
oldColor = 1
newColor = 1
x = 1
y = 1
print floodfill(screen, x, y, oldColor, newColor)


# https://discuss.leetcode.com/topic/112089/simple-python-solution
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # The length of image and image[0] will be in the range [1, 50].
        # The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
        # The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
        NR, NC, startColor = len(image), len(image[0]), image[sr][sc]
        if startColor == newColor:
            return image

        def floodFillHelper(r, c):
            if image[r][c] == startColor:
                print '(%d, %d)' %(r, c)
                image[r][c] = newColor
                # try to fill up, down, left, right if possible
                if c+1 < NC: floodFillHelper(r, c+1)
                if c-1 >= 0: floodFillHelper(r, c-1)
                if r+1 < NR: floodFillHelper(r+1, c)
                if r-1 >= 0: floodFillHelper(r-1, c)

        floodFillHelper(sr, sc)
        return image


# https://discuss.leetcode.com/topic/112097/easy-python-dfs-no-need-for-visited
class Solution2(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image

class Solution3(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        nr, nc, oldColor= len(image), len(image[0]), image[sr][sc]
        
        def fillRecursive(r, c):
            if r<0 or c<0 or r>=nr or c>=nc or image[r][c] != oldColor:
                return image
            image[r][c] = newColor
            fillRecursive(r, c+1)
            fillRecursive(r, c-1)
            fillRecursive(r-1, c)
            fillRecursive(r+1, c)
        # in case of same newColor given
        if oldColor != newColor:
            fillRecursive(sr, sc)
        return image

if __name__=='__main__':
    mysol = Solution3()
    screen = [[ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 1.,  0.,  0.,  0.,  0.]]
    screen = [[1,1,1],[1,1,0],[1,0,1]]       
    screen = [[0,0,0],[0,1,1]]       
    print mysol.floodFill(screen, 1, 1, 1)